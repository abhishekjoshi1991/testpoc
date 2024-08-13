-- imai.postprocess_pattern definition
CREATE TABLE `postprocess_pattern` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pattern` varchar(500) NOT NULL,
  `replacement` varchar(500) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
);