-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: mysql_shiyan
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dpt_name` char(20) NOT NULL,
  `people_num` int(10) DEFAULT '10',
  PRIMARY KEY (`dpt_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('dpt1',11),('dpt2',12),('dpt3',10),('dpt4',15);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(10) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `age` int(10) DEFAULT NULL,
  `salary` int(10) NOT NULL,
  `phone` int(12) NOT NULL,
  `in_dpt` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  KEY `emp_fk` (`in_dpt`),
  CONSTRAINT `emp_fk` FOREIGN KEY (`in_dpt`) REFERENCES `department` (`dpt_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Tom',26,2500,119119,'dpt4'),(2,'Jack',24,2500,120120,'dpt2'),(3,'Rose',22,2800,114114,'dpt3'),(4,'Jim',35,3000,100861,'dpt1'),(5,'Mary',21,3000,100101,'dpt2'),(6,'Alex',26,3000,123456,'dpt1'),(7,'Ken',27,3500,654321,'dpt1'),(8,'Rick',24,3500,987654,'dpt3'),(9,'Joe',31,3600,110129,'dpt2'),(10,'Mike',23,3400,110110,'dpt4'),(11,'Jobs',NULL,3600,19283,'dpt2'),(12,'Tony',NULL,3400,102938,'dpt3'),(13,'wmsj100',30,5000,119129,'dpt4'),(14,'wanmei',25,3000,119120,'dpt2');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `proj_num` int(10) NOT NULL,
  `proj_name` char(20) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT '2015-04-01',
  `of_dpt` char(20) DEFAULT NULL,
  PRIMARY KEY (`proj_num`,`proj_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'proj_a','2015-01-15','2015-01-31','dpt2'),(2,'proj_b','2015-01-15','2015-02-15','dpt1'),(3,'proj_c','2015-02-01','2015-03-01','dpt4'),(4,'proj_d','2015-02-15','2015-04-01','dpt3'),(5,'proj_e','2015-02-25','2015-03-01','dpt4'),(6,'proj_f','2015-02-26','2015-03-01','dpt2');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-29 16:44:45
