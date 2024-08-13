-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: logsdb
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Role`
--

DROP TABLE IF EXISTS `Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Role`
--

LOCK TABLES `Role` WRITE;
/*!40000 ALTER TABLE `Role` DISABLE KEYS */;
INSERT INTO `Role` VALUES (1,'ROLE_USER','2024-01-12 05:22:13','2024-01-12 05:22:13');
/*!40000 ALTER TABLE `Role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'abhijsh61@gmail.com','$2b$10$OpNJ31ydlPrlRi3a7yO9KObQG2UXiTp8iHtZQjy8Br2tX3onFnU1S','abhishek','2024-01-12 05:22:13','2024-01-12 05:22:13'),(2,'omkartestUser@vm2.com','$2b$10$PMQPhAkOyYbad32MFEjybuOIEPkB7FiwQPksjtm87DNPE5o0hyLMy','omkartestvm2','2024-01-16 09:15:22','2024-01-16 09:15:22'),(3,'omkartestone@gmail.com','$2b$10$CNANl0I57O9tw8e6h6sjoe29m3zzgJIMUW9MAknxQfMDOUP9ClYDW','omkartestone','2024-08-08 05:42:49','2024-08-08 05:42:49'),(4,'test2@gmail.com','$2b$10$zbRPdutOYCABwzY2RNwJ7eV2ksHD10UUxS//saoFpJViAmqurawp2','test2','2024-08-08 05:45:25','2024-08-08 05:45:25'),(5,'test3@gmail.com','$2b$10$e2sa6zuczqxT7cCJBHww2eBSIJ2w1JC4T1xZzQs14xoGuXPVg0eQ2','test3','2024-08-08 05:46:26','2024-08-08 05:46:26');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserRole`
--

DROP TABLE IF EXISTS `UserRole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserRole` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `roleId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_UserRole_User_idx` (`userId`),
  KEY `fk_UserRole_Role_idx` (`roleId`),
  CONSTRAINT `UserRole_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `User` (`idUser`),
  CONSTRAINT `UserRole_ibfk_2` FOREIGN KEY (`roleId`) REFERENCES `Role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserRole`
--

