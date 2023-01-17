-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema playlists_analysis
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`artist` (
  `url` VARCHAR(60) NOT NULL,
  `artist` VARCHAR(1000) NULL,
  `title` VARCHAR(5000) NULL,
  PRIMARY KEY (`url`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`playlist` (
  `idplaylist` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(5000) NOT NULL,
  `ranking` INT NOT NULL,
  `date` DATE NOT NULL,
  `artist` VARCHAR(1000) NOT NULL,
  `url` VARCHAR(60) NOT NULL,
  `region` VARCHAR(45) NOT NULL,
  `chart` VARCHAR(25) NOT NULL,
  `trend` VARCHAR(45) NOT NULL,
  `streams` DOUBLE NULL,
  `highest_rank` INT NOT NULL,
  `weeks_in_rank` INT NOT NULL,
  `artist_url` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`idplaylist`),
  INDEX `fk_playlist_artist1_idx` (`artist_url` ASC) VISIBLE,
  CONSTRAINT `fk_playlist_artist1`
    FOREIGN KEY (`artist_url`)
    REFERENCES `mydb`.`artist` (`url`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`lastfm`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`lastfm` (
  `url` VARCHAR(60) NOT NULL,
  `artist` VARCHAR(1000) NOT NULL,
  `track` VARCHAR(5000) NOT NULL,
  `published_track` DATETIME NULL,
  `published` DATETIME NULL,
  `summary` BLOB NULL,
  `content` LONGBLOB NULL,
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
  `genre` VARCHAR(45) NULL,
  `artist_url` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`url`),
  INDEX `fk_lastfm_artist1_idx` (`artist_url` ASC) VISIBLE,
  CONSTRAINT `fk_lastfm_artist1`
    FOREIGN KEY (`artist_url`)
    REFERENCES `mydb`.`artist` (`url`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`spotify`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`spotify` (
  `url` VARCHAR(60) NOT NULL,
  `artist` VARCHAR(1000) NOT NULL,
  `track` VARCHAR(5000) NOT NULL,
  `URI` VARCHAR(45) NULL,
  `daceability` DOUBLE NULL,
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
  `duration_ms` DOUBLE NULL,
  `duration_mins` INT NULL,
  `artist_url` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`url`, `artist_url`),
  INDEX `fk_spotify_artist1_idx` (`artist_url` ASC) VISIBLE,
  CONSTRAINT `fk_spotify_artist1`
    FOREIGN KEY (`artist_url`)
    REFERENCES `mydb`.`artist` (`url`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
