/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 10.4.32-MariaDB : Database - qkd
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`qkd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `qkd`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `birthday` varchar(200) DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `sender_key` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `account` */

insert  into `account`(`id`,`username`,`email`,`password`,`birthday`,`gender`,`sender_key`) values 
(1,'Test1','Test1@gmail.com','Test1@gmail.com',NULL,NULL,NULL),
(2,'Test2','Test2@gmail.com','Test2@gmail.com',NULL,NULL,NULL),
(3,'Raji','Test4@gmail.com','Test4@gmail.com','1992-11-11','female','3.pkl'),
(4,'Manoo','Manoo@gmail.com','Manoo@gmail.com','1992-11-11','female','4.pkl');

/*Table structure for table `emailnfo` */

DROP TABLE IF EXISTS `emailnfo`;

CREATE TABLE `emailnfo` (
  `id` int(67) NOT NULL AUTO_INCREMENT,
  `userid` varchar(66) DEFAULT NULL,
  `useremail` varchar(66) DEFAULT NULL,
  `toemail` varchar(66) DEFAULT NULL,
  `toname` varchar(66) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `emailnfo` */

insert  into `emailnfo`(`id`,`userid`,`useremail`,`toemail`,`toname`,`subject`,`message`,`date`) values 
(1,'1','Test1@gmail.com','Test2@gmail.com','Test2','Sample','','11/25/2024'),
(2,'3','Test4@gmail.com','Test2@gmail.com','Test2','Sample','2ciphertext.bin','11/25/2024'),
(3,'3','Test4@gmail.com','Test2@gmail.com','Test2','Sample','3ciphertext.bin','11/25/2024'),
(4,'3','Test4@gmail.com','Test4@gmail.com','Raji','checking mail','4ciphertext.bin','11/25/2024'),
(5,'3','Test4@gmail.com','Test4@gmail.com','Raji','checking mail','5ciphertext.bin','11/25/2024'),
(6,'4','Manoo@gmail.com','Test2@gmail.com','Test2','checking mail','6ciphertext.bin','12/02/2024'),
(7,'3','Test4@gmail.com','Manoo@gmail.com','Manoo','File Detaol;s','7ciphertext.bin','02/02/2025');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
