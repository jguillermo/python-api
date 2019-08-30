-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: flash_test
-- ------------------------------------------------------
-- Server version	5.7.25

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8_spanish2_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('9a0feec33aae');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_challenge`
--

DROP TABLE IF EXISTS `gm_challenge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_challenge` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `project` varchar(50) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `title` varchar(200) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `description` text COLLATE utf8_spanish2_ci,
  `score` int(11) DEFAULT NULL,
  `start_at` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `status` varchar(50) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `challenge_number` int(11) DEFAULT NULL,
  `challenge_event` varchar(50) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_challenge`
--

LOCK TABLES `gm_challenge` WRITE;
/*!40000 ALTER TABLE `gm_challenge` DISABLE KEYS */;
INSERT INTO `gm_challenge` VALUES ('0771ff7f-5628-4587-ba41-84c550780d80','ugo','UGO Estudiantes','Asiste a 04 sesiones de UGO Estudiantes en esta semana.',200,'2019-07-01 00:00:00',7,'enable',4,'ugo_session_student_attended',1,10,1,'2019-08-21 19:24:19'),('0d3bddf6-3aed-4eea-a03e-b97279b7fc33','pepe','Pepe','Responde 03 preguntas en la web de PEPE en esta semana.',144,'2019-07-01 00:00:00',7,'enable',3,'pepe_answer_created',2,10,1,'2019-08-21 19:24:19'),('12341608-e65a-44da-baa2-df6ce61ea947','pepe','Pepe','Realiza 02 preguntas en la web de PEPE en esta semana.',70,'2019-07-01 00:00:00',7,'enable',2,'pepe_question_created',2,10,1,'2019-08-21 19:24:19'),('3c7e499c-5e5a-4fb5-a3f6-af31f273b2e1','pepe','Pepe','Responde 02 preguntas en la web de PEPE en esta semana.',70,'2019-07-01 00:00:00',7,'enable',2,'pepe_answer_created',2,10,1,'2019-08-21 19:24:19'),('698ee3ce-ca6f-4bda-8e33-a985d2b01b48','pepe','Pepe','Realiza 04 preguntas en la web de PEPE en esta semana.',140,'2019-07-01 00:00:00',7,'enable',4,'pepe_question_created',2,10,1,'2019-08-21 19:24:19'),('861afea5-b7b7-4125-b93b-1d5323dad675','ugo','UGO Estudiantes','Agenda 02 sesiones de tutoría (presencial o virtual) en UGO Estudiantes.',100,'2019-07-01 00:00:00',7,'enable',2,'ugo_session_student_scheduled',2,10,1,'2019-08-21 19:24:19'),('c44b4b43-8390-4647-aa28-93898992dda0','ugo','UGO Estudiantes','Agenda 04 sesiones de tutoría (presencial o virtual) en UGO Estudiantes.',180,'2019-07-01 00:00:00',7,'enable',4,'ugo_session_student_scheduled',2,10,1,'2019-08-21 19:24:19'),('c9369770-ae19-4253-bd27-cd95270b400f','ugo','UGO Estudiantes','Califica 01 sesión de tutoría o taller en UGO Estudiantes  en esta semana.',100,'2019-07-01 00:00:00',7,'enable',1,'ugo_session_student_rated',2,10,1,'2019-08-21 19:24:19'),('e7bc3f0c-501e-4bc1-aec4-66da06ad07d9','ugo','UGO Estudiantes','Asiste a 02 sesiones de UGO Estudiantes en esta semana.',150,'2019-07-01 00:00:00',7,'enable',1,'ugo_session_student_attended',2,10,1,'2019-08-21 19:24:19'),('ed382a03-60c8-4f90-9486-ac2bcc507cd9','ugo','UGO Estudiantes','Califica 03 sesiones de tutoría o taller en UGO Estudiantes  en esta semana.',180,'2019-07-01 00:00:00',7,'enable',3,'ugo_session_student_rated',2,10,1,'2019-08-21 19:24:19');
/*!40000 ALTER TABLE `gm_challenge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_claim`
--

DROP TABLE IF EXISTS `gm_claim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_claim` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `code` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `student_id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `reward_id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `score` int(11) DEFAULT NULL,
  `claimed_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`student_id`,`reward_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_claim`
--

LOCK TABLES `gm_claim` WRITE;
/*!40000 ALTER TABLE `gm_claim` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_claim` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_level`
--

DROP TABLE IF EXISTS `gm_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_level` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `level` int(11) DEFAULT NULL,
  `min_point` int(11) DEFAULT NULL,
  `max_point` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_level`
--

LOCK TABLES `gm_level` WRITE;
/*!40000 ALTER TABLE `gm_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_progress`
--

DROP TABLE IF EXISTS `gm_progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_progress` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `total` int(11) DEFAULT NULL,
  `progress` int(11) DEFAULT NULL,
  `status` varchar(50) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `challenge_id` char(36) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `student_id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `date_start` datetime DEFAULT NULL,
  `date_end` datetime DEFAULT NULL,
  `seen` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `gm_progress_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `gm_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_progress`
--

LOCK TABLES `gm_progress` WRITE;
/*!40000 ALTER TABLE `gm_progress` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_progress_item`
--

DROP TABLE IF EXISTS `gm_progress_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_progress_item` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `challenge_event` varchar(50) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `student_id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `gm_progress_item_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `gm_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_progress_item`
--

LOCK TABLES `gm_progress_item` WRITE;
/*!40000 ALTER TABLE `gm_progress_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_progress_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_reward`
--

DROP TABLE IF EXISTS `gm_reward`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_reward` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `point` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `expiration` datetime DEFAULT NULL,
  `title` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `image` varchar(150) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `description` text COLLATE utf8_spanish2_ci,
  `requirement` text COLLATE utf8_spanish2_ci,
  `condition` text COLLATE utf8_spanish2_ci,
  `map` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_reward`
--

LOCK TABLES `gm_reward` WRITE;
/*!40000 ALTER TABLE `gm_reward` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_reward` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_student`
--

DROP TABLE IF EXISTS `gm_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_student` (
  `id` char(36) COLLATE utf8_spanish2_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `last_name` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `code` varchar(15) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `campus` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_student`
--

LOCK TABLES `gm_student` WRITE;
/*!40000 ALTER TABLE `gm_student` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gm_student_access`
--

DROP TABLE IF EXISTS `gm_student_access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gm_student_access` (
  `code` char(9) COLLATE utf8_spanish2_ci NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gm_student_access`
--

LOCK TABLES `gm_student_access` WRITE;
/*!40000 ALTER TABLE `gm_student_access` DISABLE KEYS */;
/*!40000 ALTER TABLE `gm_student_access` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-27 19:47:48
