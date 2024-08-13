-- imai.generated_sop_feedback definition
CREATE TABLE `generated_sop_feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `msa_id` int NOT NULL,
  `generated_sop` longtext,
  `comments` longtext,
  PRIMARY KEY (`id`),
  KEY `msa_id` (`msa_id`),
  CONSTRAINT `generated_sop_feedback_ibfk_1` FOREIGN KEY (`msa_id`) REFERENCES `master_module_state_agent` (`id`)
);