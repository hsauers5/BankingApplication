CREATE TABLE db.users (
    Username VARCHAR(255) NOT NULL,
    Name VARCHAR(255),
    PasswordHash VARCHAR(255),
    Account1ID int,
    Account2ID int,
    PRIMARY KEY (Username)
);

CREATE TABLE db.accounts (
    ID int NOT NULL AUTO_INCREMENT,
    Username VARCHAR(255),
    Type VARCHAR(255),
    Balance float,
--    FOREIGN KEY (Username)
--        REFERENCES db.users(Username),
    PRIMARY KEY (ID)
);

CREATE TABLE db.transactions (
    ID int NOT NULL AUTO_INCREMENT,
    Datetime int,
    Amount float,
    FromID int,
    ToID int,
--    FOREIGN KEY (FromID)
--        REFERENCES db.accounts(ID),
--    FOREIGN KEY (ToID)
--        REFERENCES db.accounts(ID),
    PRIMARY KEY (ID)
);

INSERT INTO db.users (Username, Name, PasswordHash, Account1ID, Account2ID) VALUES ("harry", "harry sauers", "76D8E42E1BA899A20C2EA30A35359D5D23ECECABF4F8646BDBCB05DDBEF9A9CB", 1, 2);

INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("harry", "Checking", 500.00);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("harry", "Savings", 1000.00);

INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604961965, 100.00, 1, 2);
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604934572, 125.00, 2, 1);

-- ==================
INSERT INTO db.users (Username, Name, PasswordHash, Account1ID, Account2ID) VALUES ("user", "john doe", "76D8E42E1BA899A20C2EA30A35359D5D23ECECABF4F8646BDBCB05DDBEF9A9CB", 3, 4);

INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("user", "Checking", 300.00);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("user", "Savings", 1200.00);

INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604961965, 80.00, 1, 2);
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604934572, 34.00, 2, 1);
