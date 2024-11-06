-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bdcrudpy
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `table_products`
--

DROP TABLE IF EXISTS `table_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_products` (
  `ID_produto` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `preco` float DEFAULT NULL,
  PRIMARY KEY (`ID_produto`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_products`
--

LOCK TABLES `table_products` WRITE;
/*!40000 ALTER TABLE `table_products` DISABLE KEYS */;
INSERT INTO `table_products` VALUES (1,'Arroz',50,3.99),(2,'Feijão',40,5.49),(3,'Açúcar',30,2.89),(4,'Sal',25,1.29),(5,'Café',20,8.99),(6,'Farinha de trigo',15,4.49),(7,'Óleo de soja',35,6.29),(8,'Macarrão',45,2.99),(9,'Leite',60,4.49),(10,'Manteiga',10,6.79),(11,'Margarina',25,3.49),(12,'Queijo mussarela',12,14.99),(13,'Presunto',18,9.99),(14,'Frango',40,12.59),(15,'Carne bovina',20,25.99),(16,'Linguiça',30,10.89),(17,'Peito de peru',10,11.99),(18,'Ovos',50,9.49),(19,'Pão de forma',30,5.69),(20,'Pão francês',60,0.69),(21,'Biscoito recheado',40,3.49),(22,'Biscoito de água e sal',50,2.49),(23,'Batata',80,4.19),(24,'Cenoura',45,3.29),(25,'Tomate',70,5.99),(26,'Alface',30,1.99),(27,'Cebola',60,3.89),(28,'Alho',20,2.59),(29,'Maçã',50,4.99),(30,'Banana',80,3.49),(31,'Laranja',60,3.29),(32,'Melancia',15,8.49),(33,'Uva',25,6.99),(34,'Morango',20,5.99),(35,'Abacaxi',10,4.79),(36,'Sabão em pó',40,7.99),(37,'Sabonete',60,1.89),(38,'Desodorante',25,9.99),(39,'Shampoo',30,10.49),(40,'Condicionador',30,11.29),(41,'Creme dental',45,3.99),(42,'Papel higiênico',50,12.49),(43,'Água sanitária',35,4.29),(44,'Amaciante',20,8.99),(45,'Detergente',40,2.29),(46,'Limpador multiuso',30,6.49),(47,'Esponja de aço',30,1.59),(48,'Sabão líquido',25,5.89),(49,'Refrigerante',60,5.99),(50,'Suco de laranja',40,3.49),(51,'Suco de uva',30,4.99),(52,'Cerveja',50,3.19),(53,'Vinho tinto',15,24.99),(54,'Vodka',20,29.99),(55,'Massa para pizza',10,7.99),(56,'Molho de tomate',35,3.49),(57,'Ketchup',30,6.29),(58,'Maionese',25,5.69),(59,'Mostarda',20,4.29),(60,'Leite condensado',30,3.99),(61,'Creme de leite',40,2.99),(62,'Achocolatado',25,7.49),(63,'Chocolate em barra',15,4.99),(64,'Gelatina',50,1.59),(65,'Manteiga de amendoim',20,9.99),(66,'Mel',20,12.99),(67,'Granola',15,10.89),(68,'Aveia',30,4.49),(69,'Cereal matinal',20,7.99),(70,'Bolo pronto',25,5.49),(71,'Bolacha de maizena',40,3.29),(72,'Iogurte',35,2.89),(73,'Pizza congelada',10,15.99),(74,'Salsicha',50,6.99),(75,'Hambúrguer',30,10.99),(76,'Batata frita congelada',25,8.49),(77,'Sorvete',20,12.49),(78,'Pipoca de micro-ondas',40,2.99),(79,'Chá mate',35,4.99),(80,'Chá verde',15,6.49),(81,'Erva-doce',20,5.29),(82,'Carvão',10,14.99),(83,'Amendoim',25,3.99),(84,'Castanha de caju',15,18.49),(85,'Castanha do Pará',15,20.49),(86,'Nozes',10,22.99),(87,'Azeitona',30,8.99),(88,'Picles',20,6.99),(89,'Suco detox',15,9.99),(90,'Cenoura baby',20,3.89),(91,'Brócolis',25,5.29),(92,'Couve-flor',20,5.99),(93,'Espinafre',15,4.49),(94,'Gengibre',10,9.49),(95,'Pimenta',10,2.99),(96,'Leite em pó',30,10.99),(97,'Água de coco',40,4.99);
/*!40000 ALTER TABLE `table_products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-02  1:05:41
