-- imai.contact_information definition
CREATE TABLE `contact_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identifier` varchar(200) DEFAULT NULL,
  `contact_page_content` longtext,
  PRIMARY KEY (`id`)
);