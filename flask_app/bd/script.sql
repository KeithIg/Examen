-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_citas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_citas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_citas` DEFAULT CHARACTER SET utf8 ;
USE `esquema_citas` ;

-- -----------------------------------------------------
-- Table `esquema_citas`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_citas`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_citas`.`appointments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_citas`.`appointments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `task` TEXT NULL,
  `date` DATE NULL,
  `status` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_appointments_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_appointments_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_citas`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
