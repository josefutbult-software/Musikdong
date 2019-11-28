-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: musikdong
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cart` (
  `userId` int(11) NOT NULL,
  `productId` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`userId`,`productId`),
  KEY `productId` (`productId`),
  CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `Products` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart`
--

LOCK TABLES `Cart` WRITE;
/*!40000 ALTER TABLE `Cart` DISABLE KEYS */;
INSERT INTO `Cart` VALUES (1,'019302'),(1,'043821'),(1,'183719'),(2,'019302'),(2,'183719'),(3,'043821'),(4,'018183');
/*!40000 ALTER TABLE `Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Category` (
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES ('Compressor'),('Distortion'),('Overdrive'),('Sexual Favor');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Products` (
  `id` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` float DEFAULT 0,
  `description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `imageUrl` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  CONSTRAINT `Products_ibfk_1` FOREIGN KEY (`category`) REFERENCES `Category` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES ('018183','Comp ma Swamp',200,'Some body once told me the world is gonna roll me, I ain\'t the sharpest tool i the shed','None','Compressor'),('019302','Magical powder',100,'Not drugs...I promise','None','Sexual Favor'),('043821','Guma Drive',450,'An overdrive for bass. Gimme some more of that bass daddy','None','Overdrive'),('183719','Josefs Oskuld',-40,'Jag är desperat asså!','None','Sexual Favor');
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Review` (
  `userId` int(11) NOT NULL,
  `productId` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`userId`,`productId`),
  KEY `productId` (`productId`),
  CONSTRAINT `Review_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `Review_ibfk_2` FOREIGN KEY (`productId`) REFERENCES `Products` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Review`
--

LOCK TABLES `Review` WRITE;
/*!40000 ALTER TABLE `Review` DISABLE KEYS */;
INSERT INTO `Review` VALUES (1,'043821',4),(1,'183719',2),(2,'019302',5),(3,'183719',5);
/*!40000 ALTER TABLE `Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tag`
--

DROP TABLE IF EXISTS `Tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tag` (
  `productId` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tagTypeName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`productId`,`tagTypeName`),
  KEY `tagTypeName` (`tagTypeName`),
  CONSTRAINT `Tag_ibfk_1` FOREIGN KEY (`productId`) REFERENCES `Products` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `Tag_ibfk_2` FOREIGN KEY (`tagTypeName`) REFERENCES `TagTypes` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tag`
--

LOCK TABLES `Tag` WRITE;
/*!40000 ALTER TABLE `Tag` DISABLE KEYS */;
INSERT INTO `Tag` VALUES ('018183','Compressor'),('018183','Drugs'),('018183','Stomp'),('019302','Drugs'),('019302','Overdrive'),('019302','Sexual Favor'),('043821','Distortion'),('043821','Drive'),('043821','Overdrive'),('183719','Sexual Favor');
/*!40000 ALTER TABLE `Tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TagTypes`
--

DROP TABLE IF EXISTS `TagTypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TagTypes` (
  `name` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TagTypes`
--

LOCK TABLES `TagTypes` WRITE;
/*!40000 ALTER TABLE `TagTypes` DISABLE KEYS */;
INSERT INTO `TagTypes` VALUES ('Compressor'),('Distortion'),('Drive'),('Drugs'),('Overdrive'),('Sexual Favor'),('Stomp'),('Telejack');
/*!40000 ALTER TABLE `TagTypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(94) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alias` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `clearance` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'admin','pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73','Admin',0),(2,'Josef_U','pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73','Josef',1),(3,'FuckMaster69','pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73','Leo',2),(4,'JizzWizzard420','pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73','Jens',2),(5,'LadyBeard','pbkdf2:sha256:150000$IkTnIhuh$387dfe8fd61978dd55016cfebf20abd9f4b3c5b4578c4f4a84db9c2249e98e73','Tom',2);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-28 17:13:55
