-- Let me do some shady stuff
SET FOREIGN_KEY_CHECKS=0;

-- Generates schema Musikdong
DROP SCHEMA IF EXISTS `musikdong`;
CREATE SCHEMA IF NOT EXISTS `musikdong` ;
USE `musikdong` ;

-- Create table Category
-- +-------+-------------+------+-----+---------+-------+
-- | Field | Type        | Null | Key | Default | Extra |
-- +-------+-------------+------+-----+---------+-------+
-- | name  | varchar(45) | NO   | PRI | NULL    |       |
-- +-------+-------------+------+-----+---------+-------+

DROP TABLE IF EXISTS Category;
CREATE TABLE Category (
	`name` VARCHAR(45) NOT NULL,
	PRIMARY KEY (`name`)
);

-- Create table Products
-- +-------------+-------------+------+-----+---------+-------+
-- | Field       | Type        | Null | Key | Default | Extra |
-- +-------------+-------------+------+-----+---------+-------+
-- | id          | varchar(6)  | NO   | PRI | NULL    |       |
-- | name        | varchar(45) | NO   |     | NULL    |       |
-- | price       | float       | YES  |     | 0       |       |
-- | description | longtext    | YES  |     | NULL    |       |
-- | imageUrl    | varchar(45) | YES  |     | NULL    |       |
-- | category    | varchar(45) | YES  | MUL | NULL    |       |
-- +-------------+-------------+------+-----+---------+-------+

DROP TABLE IF EXISTS Products ;
CREATE TABLE IF NOT EXISTS Products (
	`id` VARCHAR(6) NOT NULL,
	`name` VARCHAR(45) NOT NULL,
	`price` FLOAT NULL DEFAULT 0,
	`description` LONGTEXT NULL,
	`imageUrl` VARCHAR(45) NULL,
	`category` VARCHAR(45) NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (category) REFERENCES Category(name)
);

-- Create table TagTypes
-- +-------+-------------+------+-----+---------+-------+
-- | Field | Type        | Null | Key | Default | Extra |
-- +-------+-------------+------+-----+---------+-------+
-- | name  | varchar(45) | NO   | PRI | NULL    |       |
-- +-------+-------------+------+-----+---------+-------+

DROP TABLE IF EXISTS TagTypes;
CREATE TABLE IF NOT EXISTS TagTypes (
	`name` VARCHAR(45) NOT NULL,
	PRIMARY KEY (`name`)
);

-- Create table Tag
-- +-------------+-------------+------+-----+---------+-------+
-- | Field       | Type        | Null | Key | Default | Extra |
-- +-------------+-------------+------+-----+---------+-------+
-- | productId   | varchar(6)  | NO   | PRI | NULL    |       |
-- | tagTypeName | varchar(45) | NO   | PRI | NULL    |       |
-- +-------------+-------------+------+-----+---------+-------+

