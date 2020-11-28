CREATE DATABASE  IF NOT EXISTS `myfitapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `myfitapp`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: myfitapp
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cardiovascular`
--

DROP TABLE IF EXISTS `cardiovascular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardiovascular` (
  `id_ejercicio` int NOT NULL AUTO_INCREMENT,
  `nombreEjercicio` varchar(45) NOT NULL,
  `caloriasQuemadas` decimal(10,2) NOT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_ejercicio`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardiovascular`
--

LOCK TABLES `cardiovascular` WRITE;
/*!40000 ALTER TABLE `cardiovascular` DISABLE KEYS */;
INSERT INTO `cardiovascular` VALUES (1,'Pasos altos',40.00,1),(2,'Escalada',35.00,1),(3,'Comba',100.00,1),(4,'Flexiones con sentadillas',110.00,1),(5,'Corrida(100mts)',50.00,1),(6,'Mountain Climbers',80.00,2),(7,'Bicicleta',100.00,2),(8,'Eliptica',200.00,1),(9,'Aerobicos',100.00,2),(10,'Side Plank',80.00,1);
/*!40000 ALTER TABLE `cardiovascular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumoalimento`
--

DROP TABLE IF EXISTS `consumoalimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumoalimento` (
  `id_consumoAlimento` int NOT NULL AUTO_INCREMENT,
  `id_producto` int NOT NULL,
  `id_usuario` int NOT NULL,
  `porcion` decimal(10,2) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id_consumoAlimento`,`id_producto`,`id_usuario`),
  KEY `fk_ConsumoAlimento_Producto1_idx` (`id_producto`),
  KEY `fk_ConsumoAlimento_Usuario1_idx` (`id_usuario`),
  CONSTRAINT `fk_ConsumoAlimento_Producto1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  CONSTRAINT `fk_ConsumoAlimento_Usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumoalimento`
--

LOCK TABLES `consumoalimento` WRITE;
/*!40000 ALTER TABLE `consumoalimento` DISABLE KEYS */;
INSERT INTO `consumoalimento` VALUES (1,1,1,2.00,'2020-11-29 00:00:00'),(2,3,5,1.00,'2020-11-25 00:00:00'),(3,9,1,2.00,'2020-11-29 00:00:00'),(4,14,1,1.00,'2020-11-29 00:00:00'),(5,13,5,1.00,'2020-11-25 00:00:00'),(6,18,5,1.00,'2020-11-29 00:00:00'),(7,4,2,1.00,'2020-11-20 00:00:00'),(8,1,2,1.00,'2020-11-20 00:00:00'),(9,9,2,1.00,'2020-11-20 00:00:00'),(10,15,3,1.00,'2020-11-21 00:00:00'),(11,17,3,4.00,'2020-11-21 00:00:00'),(12,12,3,2.00,'2020-11-21 00:00:00'),(13,5,4,2.00,'2020-11-19 00:00:00'),(14,8,4,3.00,'2020-11-19 00:00:00'),(15,10,4,1.00,'2020-11-19 00:00:00'),(16,3,1,2.00,'2020-11-16 21:40:39'),(17,19,1,3.00,'2020-11-16 00:00:00');
/*!40000 ALTER TABLE `consumoalimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fuerza`
--

DROP TABLE IF EXISTS `fuerza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fuerza` (
  `id_ejercicio` int NOT NULL AUTO_INCREMENT,
  `nombreEjercicio` varchar(45) NOT NULL,
  `parteDelCuerpo` varchar(45) DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_ejercicio`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fuerza`
--

LOCK TABLES `fuerza` WRITE;
/*!40000 ALTER TABLE `fuerza` DISABLE KEYS */;
INSERT INTO `fuerza` VALUES (1,'Sentadillas','Piernas',1),(2,'Lagartijas','Pectorales y Triceps',1),(3,'Flexion de biceps','biceps',0),(4,'Burppes','Piernas',1),(5,'Mountain climber','Biceps y abdomen',1),(6,'Planks','Hombros y abdomen',2),(7,'Pose de cobra','abdomen',1),(8,'Saltos','Pantorrillas',2),(9,'Remo','Brazos',1),(10,'Estocadas','Piernas',2);
/*!40000 ALTER TABLE `fuerza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genero` (
  `id_genero` int NOT NULL AUTO_INCREMENT,
  `Genero` varchar(45) NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
INSERT INTO `genero` VALUES (1,'Masculino'),(2,'Femenino');
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objetivos`
--

DROP TABLE IF EXISTS `objetivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objetivos` (
  `id_objetivos` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `objetivos` varchar(500) NOT NULL,
  `caloriasPorDia` int DEFAULT NULL,
  `pesoIdeal` int DEFAULT NULL,
  PRIMARY KEY (`id_objetivos`,`id_usuario`),
  KEY `fk_Objetivos_Usuario1_idx` (`id_usuario`),
  CONSTRAINT `fk_Objetivos_Usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objetivos`
--

LOCK TABLES `objetivos` WRITE;
/*!40000 ALTER TABLE `objetivos` DISABLE KEYS */;
INSERT INTO `objetivos` VALUES (1,1,'Lograr hacer mas repeticiones de las propuestas',350,140),(2,2,'Repetir la sesion de ejercicios 2 veces',250,150),(3,3,'levantar mas peso del propuesto',300,130),(4,4,'Hacer el primer ejercicio propuesto almenos 2 veces',400,170),(5,5,'Terminar haciendo 1 ejercicio extra de su preferencia',350,160);
/*!40000 ALTER TABLE `objetivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `calorias` decimal(10,2) NOT NULL,
  `grasasTotales` decimal(10,2) NOT NULL,
  `colesterol` decimal(10,2) NOT NULL,
  `sodio` decimal(10,2) NOT NULL,
  `azucares` decimal(10,2) NOT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Huevo',155.00,10.00,373.00,1.24,1.10,0),(2,'Carne roja',130.00,7.00,95.00,3.97,11.00,0),(3,'Pollo',239.00,3.80,88.00,0.32,0.70,0),(4,'Aguacate',160.00,2.10,0.00,0.70,0.70,0),(5,'Banano',122.00,0.10,0.00,0.40,15.00,0),(6,'Manzana',52.00,0.20,0.00,0.10,10.00,1),(7,'Pera',57.00,0.00,0.00,0.10,10.00,1),(8,'Melocoton',39.00,0.00,0.00,0.00,8.00,1),(9,'Pan integral',313.00,1.00,0.00,6.01,6.00,2),(10,'Yogurt',59.00,0.10,0.50,0.36,3.20,2),(11,'Avena',350.00,6.52,0.37,2.86,4.70,2),(12,'Brocoli',7.00,0.90,0.26,2.70,1.80,2),(13,'Arroz integral',111.00,0.20,0.00,0.50,0.40,2),(14,'Nueces',607.00,13.00,0.74,0.20,4.20,2),(15,'Pescado',206.00,6.00,0.63,0.61,1.20,2),(16,'Zanahoria',37.00,0.24,0.93,0.61,4.24,2),(17,'Lechuga',15.00,0.00,0.00,0.28,0.80,2),(18,'Pepino',16.00,0.00,0.00,0.15,0.50,2),(19,'Tomate',18.00,0.00,0.00,0.05,2.60,1),(20,'Naranjas',40.00,0.12,0.11,0.01,23.00,1);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrodiario`
--

DROP TABLE IF EXISTS `registrodiario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrodiario` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `cintura` decimal(10,2) NOT NULL,
  `cuello` decimal(10,2) NOT NULL,
  `pesoActual` decimal(10,2) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id_registro`,`id_usuario`),
  KEY `fk_RegistroDiario_Usuario1_idx` (`id_usuario`),
  CONSTRAINT `fk_RegistroDiario_Usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrodiario`
--

LOCK TABLES `registrodiario` WRITE;
/*!40000 ALTER TABLE `registrodiario` DISABLE KEYS */;
INSERT INTO `registrodiario` VALUES (1,1,40.00,20.00,160.00,'2020-11-10 00:00:00'),(2,2,40.00,25.00,170.00,'2020-11-19 00:00:00'),(3,3,30.00,20.00,140.00,'2020-11-15 00:00:00'),(4,4,50.00,20.00,190.00,'2020-11-10 00:00:00'),(5,5,50.00,10.00,180.00,'2020-11-14 00:00:00'),(6,1,0.00,22.00,0.00,'2020-11-16 00:00:00');
/*!40000 ALTER TABLE `registrodiario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrousuarioejerciciocardio`
--

DROP TABLE IF EXISTS `registrousuarioejerciciocardio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrousuarioejerciciocardio` (
  `id_registroUsuarioCardio` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_ejercicio` int NOT NULL,
  `tiempoTotalEmpleado` int NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id_registroUsuarioCardio`,`id_usuario`,`id_ejercicio`),
  KEY `fk_EjercicioUsuario_InformacionUsuario1_idx` (`id_usuario`),
  KEY `fk_EjercicioUsuario_cardio_Cardiovascular1_idx` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_cardio_Cardiovascular1` FOREIGN KEY (`id_ejercicio`) REFERENCES `cardiovascular` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_InformacionUsuario10` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrousuarioejerciciocardio`
--

LOCK TABLES `registrousuarioejerciciocardio` WRITE;
/*!40000 ALTER TABLE `registrousuarioejerciciocardio` DISABLE KEYS */;
INSERT INTO `registrousuarioejerciciocardio` VALUES (1,1,1,5,'2020-11-29 00:00:00'),(2,1,6,10,'2020-11-29 00:00:00'),(3,1,5,5,'2020-11-29 00:00:00'),(4,4,1,3,'2020-11-25 00:00:00'),(5,4,4,5,'2020-11-25 00:00:00'),(6,4,10,4,'2020-11-25 00:00:00'),(7,5,2,2,'2020-11-20 00:00:00'),(8,5,3,5,'2020-11-20 00:00:00'),(9,5,7,20,'2020-11-20 00:00:00'),(10,3,9,10,'2020-11-19 00:00:00'),(11,3,1,5,'2020-11-19 00:00:00'),(12,3,6,5,'2020-11-19 00:00:00');
/*!40000 ALTER TABLE `registrousuarioejerciciocardio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrousuarioejerciciofuerza`
--

DROP TABLE IF EXISTS `registrousuarioejerciciofuerza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrousuarioejerciciofuerza` (
  `id_registroUsuarioFuerza` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_ejercicio` int NOT NULL,
  `repeticiones` int NOT NULL,
  `series` int NOT NULL,
  `pesoAplicado` decimal(10,2) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id_registroUsuarioFuerza`,`id_usuario`,`id_ejercicio`),
  KEY `fk_EjercicioUsuario_InformacionUsuario1_idx` (`id_usuario`),
  KEY `fk_EjercicioUsuario_Ejercicios1_idx` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_Ejercicios1` FOREIGN KEY (`id_ejercicio`) REFERENCES `fuerza` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_InformacionUsuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrousuarioejerciciofuerza`
--

LOCK TABLES `registrousuarioejerciciofuerza` WRITE;
/*!40000 ALTER TABLE `registrousuarioejerciciofuerza` DISABLE KEYS */;
INSERT INTO `registrousuarioejerciciofuerza` VALUES (1,1,1,20,2,5.00,'2020-11-29 00:00:00'),(2,1,7,1,1,0.00,'2020-11-29 00:00:00'),(3,1,10,10,3,10.00,'2020-11-29 00:00:00'),(4,2,4,20,2,10.00,'2020-11-25 00:00:00'),(5,2,8,10,4,2.00,'2020-11-25 00:00:00'),(6,2,9,20,3,20.00,'2020-11-25 00:00:00'),(7,3,4,15,3,10.00,'2020-11-19 00:00:00'),(8,3,5,15,2,15.00,'2020-11-19 00:00:00'),(9,3,6,10,3,10.00,'2020-11-19 00:00:00'),(10,4,9,10,4,10.00,'2020-11-19 00:00:00'),(11,4,3,20,1,5.00,'2020-11-19 00:00:00'),(12,4,10,10,2,10.00,'2020-11-19 00:00:00'),(13,5,6,10,3,10.00,'2020-11-23 00:00:00'),(14,5,8,10,2,10.00,'2020-11-23 00:00:00'),(15,5,7,1,1,0.00,'2020-11-23 00:00:00');
/*!40000 ALTER TABLE `registrousuarioejerciciofuerza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `user` varchar(45) NOT NULL,
  `contra` varchar(45) NOT NULL,
  `id_genero` int NOT NULL,
  `altura` decimal(10,2) NOT NULL,
  `pesoActual` decimal(10,2) NOT NULL,
  `pesoDeseado` decimal(10,2) NOT NULL,
  `nacimiento` datetime NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_genero`),
  UNIQUE KEY `usuario_UNIQUE` (`user`),
  UNIQUE KEY `correo_UNIQUE` (`correo`),
  KEY `fk_Usuario_Genero1_idx` (`id_genero`),
  CONSTRAINT `fk_Usuario_Genero1` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Sofia','Gomez','sofia@gmail.com','sofiasofia','12345',2,1.75,160.00,140.00,'2001-03-28 00:00:00'),(2,'Alberto','Caceres','Caceres@gmail.com','albertoalberto','12345',1,1.70,170.00,150.00,'1999-09-06 00:00:00'),(3,'Valeria','Flores','Vale@gmail.com','valeriavaleria','12345',2,1.65,140.00,130.00,'2000-08-20 00:00:00'),(4,'Juan','Ramírez','juan@gmail.com','juanjuan','12345',1,1.70,190.00,170.00,'1997-02-06 00:00:00'),(5,'Erick','Olmedo','erick@gmail.com','erickerick','12345',1,1.78,180.00,160.00,'2000-08-10 00:00:00'),(6,'Jesús','Barahona','jesus@gmail.com','Jesús','12345',1,1.75,70.00,65.00,'1999-10-25 00:00:00'),(7,'Gil','López','yill@gmail.com','Yill','12345',1,1.55,50.00,45.00,'2001-07-20 00:00:00'),(8,'Alejandra','Mejía','ale@gmail.com','Alejandra','12345',2,1.50,50.00,45.00,'1998-02-12 00:00:00');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-17 19:17:49