LOCK TABLES `UserRole` WRITE;
/*!40000 ALTER TABLE `UserRole` DISABLE KEYS */;
INSERT INTO `UserRole` VALUES (1,1,1,'2024-01-12 05:22:13','2024-01-12 05:22:13'),(2,2,1,'2024-01-16 09:15:22','2024-01-16 09:15:22'),(3,3,1,'2024-08-08 05:42:49','2024-08-08 05:42:49'),(4,4,1,'2024-08-08 05:45:25','2024-08-08 05:45:25'),(5,5,1,'2024-08-08 05:46:26','2024-08-08 05:46:26');
/*!40000 ALTER TABLE `UserRole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_information`
--

DROP TABLE IF EXISTS `contact_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identifier` varchar(200) DEFAULT NULL,
  `contact_page_content` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_information`
--

LOCK TABLES `contact_information` WRITE;
/*!40000 ALTER TABLE `contact_information` DISABLE KEYS */;
INSERT INTO `contact_information` VALUES (1,'iwakura-op','h2. 連絡先\r\n\r\nh3. 岩倉ネジ製作所 連絡先 \r\n\r\nh4. 平日日中 (09:00～18:00)\r\n\r\n* 岩倉ネジ製作所\r\n|_.氏名	|_.氏名読み	|_.電話番号	|_.メールアドレス	|\r\n|○○ ○○	|○○ ○○	|0000-00-0000	|xxxx@xxx.xxx|	\r\n|▲▲ ▲▲	|▲▲ ▲▲	|0000-00-0000	|yyyy@xxx.xxx|\r\n\r\nh4. 夜間・休日\r\n\r\n# お客様の判断を仰ぐ規模の障害発生時にはオフィスへの電話を試みる\r\n# 電話での連絡ができない場合は、チケットでご報告\r\n\r\n----\r\n\r\n* チケットメール送信先\r\naaaa@xxxx.xxx, bbbb@xxxx.xxx, cccc@xxxx.xxx\r\n\r\n* 障害検知時のアラートメール送信先\r\ndddd@xxxx.xxx, eeee@xxxx.xxx, ffff@xxxx.xxx\r\n\r\n* 障害検知時の自動架電先\r\n無し。\r\n\r\n\r\nh3. 株式会社アールワークス 連絡先\r\n\r\n|_.氏名	|_.氏名読み	|_.電話番号	|_.メールアドレス	|_.部署	|\r\n|通常連絡窓口（平日日中）	||00-0000-0000	|xxxx@xxxx.xxx	|システムソリューション部|\r\n|障害対応窓口（24時間365日）	||00-0000-0000	|xxxx@xxxx.xxx （※）	|システムソリューション部|\r\n\r\n※ 運用ポータルサイトより「障害対応」でチケットを起票いただいても、緊急連絡扱いとなります。\r\n\r\n\r\n\r\n'),(2,'naniwa-univ-op','h2. 連絡先\r\n\r\nh3. 浪速大学 連絡先 \r\n\r\nh4. prod_univ サーバ、 https://www.xxxxx.ac.jp/univ/\r\n\r\n|_.氏名 |_.氏名読み |_.電話番号  |_.メールアドレス        |_. 備考|\r\n|○○ ○○|○○ ○○ |06-0000-0000|xxxx@xxxx.ac.jp        ||\r\n\r\nh4. その他\r\n\r\n|_.氏名 |_.氏名読み |_.電話番号  |_.メールアドレス        |_. 備考|\r\n|▲▲ ▲▲|▲▲ ▲▲|06-0000-0000|yyyy@xxxx.ac.jp         |レベル1緊急連絡先も同じ|\r\n\r\n* チケットメール送信先\r\nxxxx@xxxx.ac.jp\r\nyyyy@xxxx.ac.jp\r\nzzzz@xxxx.ac.jp\r\n\r\n\r\nh3. 株式会社アールワークス 連絡先\r\n\r\n|_.氏名	|_.氏名読み	|_.電話番号	|_.メールアドレス	|_.部署	|\r\n|通常連絡窓口（平日日中）	||00-0000-0000	|xxxx@rworks.jp	|システムソリューション部|\r\n|障害対応窓口（24時間365日）	||00-0000-0000	|xxxx@monitor.rworks-ms.jp （※）	|システムソリューション部|\r\n\r\n※ 運用ポータルサイトより「障害対応」でチケットを起票いただいても、緊急連絡扱いとなります。\r\n\r\n\r\n'),(3,'mineya-shuzou-op','h2. 連絡先\r\n\r\nh3. ABC社様 連絡先\r\n\r\n営業時間内(平日:9:00 - 17:00)\r\n|_.氏名		|_.氏名読み	|_.電話番号		|_.メールアドレス	|_.部署	 |\r\n|○○ ○○	|○○ ○○	|/3. 000-000-0000	|XXXXXX@xxxx.xxx	|技術部  |\r\n|▲▲ ▲▲	|▲▲ ▲▲	|			YYYYYY@xxxx.xxx	|技術部  |\r\n|◇◇ ◇◇	|◇◇ ◇◇	|			ZZZZZZ@xxxx.xxx	|営業部  |\r\n\r\n営業時間外(休日夜間)\r\n|_.氏名		|_.氏名読み	|_.電話番号		|_.メールアドレス	|_.部署	 |\r\n|○○ ○○	|○○ ○○	|/3. 000-000-0000	|XXXXXX@xxxx.xxx	|技術部  |\r\n|▲▲ ▲▲	|▲▲ ▲▲	|			YYYYYY@xxxx.xxx	|技術部  |\r\n|◇◇ ◇◇	|◇◇ ◇◇	|			ZZZZZZ@xxxx.xxx	|営業部  |\r\n\r\n\r\nh3. 峰屋酒造様 連絡先\r\n\r\n|_.氏名		|_.氏名読み	|_.電話番号	|_.メールアドレス	|_.FAX		|\r\n|○○ ○○	|○○ ○○	| 000-000-0000	|XXXXXX@xxxx.xxx	|000-000-0000	|\r\n\r\n\r\n\r\nh3. 株式会社アールワークス 連絡先\r\n\r\n|_.氏名	|_.電話番号	|_.メールアドレス	|_.部署	|\r\n|通常連絡窓口（平日日中）|00-0000-0000	|xxxx@rworks.jp	|システムソリューション部|\r\n|障害対応窓口（24時間365日）|00-0000-0000	|xxxx@monitor.rworks-ms.jp （※）	|システムソリューション部|\r\n\r\n※ 運用ポータルサイトより「障害対応」でチケットを起票いただいても、緊急連絡扱いとなります。\r\n'),(4,'kitasanriku-sodegahama-gyokyo-op','h3. 顧客緊急連絡先\r\n\r\n\r\n\r\nh3. 架電の順番（北三陸担当表）\r\n\r\ndocument#2 にて最新の「北三陸緊急連絡先_YYYYMMDD.xlsx」を参照し、\r\n該当する期間の架電順に従い連絡してください。\r\n3 周して誰も電話に出なければ、その旨を記載の上、チケットで報告してください。\r\n\r\n\r\n\r\n\r\nh3. Rworks 連絡先\r\n\r\n|_. 連絡先 |_. 電話番号   |_. 受付時間|\r\n| 障害に関するお問い合わせ (緊急窓口)| 000-0000-0000 | 24時間365日|\r\n| その他のお問い合わせ  (オフィス) | 00-0000-0000 | 弊社営業日 9:00 ~ 18:00|\r\n\r\n\r\n本ポータルサイトのチケットを更新すると、指定されたメールアドレスに通知されます。\r\n原則として弊社へのメール連絡はチケット経由でお願いいたします。\r\n\r\n'),(5,'kitasanriku-common-op','h3. 架電の順番（北三陸担当表）\r\n\r\ndocument#2 にて最新の「北三陸緊急連絡先_YYYYMMDD.xlsx」を参照し、\r\n該当する期間の架電順に従い連絡してください。\r\n3 周して誰も電話に出なければ、その旨を記載の上、チケットで報告してください。\r\n\r\n'),(6,'kitasanriku-railway-op','h2. 連絡先\r\n\r\nh3. 北三陸鉄道 連絡先\r\n\r\nh4. 電話連絡先\r\n\r\nh3. 架電の順番（北三陸担当表）\r\n\r\ndocument#2 にて最新の「北三陸緊急連絡先_YYYYMMDD.xlsx」を参照し、\r\n該当する期間の架電順に従い連絡してください。\r\n3 周して誰も電話に出なければ、その旨を記載の上、チケットで報告してください。\r\n\r\n\r\n\r\nh4. チケットメール送信先\r\n\r\nXXXXXX@XXXX.XXX, YYYYYY@XXXX.XXX, ZZZZZZ@XXXX.XXX\r\n\r\nh4. アラートメール送信先\r\n\r\nXXXXXX@XXXX.XXX\r\n\r\n{{cut_start(2000/0/0 #00000 でいただいた情報)}}\r\n<pre>\r\n★ML-北三陸鉄道システム運用（XXXXXX@XXXX.XXX)\r\n　○○ ○○さん（YYYYYY@XXXX.XXX）\r\n　△△ △△さん（ZZZZZZ@XXXX.XXX)\r\n</pre>\r\n{{cut_end}}\r\n\r\n\r\nh3. 株式会社アールワークス 連絡先\r\n\r\n|_.氏名	|_.氏名読み	|_.電話番号	|_.メールアドレス	|_.部署	|\r\n|通常連絡窓口（平日日中）	||00-0000-0000	|XXXXXX@rworks.jp	|システムソリューション部|\r\n|障害対応窓口（24時間365日）	||000-0000-0000	|XXXXXX@monitor.rworks-ms.jp （※）	|システムソリューション部|\r\n\r\n※ 運用ポータルサイトより「障害対応」でチケットを起票いただいても、緊急連絡扱いとなります。\r\n\r\n\r\n'),(7,'jittoku-nagaya-op','h1. 緊急連絡先\r\n\r\n変更の際はEmergencyCallを編集してください。 \r\n\r\nh1. EmergencyCall\r\n\r\n{{cut_start(平日 9:00～18:00)}}\r\n\r\n|_.#|_. 部署       |_. お名前                     |_. 電話番号    |_. メール|_. 備考|\r\n|>.1|/3. 情報システム部|○○ ○○(あああ あああ)    |/2.00-0000-0000|         |       |\r\n|>.2|               △△ △△(いいい いいい)\r\n                    ◇◇ ◇◇(ううう ううう)\r\n                    ●● ●●(えええ えええ)                |         |       |\r\n|>.3|               ○○ ○○(あああ あああ)    |000-0000-0000  |         |電話に出てもらえない場合、留守電にメッセージを残してください|\r\n\r\n{{cut_end}}\r\n\r\n{{cut_start(夜間・休日)}}\r\n\r\n|_. 部署                                |_. お名前                |_. 電話番号|_. メール|_. 備考|\r\n|なし|○○ ○○(あああ あああ)|000-0000-0000|メール通知|電話に出てもらえない場合、留守電にメッセージを残してください|\r\n\r\n{{cut_end}}\r\n\r\nh3. 株式会社アールワークス 連絡先\r\n\r\nh4. 緊急連絡先\r\n\r\n|_.氏名|_.メールアドレス|_.電話番号|\r\n|24時間365日障害対応窓口|XXXXXX@monitor.rworks-ms.jp\r\n（なるべく運用ポータルサイトのチケット発行／更新にてご連絡いただければと存じます。）|000-0000-0000|\r\n\r\nh4. 平常時の連絡先\r\n\r\n|_.氏名|_.メールアドレス|_.電話番号|\r\n|通常受付窓口|XXXXXX@rworks.jp\r\n（なるべく運用ポータルサイトのチケット発行／更新にてご連絡いただければと存じます。）|00-0000-0000|\r\n\r\n'),(8,'jittoku-nagaya-inner','h1. EmergencyCall\r\n\r\n{{cut_start(平日 9:00～18:00)}}\r\n\r\n|_.#|_. 部署       |_. お名前                     |_. 電話番号    |_. メール|_. 備考|\r\n|>.1|/3. 情報システム部|○○ ○○(あああ あああ)    |/2.00-0000-0000|         |       |\r\n|>.2|               △△ △△(いいい いいい)\r\n                    ◇◇ ◇◇(ううう ううう)\r\n                    ●● ●●(えええ えええ)                |         |       |\r\n|>.3|               ○○ ○○(あああ あああ)    |000-0000-0000  |         |電話に出てもらえない場合、留守電にメッセージを残してください|\r\n\r\n{{cut_end}}\r\n\r\n{{cut_start(夜間・休日)}}\r\n\r\n|_. 部署                                |_. お名前                |_. 電話番号|_. メール|_. 備考|\r\n|なし|○○ ○○(あああ あああ)|000-0000-0000|メール通知|電話に出てもらえない場合、留守電にメッセージを残してください|\r\n\r\n{{cut_end}}\r\n\r\nh3. 株式会社アールワークス 連絡先\r\n\r\nh4. 緊急連絡先\r\n\r\n|_.氏名|_.メールアドレス|_.電話番号|\r\n|24時間365日障害対応窓口|XXXXXX@monitor.rworks-ms.jp\r\n（なるべく運用ポータルサイトのチケット発行／更新にてご連絡いただければと存じます。）|000-0000-0000|\r\n\r\nh4. 平常時の連絡先\r\n\r\n|_.氏名|_.メールアドレス|_.電話番号|\r\n|通常受付窓口|XXXXXX@rworks.jp\r\n（なるべく運用ポータルサイトのチケット発行／更新にてご連絡いただければと存じます。）|00-0000-0000|\r\n'),(9,'honekawa-op','h3. 顧客緊急連絡先\r\n\r\n|_.#|_.氏名|_.電話番号|_.備考|\r\n|>.1|○○ ○○ (あああ あああ)|=.000-0000-0000||\r\n|>.2|▲▲ ▲▲ (いいい いいい |=.000-0000-0000||\r\n|>.3|◇◇ ◇◇ (ううう ううう)|=.000-0000-0000||\r\n|>.4|●● ●● (えええ えええ)|=.000-0000-0000||\r\n|>.5|△△ △△ (おおお おおお)|=.000-0000-0000||\r\n\r\n\r\nh3. Rworks 連絡先\r\n\r\n|_. 連絡先 |_. 電話番号   |_. 受付時間|\r\n| 障害に関するお問い合わせ (緊急窓口)| 000-0000-0000 |  24時間365日 |\r\n| その他のお問い合わせ  (オフィス) | 00-0000-0000 | 弊社営業日 9:00 ~ 18:00|\r\n\r\n\r\n本ポータルサイトのチケットを更新すると、指定されたメールアドレスに通知されます。\r\n原則として弊社へのメール連絡はチケット経由でお願いいたします。'),(10,'sekimachi-op','h3. 顧客緊急連絡先\r\n\r\n| 順位 | 氏名 | よみ(敬称略) | 電話番号 | 備考 |\r\n| 1 | ○○ ○○ 様 | ○○ ○○ | 000-0000-0000 | |\r\n| 2 | △△ △△ 様 | △△ △△ | 111-111-1111 | 平日9:00～18:00のみ連絡可 ​|\r\n| 3 | ◇◇ ◇◇ 様 | ◇◇ ◇◇ | 222-2222-2222 | |\r\n\r\nh3. Rworks 連絡先\r\n\r\n|_. 連絡先 |_. 電話番号   |_. 受付時間|\r\n| 障害に関するお問い合わせ (緊急窓口)| 000-0000-0000 | 24時間365日|\r\n| その他のお問い合わせ  (オフィス) | 00-0000-0000 | 弊社営業日 9:00 ~ 18:00|\r\n\r\n\r\n本ポータルサイトのチケットを更新すると、指定されたメールアドレスに通知されます。\r\n原則として弊社へのメール連絡はチケット経由でお願いいたします。'),(11,'manpyo-op','h3. 万俵商事 様 緊急連絡先\r\n\r\n{{warning\r\n*障害連絡で顧客へ電話連絡した際は、チケットに「万俵商事様要対応」カテゴリを設定してください*\r\n}}\r\n\r\n|_.お名前                    |_.電話番号  |_. 備考|\r\n|○○ ○○|000-0000-0000||\r\n|△△ △△|111-1111-1111||\r\n\r\nh4. 障害/静観チケットメール通知先\r\n\r\nadmin@xxxx.xxx\r\nalert@yyyy.yyy（「万俵商事様要対応」カテゴリ設定時）\r\n\r\nh4. アラートメール自動通知先\r\n\r\nalert@zzzz.zzz\r\n\r\nh3. Rworks 連絡先\r\n\r\n|_. 連絡先 |_. 電話番号   |_. 受付時間|\r\n| 障害に関するお問い合わせ (緊急窓口)| 000-0000-0000 | 24時間365日|\r\n| その他のお問い合わせ  (オフィス) | 00-0000-0000 | 弊社営業日 9:00 ~ 18:00|\r\n\r\n\r\n本ポータルサイトのチケットを更新すると、指定されたメールアドレスに通知されます。\r\n原則として弊社へのメール連絡はチケット経由でお願いいたします。\r\n');
/*!40000 ALTER TABLE `contact_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `correct_sop`
--

DROP TABLE IF EXISTS `correct_sop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `correct_sop` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mod_state_agent_id` int NOT NULL,
  `page_number` int DEFAULT NULL,
  `prepared_query` varchar(200) DEFAULT NULL,
  `generated_sop` varchar(200) DEFAULT NULL,
  `correct_sop` varchar(200) DEFAULT NULL,
  `sop_type` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mod_state_agent_id` (`mod_state_agent_id`),
  CONSTRAINT `correct_sop_ibfk_1` FOREIGN KEY (`mod_state_agent_id`) REFERENCES `master_module_state_agent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=309 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `correct_sop`
--

LOCK TABLES `correct_sop` WRITE;
/*!40000 ALTER TABLE `correct_sop` DISABLE KEYS */;
/*!40000 ALTER TABLE `correct_sop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generated_sop_feedback`
--

DROP TABLE IF EXISTS `generated_sop_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generated_sop_feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `msa_id` int NOT NULL,
  `generated_sop` longtext,
  `customer_specific_sop` longtext,
  `modified_sop` longtext,
  `comments` longtext,
  PRIMARY KEY (`id`),
  KEY `msa_id` (`msa_id`),
  CONSTRAINT `generated_sop_feedback_ibfk_1` FOREIGN KEY (`msa_id`) REFERENCES `master_module_state_agent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generated_sop_feedback`
--

LOCK TABLES `generated_sop_feedback` WRITE;
/*!40000 ALTER TABLE `generated_sop_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `generated_sop_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_module_state_agent`
--

DROP TABLE IF EXISTS `master_module_state_agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_module_state_agent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `module` varchar(200) DEFAULT NULL,
  `state` varchar(200) DEFAULT NULL,
  `agent` varchar(200) DEFAULT NULL,
  `project` varchar(200) DEFAULT NULL,
  `user_email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_module_state_agent`
--

LOCK TABLES `master_module_state_agent` WRITE;
/*!40000 ALTER TABLE `master_module_state_agent` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_module_state_agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_project_type`
--

DROP TABLE IF EXISTS `master_project_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_project_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identifier` varchar(200) DEFAULT NULL,
  `type` varchar(200) DEFAULT NULL,
  `module` varchar(200) DEFAULT NULL,
  `state` varchar(200) DEFAULT NULL,
  `agent` varchar(200) DEFAULT NULL,
  `sop_column` varchar(200) DEFAULT NULL,
  `sop_delimeter` varchar(200) DEFAULT NULL,
  `special_case1` varchar(200) DEFAULT NULL,
  `level` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_project_type`
--

LOCK TABLES `master_project_type` WRITE;
/*!40000 ALTER TABLE `master_project_type` DISABLE KEYS */;
INSERT INTO `master_project_type` VALUES (49,'iwakura-op','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(50,'ohata-print-op','ohata type','','障害箇所','','障害対応手順',':(.*?)]','',NULL),(51,'naniwa-univ-op','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(52,'naniwa-univ-inner','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(53,'mineya-shuzou-op','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(54,'mineya-shuzou-inner','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(55,'kitasanriku-inner','','','','','','','',NULL),(56,'kitasanriku-kankokyokai-op','','','','','','','',NULL),(57,'kitasanriku-sodegahama-gyokyo-op','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','&ltDISK&gt_*使用率','対応レベル'),(58,'kitasanriku-railway-op','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(59,'jittoku-nagaya-inner','jittoku type','モジュール名','状態','エージェント','状態','\\[\\[(.*?):','','対応レベル'),(60,'jittoku-nagaya-op','jittoku type','モジュール名','状態','エージェント','状態','\\[\\[(.*?):','','対応レベル'),(61,'honekawa-op','honekawa op type','監視項目','','対象エージェント','障害対応手順',':(.*?)]','',NULL),(62,'honekawa-gouda-op','honekawa gouda type','監視項目','','','対応手順テンプレート','\\[\\[(.*?)\\]\\]','',NULL),(63,'sekimachi-op','sekimachi type','監視項目','','','対応手順','\\[\\[(.*?)\\]\\]','','対応レベル'),(64,'manpyo-op','manpyo type','監視項目','','対象サーバ','障害対応手順',':(.*?)]','',NULL),(65,'acron-layout-op','naniwa type','モジュール','状態','エージェント','対応手順',':(.*?)]','','対応レベル'),(66,'ladderpencil-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(67,'diningmanner-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(68,'nerimarubber-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(69,'diningmanner-www-trouble-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(70,'diningmanner-temple-trouble-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','History_データ転送_*_ログ','対応レベル'),(71,'diningmanner-lan-trouble-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(72,'diningmanner-galaxy-trouble-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(73,'diningmanner-datalake-trouble-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(74,'kaifuku-tp-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(75,'kaifuku-bcg-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(76,'kaifuku-map-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(77,'kaifuku-lab-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(78,'kaifuku-uv-op','ladderpencil type','監視項目','状態','エージェント','監視項目',':(.*?)]','','対応レベル'),(79,'sjourneytoy-op','manpyo type','監視項目','','対象サーバ','障害対応手順',':(.*?)]','',NULL),(80,'sjournyetoy-patent-scan-op','manpyo type','監視項目','','対象サーバ','障害対応手順',':(.*?)]','',NULL);
/*!40000 ALTER TABLE `master_project_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postprocess_pattern`
--

DROP TABLE IF EXISTS `postprocess_pattern`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postprocess_pattern` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pattern` varchar(500) NOT NULL,
  `replacement` varchar(500) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postprocess_pattern`
--

LOCK TABLES `postprocess_pattern` WRITE;
/*!40000 ALTER TABLE `postprocess_pattern` DISABLE KEYS */;
INSERT INTO `postprocess_pattern` VALUES (42,'次のコマンドを実行します(.*?)(?:。。。|。。|$)','\\n次のコマンドを実行します\\n<pre class=\'border p-2\'>\\1</pre>','Pre Tags'),(50,'(警告:.*?)(?:\\n\\n|$)','<div class=\'alert alert-danger\'>\\1</div>','Warning'),(51,'(注記:.*?)(?:\\n\\n|$)','<div class=\'alert alert-primary\'>\\1</div>','Note'),(52,'(重要:.*?)(?:\\n\\n|$)','<div class=\'alert alert-warning\'>\\1</div>','Important'),(53,'h([1-6])\\.\\s*(.*)','<h\\1>\\2</h\\1>','Header');
/*!40000 ALTER TABLE `postprocess_pattern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `severity_level_data`
--

DROP TABLE IF EXISTS `severity_level_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `severity_level_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identifier` varchar(200) DEFAULT NULL,
  `troubleshoot_level` longtext,
  `troubleshoot_flow` longtext,
  `troubleshoot_descripton` longtext,
  `level_content` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1374 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `severity_level_data`
--

LOCK TABLES `severity_level_data` WRITE;
/*!40000 ALTER TABLE `severity_level_data` DISABLE KEYS */;
INSERT INTO `severity_level_data` VALUES (1326,'iwakura-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。','h2. [[iwakura-op:レベル1]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル1は、重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n\r\n障害対応レベル1の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へ電話やチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n\r\n{{include(iwakura-op:連絡先)}}'),(1327,'iwakura-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。','h2. [[iwakura-op:レベル2]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル2は、復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケースです。\r\n\r\n障害対応レベル2の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。'),(1328,'iwakura-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。','h2. [[iwakura-op:レベル3]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル3は、障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケースです。\r\n\r\n障害対応レベル3の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n障害検知した内容が監視システムから自動メール通知されます。\r\nアールワークスの担当者が実施する障害報告・復旧作業はありません。'),(1329,'naniwa-univ-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。','h2. [[naniwa-univ-op:レベル1]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル1は、重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n\r\n障害対応レベル1の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へ電話やチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n\r\n{{include(naniwa-univ-op:連絡先)}}\r\n'),(1330,'naniwa-univ-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。','h2. [[naniwa-univ-op:レベル2]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル2は、復旧について貴校との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケースです。\r\n\r\n障害対応レベル2の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n'),(1331,'mineya-shuzou-op','レベル1','サービス影響があり、弊社のみで対応不可な障害','貴社に電話+チケット、峰屋酒造様にチケット(メール)でご連絡','h2. [[mineya-shuzou-op:レベル1]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル1は、重要なサービスが停止した場合等、電話にてABC社様へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n*また、障害報告は峰屋酒造様への報告も必要です。*\r\n\r\n{{include(障害対応時共通注意事項)}}\r\n\r\nh3. 連絡手順\r\n\r\n# 手早く状況を確認します。\r\n# 障害が発生中と確認できたら、峰屋酒造様にチケットにて第一報を連絡します。( \"峰屋酒造様チケット報告手順\":[[障害報告]] )\r\n# [[mineya-shuzou-op:ABC社様_連絡先]]に記載のある連絡先へ、上から順につながるまで電話にて障害報告を行います。\r\n# ABC社様へ復旧対応をお願いした場合は、 \"こちら\": #1 を基に、復旧対応依頼チケットを起票します。\r\n(以降の、ABC社様とRworks間のみのやり取りは、復旧対応依頼チケットで行います)\r\n# ABC社様と連携して復旧対応を行います。\r\n\r\n{{include(mineya-shuzou-op:連絡先)}}\r\n\r\n{{include(mineya-shuzou-op:障害報告)}}'),(1332,'mineya-shuzou-op','レベル2','サービス影響があるが、弊社のみで対応可能な障害','貴社にチケット、峰屋酒造様にチケット(メール)でご連絡','h2. [[mineya-shuzou-op:レベル2]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル2は、復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケースです。\r\n\r\n障害対応レベル2の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n*また、障害報告は峰屋酒造様への報告も必要です。*\r\n\r\n{{include(障害対応時共通注意事項)}}\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# 峰屋酒造様にチケットにて第一報を連絡します。\r\n# 以後は、進捗をチケット更新することで連絡します。\r\n\r\nh2. 峰屋酒造様チケット報告手順\r\n\r\n{{include(mineya-shuzou-op:障害報告)}}'),(1333,'mineya-shuzou-op','レベル3','サービス影響がないが、早急な復旧対応が必要な障害(ディスク使用率の急上昇など)','貴社に電話+チケットでご連絡、峰屋酒造様にはご連絡しない','h2. [[mineya-shuzou-op:レベル3]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル3は、サービスに影響のないが早期対応が必要な障害が発生した場合等、電話にてABC様へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n*峰屋酒造様への障害報告は不要です。*\r\n\r\n{{include(障害対応時共通注意事項)}}\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# 障害が発生中と確認できたら、チケットにて第一報を連絡します。\r\n# [[mineya-shuzou-op:ABC社様_連絡先]]に記載のある連絡先へ、上から順につながるまで電話にて障害報告を行います。\r\n# ABC様と連携して復旧対応を行います。\r\n\r\n\r\nh2. チケット報告手順\r\n\r\n{{include(mineya-shuzou-op:障害報告_ABC)}}\r\n\r\n'),(1334,'mineya-shuzou-op','レベル4','サービス影響はなく、弊社のみで対応可能、または早急な復旧対応が不要な障害','貴社にチケットでご連絡、峰屋酒造様にはご連絡しない','h2. [[mineya-shuzou-op:レベル4]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル4は、サービスに影響のない障害が発生した場合等、チケットのみで報告を実施するケースです。\r\n*峰屋酒造様への障害報告は不要です。*\r\n\r\n{{include(障害対応時共通注意事項)}}\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# 障害が発生中と確認できたら、チケットにて第一報を連絡します。\r\n# 復旧対応が可能であれば実施します。\r\n\r\nh2. チケット報告手順\r\n\r\n{{include(mineya-shuzou-op:障害報告_ABC)}}\r\n\r\n'),(1335,'kitasanriku-sodegahama-gyokyo-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。','h2. [[kitasanriku-sodegahama-gyokyo-op:レベル1]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル1は、重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n\r\n障害対応レベル1の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へ電話やチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n\r\n{{include(kitasanriku-sodegahama-gyokyo-op:顧客緊急連絡先)}}\r\n'),(1336,'kitasanriku-sodegahama-gyokyo-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。','h2. [[kitasanriku-sodegahama-gyokyo-op:レベル2]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル2は、復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケースです。\r\n\r\n障害対応レベル2の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n'),(1337,'kitasanriku-sodegahama-gyokyo-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。','h2. [[kitasanriku-sodegahama-gyokyo-op:レベル3]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル3は、障害検知時のご連絡として、監視システムから自動メール通知または自動チケット起票のみを実施するケースです。\r\n\r\n障害対応レベル3の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n障害検知した内容が監視システムから自動メール通知または自動チケット起票されます。\r\nアールワークスの担当者が実施する障害報告・復旧作業はありません。\r\n'),(1338,'kitasanriku-railway-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。','h2. [[kitasanriku-railway-op:レベル1]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル1は、重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n\r\n障害対応レベル1の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へ電話やチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n\r\n{{include(kitasanriku-railway-op:連絡先)}}\r\n'),(1339,'kitasanriku-railway-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。','h2. [[kitasanriku-railway-op:レベル2]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル2は、復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケースです。\r\n\r\n障害対応レベル2の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n'),(1340,'kitasanriku-railway-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。','h2. [[kitasanriku-railway-op:レベル3]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル3は、障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケースです。\r\n\r\n障害対応レベル3の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n障害検知した内容が監視システムから自動メール通知されます。\r\nアールワークスの担当者が実施する障害報告・復旧作業はありません。\r\n'),(1341,'jittoku-nagaya-inner','レベル1','状況確認 および 緊急連絡','電話、チケットによる緊急連絡','h2. ① 状況確認\r\n\r\n# {{include(pandora_console)}}\r\n# {{include(監視対象機器)}}\r\n# 状況判断\r\n|_. 状況                           |_. 対応内容|\r\n|障害が発生中 or 障害発生もすぐ復旧|以下②以降の手順へ進む|\r\n|障害じゃなかった                  |社内宛てに連絡をして対応完了|\r\n\r\nh2. ② お客様へ障害検知を電話連絡し、エスカレーションしてください。 ([[緊急電話連絡先]])\r\n\r\n{{include(緊急電話連絡先)}}\r\n\r\nh2. ③ 電話連絡後、「障害対応」チケットを起票 ([[障害対応チケット]])\r\n\r\n{{include(障害対応チケット)}}\r\n\r\nh2. ④ 復旧手順\r\n\r\n* 復旧作業はお客様にて実施します。\r\n* お客様から作業依頼を受けた場合、依頼に従って作業してください。\r\n\r\n\r\nh2. ⑤ 復旧通知を受け取る\r\n\r\n* お客様作業により、復旧通知が届くはずです。\r\n\r\n\r\nh2. ⑥ お客様へ障害復旧を電話連絡 ([[緊急電話連絡先]])\r\n\r\n{{include(緊急電話連絡先)}}\r\n\r\nh2. ⑦ 電話連絡後、③で起票した「障害対応」チケットを更新、終了させる。\r\n\r\n{{include(障害対応チケット)}}\r\n'),(1342,'jittoku-nagaya-inner','レベル1N','状況確認、緊急連絡、障害復旧作業','電話、チケットによる連絡','h2. ① 状況確認\r\n\r\n# {{include(pandora_console)}}\r\n# {{include(監視対象機器)}}\r\n# 状況判断\r\n|_. 状況                           |_. 対応内容|\r\n|障害が発生中 or 障害発生もすぐ復旧|以下②以降の手順へ進む|\r\n|障害じゃなかった                  |社内宛てに連絡をして対応完了|\r\n\r\nh2. ② お客様へ障害検知を電話連絡 ([[緊急電話連絡先]])\r\n\r\n{{include(緊急電話連絡先)}}\r\n\r\nh2. ③ 電話連絡後、「障害対応」チケットを起票 ([[障害対応チケット]])\r\n\r\n{{include(障害対応チケット)}}\r\n\r\nh2. ④ 復旧手順\r\n\r\n* 主担当 and/or お客様と相談しながら対応\r\n* 障害毎に手順がある場合は、手順にそって対応\r\n* 弊社にて対応不可能な障害の場合、お客様にエスカレーションし、以降お客様による復旧作業を待ってください。\r\n\r\nh2. ⑤ お客様へ障害復旧を電話連絡 ([[緊急電話連絡先]])\r\n\r\n{{include(緊急電話連絡先)}}\r\n\r\nh2. ⑥ 電話連絡後、③で起票した「障害対応」チケットを更新、終了させる。\r\n\r\n{{include(障害対応チケット)}}\r\n'),(1343,'jittoku-nagaya-inner','レベル3','状況確認、障害復旧作業、通常連絡','チケットによる連絡','h2. ① 状況確認\r\n\r\n# {{include(pandora_console)}}\r\n# {{include(監視対象機器)}}\r\n# 状況判断\r\n|_. 状況                           |_. 対応内容|\r\n|障害が発生中 or 障害発生もすぐ復旧|以下②以降の手順へ進む|\r\n|障害じゃなかった                  |社内宛てに連絡をして対応完了|\r\n\r\nh2. ② 復旧手順\r\n\r\n* 主担当 and/or お客様と相談しながら対応\r\n* 障害毎に手順がある場合は、手順にそって対応\r\n* 弊社にて対応不可能な障害の場合、お客様にエスカレーションし、以降お客様による復旧作業を待ってください。\r\n\r\nh2. ③ 「障害対応」チケットを終了ステータスで起票する。\r\n\r\n{{include(障害対応チケット)}}\r\n'),(1344,'acron-layout-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。','h2. [[acron-layout-op:レベル1]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル1は、重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケースです。\r\n\r\n障害対応レベル1の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へ電話やチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n'),(1345,'acron-layout-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。','h2. [[acron-layout-op:レベル2]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル2は、復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケースです。\r\n\r\n障害対応レベル2の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n# 手早く状況を確認します。\r\n# お客様へチケットで第一報の連絡を行います。\r\n# 状況を詳細に確認し、確認した内容と復旧のための対応方針をチケットで連絡します。\r\n# 復旧対応を行い、対応内容をチケットで連絡します。\r\n'),(1346,'acron-layout-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。','h2. [[acron-layout-op:レベル3]]\r\n\r\nh3. 概要\r\n\r\n障害対応レベル3は、障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケースです。\r\n\r\n障害対応レベル3の監視項目において障害検知した際の一般的な対応は下記の通りです。監視項目別に説明がある場合はそちらに従って対応します。\r\n\r\nh3. 対応手順\r\n\r\n障害検知した内容が監視システムから自動メール通知されます。\r\nアールワークスの担当者が実施する障害報告・復旧作業はありません。\r\n'),(1347,'sekimachi-op','レベル1','サービスに影響のある障害です。 電話連絡による第一報を行った上で、復旧対応を行います。 → [[顧客緊急連絡先]]',NULL,NULL),(1348,'sekimachi-op','レベル2','冗長化されたサービスの片系障害など、直ちにサービス影響の発生しない障害です。 チケットによる報告を行った上で、復旧対応を行います。',NULL,NULL),(1349,'sekimachi-op','レベル3','サービスに影響のない障害です。 内容確認をした上で、チケットによる報告となります。',NULL,NULL),(1350,'diningmanner-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1351,'diningmanner-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1352,'ladderpencil-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1353,'ladderpencil-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1354,'nerimarubber-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1355,'nerimarubber-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1356,'diningmanner-www-trouble-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1357,'diningmanner-www-trouble-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1358,'diningmanner-temple-trouble-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1359,'diningmanner-temple-trouble-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1360,'diningmanner-lan-trouble-op','チケット',NULL,NULL,'即時直接的業務影響が発生するものではないため、チケット起票により、障害発生通知を行います。\n対応状況は都度、チケットにて報告いたします。'),(1361,'diningmanner-galaxy-trouble-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1362,'diningmanner-galaxy-trouble-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1363,'diningmanner-datalake-trouble-op','電話 + チケット',NULL,NULL,'お電話にて第一報の障害発生連絡を行います。その後、チケットを起票して、対応状況を都度、チケットにて報告いたします。'),(1364,'diningmanner-datalake-trouble-op','チケット',NULL,NULL,'チケット起票により、障害発生通知を行います。対応状況は都度、チケットにて報告いたします。'),(1365,'kaifuku-lab-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。',NULL),(1366,'kaifuku-lab-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。',NULL),(1367,'kaifuku-lab-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。',NULL),(1368,'kaifuku-tp-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。',NULL),(1369,'kaifuku-tp-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。',NULL),(1370,'kaifuku-tp-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。',NULL),(1371,'kaifuku-bcg-op','レベル1','状況確認→連絡(電話/メール)→対応→連絡(電話/メール)','重要なサービスが停止した場合等、電話にて貴社へ緊急連絡を差し上げた上で対応を実施するケース。',NULL),(1372,'kaifuku-bcg-op','レベル2','状況確認→連絡(メール)→対応→連絡(メール)','復旧について貴社との調整が不要な障害で、随時メールにて状況報告しながら対応を実施するケース。',NULL),(1373,'kaifuku-bcg-op','レベル3','自動通知(メール)','障害検知時のご連絡として、監視システムから自動メール通知のみを実施するケース。',NULL);
/*!40000 ALTER TABLE `severity_level_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vector_db_response`
--

DROP TABLE IF EXISTS `vector_db_response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vector_db_response` (
  `id` int NOT NULL AUTO_INCREMENT,
  `module` varchar(200) DEFAULT NULL,
  `state` varchar(200) DEFAULT NULL,
  `agent` varchar(200) DEFAULT NULL,
  `query` varchar(200) DEFAULT NULL,
  `solution` json DEFAULT NULL,
  `user` varchar(200) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3947 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vector_db_response`
--

LOCK TABLES `vector_db_response` WRITE;
/*!40000 ALTER TABLE `vector_db_response` DISABLE KEYS */;
/*!40000 ALTER TABLE `vector_db_response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'logsdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-13 17:54:36
