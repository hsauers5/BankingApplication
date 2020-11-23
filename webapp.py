from flask import Flask, jsonify, request, abort, render_template
from database_connector import DatabaseConnector
from auth_manager import AuthManager
from accounts_manager import AccountsManager
from transactions_manager import TransactionsManager
import time


database_connector = DatabaseConnector()
auth_manager = AuthManager(database_connector)
accounts_manager = AccountsManager(database_connector)
transactions_manager = TransactionsManager(database_connector, accounts_manager)

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/auth', methods=['POST'])
def get_token():
    """
    HTTP POST /auth:
    {
        username: username,
        password: password
    }
    """
    if 'username' not in request.form or 'password' not in request.form:
        abort(400, 'Username or password missing from form-data. ')

    username = request.form['username']
    password = request.form['password']

    # validate untrusted user input
    if len(username) > 256 or len(password) > 256:
        abort(400)

    # check auth
    auth = auth_manager.check_auth(username, password)
    if not auth:
        abort(401)
    else:
        return auth_manager.generate_token(username, password)


@app.route('/token', methods=['POST'])
def check_auth():
    if 'token' not in request.form:
        abort(400, 'Token not in request form.')

    check_token(request)
    return jsonify(True)


def check_token(req):
    if 'token' not in req.form:
        abort(401)

    token = req.form['token']
    if len(token) > 256:
        abort(400).form['token']

    auth = auth_manager.check_token(token)

    if not auth:
        abort(401)
    else:
        return True


def get_value_from_request(req, key):
    if key not in req.form:
        abort(400, f'{key} missing from request form-data. ')

    value = req.form[key]
    return value


def get_username_from_request(req):
    if 'username' not in req.form and 'token' not in req.form:
        abort(400, 'Please double-check your form-data - username/token is missing.')

    if 'username' in req.form:
        username = req.form['username']
    elif 'token' in request.form:
        username = auth_manager.get_username_from_token(req.form['token'])
        if not username:
            abort(400, 'Please double-check your form-data - username/token may be missing or incorrect.')

    return username


@app.route('/accounts', methods=['POST'])
def fetch_accounts():
    check_token(request)
    username = get_username_from_request(request)
    accounts = accounts_manager.fetch_accounts(username)

    return jsonify([account.json() for account in accounts])


@app.route('/balance', methods=['POST'])
def check_balance():
    check_token(request)
    username = get_username_from_request(request)
    account_type = get_value_from_request(request, 'account')

    account_balance = accounts_manager.fetch_account_balance(username, account_type)
    if account_balance:
        return jsonify(account_balance)
    else:
        abort(400, 'The selected account does not exist. ')


@app.route('/transactions', methods=['POST'])
def fetch_transactions():
    check_token(request)
    username = get_username_from_request(request)

    transactions = [t.json() for t in transactions_manager.fetch_all_transactions(username)]
    return jsonify(transactions)


@app.route('/sendmoney', methods=['POST'])
def send_money():
    check_token(request)
    try:
        amount = float(get_value_from_request(request, 'amount'))
        timestamp = int(time.time())
        from_id = int(get_value_from_request(request, 'from'))
        to_id = int(get_value_from_request(request, 'to'))
    except TypeError:
        abort(400, 'Wrong data types!')

    username = get_username_from_request(request)

    # validate input
    if amount < 0:
        abort(400, 'Cannot send negative balance.')

    # ensure sender is owner of account
    if not accounts_manager.user_has_account(username, from_id):
        abort(403, f'You {username} do not have an account with the ID {from_id}')

    # ensure sender has enough funds
    if not accounts_manager.account_has_sufficient_funds(from_id, amount):
        abort(400, 'Insufficient balance!')

    tx = transactions_manager.send_money(amount, timestamp, from_id, to_id)
    if tx:
        return jsonify(success=True)
    else:
        abort(400, 'Please double-check your data and try again. One or more accounts may not exist.')


# @TODO remove
@app.route('/db')
def db():
    res = {
        'users': database_connector.execute_query('SELECT * FROM users;'),
        'accounts': database_connector.execute_query('SELECT * FROM accounts;'),
        'transactions': database_connector.execute_query('SELECT * FROM transactions;')
    }
    return jsonify(res)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/accounts')
def homepage():
    return render_template('homepage.html')


@app.route('/transactions', methods=['GET'])
def transactions():
    return render_template('transactions.html')


@app.route('/sendmoney', methods=['GET'])
def sendmoney():
    return render_template('sendmoney.html')

def run():
    app.run(debug=True, host='0.0.0.0', port=5000)
