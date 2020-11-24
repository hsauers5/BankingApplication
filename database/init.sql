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

INSERT INTO db.users (Username, Name, PasswordHash, Account1ID, Account2ID) VALUES ("harry", "harry sauers", "C27E5A5B42AD5F7C1204E36DE2C569C37496FC41213960A147BE53B1DF2867FC", 1, 2);

INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("harry", "Checking", 500.00);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("harry", "Savings", 1000.00);

INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604961965, 100.00, 1, 2);
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604934572, 125.00, 2, 1);

-- ==================
-- passwords for marselluswallace and vincentvega are just "password"
INSERT INTO db.users (Username, Name, PasswordHash, Account1ID, Account2ID) VALUES ("marselluswallace", "marsellus wallace", "5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8", 3, 4);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("marselluswallace", "Checking", 300.00);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("marselluswallace", "Savings", 1200.00);

INSERT INTO db.users (Username, Name, PasswordHash, Account1ID, Account2ID) VALUES ("vincentvega", "vincent vega", "5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8", 5, 6);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("vincentvega", "Checking", 100000.00);
INSERT INTO db.accounts (Username, Type, Balance)  VALUES ("vincentvega", "Savings", 1200000.00);

-- ==========

INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604961965, 80.00, 3, 4);
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1604934572, 34.00, 4, 3);

-- harry & marselluswallace send money
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1585073799, 500.00, 1, 3);
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1606240000, 600.00, 3, 1);


-- marselluswallace & vincentvega send money
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1585073799, 500.00, 3, 5);
INSERT INTO db.transactions (Datetime, Amount, FromID, ToID) VALUES (1606240000, 600.00, 5, 4);
