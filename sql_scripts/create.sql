-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema playlists_analysis
-- -----------------------------------------------------
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist` (
  `id` VARCHAR(45) NOT NULL,
  `title` VARCHAR(5000) NOT NULL,
  `rank` INT NOT NULL,
  `date` DATE NOT NULL,
  `artist` VARCHAR(1000) NOT NULL,
  `url` VARCHAR(45) NOT NULL,
  `region` VARCHAR(45) NOT NULL,
  `chart` VARCHAR(15) NOT NULL,
  `trend` VARCHAR(45) NOT NULL,
  `streams` DOUBLE NULL,
  `highest_rank` INT NOT NULL,
  `weeks_in_charts` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`lastfm`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`lastfm` (
  `idlastfm` INT NOT NULL,
  `published_track` VARCHAR(45) NULL,
  `published` VARCHAR(45) NULL,
  `summary` VARCHAR(2000) NULL,
  `content` VARCHAR(5000) NULL,
  `aritist_genre_0` VARCHAR(25) NULL,
  `aritist_genre_1` VARCHAR(25) NULL,
  `aritist_genre_2` VARCHAR(25) NULL,
  `aritist_genre_3` VARCHAR(25) NULL,
  `aritist_genre_4` VARCHAR(25) NULL,
  `track_genre_0` VARCHAR(25) NULL,
  `track_genre_1` VARCHAR(25) NULL,
  `track_genre_2` VARCHAR(25) NULL,
  `track_genre_3` VARCHAR(25) NULL,
  `track_genre_4` VARCHAR(25) NULL,
  `url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idlastfm`),
  INDEX `fk_lastfm_playlist1_idx` (`url` ASC) VISIBLE,
  CONSTRAINT `fk_lastfm_playlist1`
    FOREIGN KEY (`url`)
    REFERENCES `mydb`.`playlist` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`spotify`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`spotify` (
  `idspotify` INT NOT NULL,
  `artist` VARCHAR(1000) NULL,
  `track` VARCHAR(5000) NULL,
  `uri` VARCHAR(45) NULL,
  `dancebility` DOUBLE NULL,
  `energy` DOUBLE NULL,
  `key` INT NULL,
  `loudness` DOUBLE NULL,
  `mode` INT NULL,
  `speechiness` DOUBLE NULL,
  `acousticness` DOUBLE NULL,
  `instrumentalness` DOUBLE NULL,
  `liveness` DOUBLE NULL,
  `valence` DOUBLE NULL,
  `tempo` DOUBLE NULL,
  `type` VARCHAR(45) NULL,
  `track_href` VARCHAR(45) NULL,
  `time_seg` DOUBLE NULL,
  `time_min` INT NULL,
  `url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idspotify`),
  INDEX `fk_spotify_playlist_idx` (`url` ASC) VISIBLE,
  CONSTRAINT `fk_spotify_playlist`
    FOREIGN KEY (`url`)
    REFERENCES `mydb`.`playlist` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
