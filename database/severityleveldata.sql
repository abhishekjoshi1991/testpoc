-- imai.severity_level_data definition
CREATE TABLE `severity_level_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identifier` varchar(200) DEFAULT NULL,
  `troubleshoot_level` longtext,
  `troubleshoot_flow` longtext,
  `troubleshoot_descripton` longtext,
  `level_content` longtext,
  PRIMARY KEY (`id`)
);