DROP TABLE IF EXISTS Tag;
CREATE TABLE IF NOT EXISTS Tag (
	`productId` VARCHAR(6) NOT NULL,
	`tagTypeName` VARCHAR(45) NOT NULL,
	PRIMARY KEY (`productId`, `tagTypeName`),
	FOREIGN KEY (`productId`)
    REFERENCES `musikdong`.`Products` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
    FOREIGN KEY (`tagTypeName`)
    REFERENCES `musikdong`.`TagTypes` (`name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Create table User
-- +----------+-------------+------+-----+---------+----------------+
-- | Field    | Type        | Null | Key | Default | Extra          |
-- +----------+-------------+------+-----+---------+----------------+
-- | id       | int(11)     | NO   | PRI | NULL    | auto_increment |
-- | userName | varchar(45) | NO   |     | NULL    |                |
-- | password | varchar(94) | NO   |     | NULL    |                |
-- | alias    | varchar(45) | NO   |     | NULL    |                |
-- +----------+-------------+------+-----+---------+----------------+

DROP TABLE IF EXISTS User;
CREATE TABLE IF NOT EXISTS User (
	`id` INT NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(45) NOT NULL,
	`password` VARCHAR(94) NOT NULL,
	`alias` VARCHAR(45) NOT NULL,
	`clearance` INT NOT NULL,
	PRIMARY KEY (`id`)
);
-- Create table Cart
-- +-----------+------------+------+-----+---------+-------+
-- | Field     | Type       | Null | Key | Default | Extra |
-- +-----------+------------+------+-----+---------+-------+
-- | userId    | int(11)    | NO   | PRI | NULL    |       |
-- | productId | varchar(6) | NO   | PRI | NULL    |       |
-- +-----------+------------+------+-----+---------+-------+

DROP TABLE IF EXISTS Cart;
CREATE TABLE IF NOT EXISTS Cart(
	`userId` INT NOT NULL,
	`productId` VARCHAR(6) NOT NULL,
	PRIMARY KEY (`userId`, `productId`),
	FOREIGN KEY (`userId`)
    REFERENCES `User` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
    FOREIGN KEY (`productId`)
    REFERENCES `Products` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
);

-- Create table Review
-- +-----------+-------------+------+-----+---------+-------+
-- | Field     | Type        | Null | Key | Default | Extra |
-- +-----------+-------------+------+-----+---------+-------+
-- | userId    | int(11)     | NO   | PRI | NULL    |       |
-- | productId | varchar(45) | NO   | PRI | NULL    |       |
-- | rating    | int(11)     | YES  |     | NULL    |       |
-- +-----------+-------------+------+-----+---------+-------+

DROP TABLE IF EXISTS Review;
CREATE TABLE IF NOT EXISTS Review (
	`userId` INT NOT NULL,
	`productId` VARCHAR(45) NOT NULL,
	`rating` INT NULL,
	PRIMARY KEY (`userId`, `productId`),
	FOREIGN KEY (`userId`)
    REFERENCES `musikdong`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
    FOREIGN KEY (`productId`)
    REFERENCES `musikdong`.`Products` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
);

-- Create table Orders
-- +-----------+------------+------+-----+---------+----------------+
-- | Field     | Type       | Null | Key | Default | Extra          |
-- +-----------+------------+------+-----+---------+----------------+
-- | id        | int(11)    | NO   | PRI | NULL    | auto_increment |
-- | userId    | int(11)    | NO   | MUL | NULL    |                |
-- | orderdate | date       | YES  |     | NULL    |                |
-- | payed     | tinyint(1) | YES  |     | NULL    |                |
-- | processed | tinyint(1) | YES  |     | NULL    |                |
-- +-----------+------------+------+-----+---------+----------------+

DROP TABLE IF EXISTS Orders;
CREATE TABLE IF NOT EXISTS Orders (
	`id` INT NOT NULL AUTO_INCREMENT,
	`userId` INT NOT NULL,
	`orderdate` DATE,
	`payed` BOOLEAN,
	`processed` BOOLEAN,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`userId`)
    REFERENCES `musikdong`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
);

-- Create table Orderitems
-- +-----------+------------+------+-----+---------+-------+
-- | Field     | Type       | Null | Key | Default | Extra |
-- +-----------+------------+------+-----+---------+-------+
-- | orderId   | int(11)    | NO   | PRI | NULL    |       |
-- | productId | varchar(6) | NO   | PRI | NULL    |       |
-- | amount    | int(11)    | YES  |     | NULL    |       |
-- +-----------+------------+------+-----+---------+-------+
DROP TABLE IF EXISTS Orderitems;
CREATE TABLE IF NOT EXISTS Orderitems(
	`orderId` INT NOT NULL,
	`productId` VARCHAR(6) NOT NULL,
	`amount` INT,
	PRIMARY KEY (`orderId`, `productId`),
	FOREIGN KEY (`orderId`)
    REFERENCES `Orders` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
    FOREIGN KEY (`productId`)
    REFERENCES `Products` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
);

-- Turn on security checks
SET FOREIGN_KEY_CHECKS=1;


-- Create some test-data

-- Categorys
INSERT INTO Category (name) VALUES (
	'Overdrive'
);
INSERT INTO Category (name) VALUES (
	'Distortion'
);
INSERT INTO Category (name) VALUES (
	'Sexual Favor'
);
INSERT INTO Category (name) VALUES (
	'Compressor'
);


-- Products
INSERT INTO Products (id, name, price, description, imageUrl, category) VALUES (
	'043821',
	'Guma Drive',
	450.0,
	'An overdrive for bass. Gimme some more of that bass daddy',
	'None',
	'Overdrive'
);
INSERT INTO Products (id, name, price, description, imageUrl, category) VALUES (
	'018183',
	'Comp ma Swamp',
	200.0,
	'Some body once told me the world is gonna roll me, I ain\'t the sharpest tool i the shed',
	'None',
	'Compressor'
);
INSERT INTO Products (id, name, price, description, imageUrl, category) VALUES (
	'183719',
	'Josefs Oskuld',
	-40.0,
	'Jag är desperat asså!',
	'None',
	'Sexual Favor'
);
INSERT INTO Products (id, name, price, description, imageUrl, category) VALUES (
	'019302',
	'Magical powder',
	100.0,
	'Not drugs...I promise',
	'None',
	'Sexual Favor'
);



-- TagTypes
INSERT INTO TagTypes (name) VALUES (
	'Overdrive'
);
INSERT INTO TagTypes (name) VALUES (
	'Distortion'
);
INSERT INTO TagTypes (name) VALUES (
	'Sexual Favor'
);
INSERT INTO TagTypes (name) VALUES (
	'Compressor'
);
INSERT INTO TagTypes (name) VALUES (
	'Stomp'
);
INSERT INTO TagTypes (name) VALUES (
	'Drive'
);
INSERT INTO TagTypes (name) VALUES (
	'Drugs'
);
INSERT INTO TagTypes (name) VALUES (
	'Telejack'
);



-- Tags
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'043821',
	'Distortion'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'043821',
	'Overdrive'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'043821',
	'Drive'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'018183',
	'Compressor'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'018183',
	'Stomp'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'018183',
	'Drugs'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'183719',
	'Sexual Favor'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'019302',
	'Drugs'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'019302',
	'Overdrive'
);
INSERT INTO Tag (productId, tagTypeName) VALUES (
	'019302',
	'Sexual Favor'
);



-- Users
INSERT INTO User (id, userName, password, alias, clearance) VALUES (
	NULL,
	'admin',
	'pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73',
	'Admin',
	0
);
INSERT INTO User (id, userName, password, alias, clearance) VALUES (
	NULL,
	'Josef_U',
	'pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73',
	'Josef',
	1
);
INSERT INTO User (id, userName, password, alias, clearance) VALUES (
	NULL,
	'FuckMaster69',
	'pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73',
	'Leo',
	2
);
INSERT INTO User (id, userName, password, alias, clearance) VALUES (
	NULL,
	'JizzWizzard420',
	'pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73',
	'Jens',
	2
);
INSERT INTO User (id, userName, password, alias, clearance) VALUES (
	NULL,
	'LadyBeard',
	'pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73',
	'Tom',
	2
);


--Cart
INSERT INTO Cart (userId, productId) VALUES (
	'1',
	'043821'
);
INSERT INTO Cart (userId, productId) VALUES (
	1,
	'183719'
);
INSERT INTO Cart (userId, productId) VALUES (
	1,
	'019302'
);
INSERT INTO Cart (userId, productId) VALUES (
	2,
	'019302'
);
INSERT INTO Cart (userId, productId) VALUES (
	2,
	'183719'
);
INSERT INTO Cart (userId, productId) VALUES (
	3,
	'043821'
);
INSERT INTO Cart (userId, productId) VALUES (
	4,
	'018183'
);


-- Review
INSERT INTO Review (userId, productId, rating) VALUES (
	1,
	'043821',
	4
);
INSERT INTO Review (userId, productId, rating) VALUES (
	1,
	'183719',
	2
);
INSERT INTO Review (userId, productId, rating) VALUES (
	2,
	'019302',
	5
);
INSERT INTO Review (userId, productId, rating) VALUES (
	3,
	'183719',
	5
);

-- Order
INSERT INTO Orders (id, userId, orderdate, payed, processed) VALUES(
	NULL,
	2,
	'2019-11-29',
	0,
	0
);
INSERT INTO Orders (id, userId, orderdate, payed, processed) VALUES(
	NULL,
	3,
	'2019-11-25',
	1,
	0
);

-- Orderitems
INSERT INTO Orderitems (orderId, productId, amount) VALUES(
	1,
	'043821',
	1
);
INSERT INTO Orderitems (orderId, productId, amount) VALUES(
	1,
	'183719',
	1
);
INSERT INTO Orderitems (orderId, productId, amount) VALUES(
	1,
	'018183',
	1
);
INSERT INTO Orderitems (orderId, productId, amount) VALUES(
	2,
	'043821',
	1
);
INSERT INTO Orderitems (orderId, productId, amount) VALUES(
	2,
	'183719',
	1
);
INSERT INTO Orderitems (orderId, productId, amount) VALUES(
	2,
	'019302',
	1
);