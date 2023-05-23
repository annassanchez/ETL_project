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
  `ranking` INT NOT NULL,
  `date` DATE NOT NULL,
  `url` VARCHAR(60) NOT NULL,
  `region` VARCHAR(45) NOT NULL,
  `chart` VARCHAR(25) NOT NULL,
  `trend` VARCHAR(45) NOT NULL,
  `streams` DOUBLE NULL,
  `highest_rank` INT NOT NULL,
  `weeks_in_rank` INT NOT NULL,
  `artist_url` VARCHAR(60) NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
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
  `artist_url` VARCHAR(60) NOT NULL,
  `artist_0` VARCHAR(60) NULL,
  `artist_1` VARCHAR(60) NULL,
  `artist_2` VARCHAR(60) NULL,
  `published_track` VARCHAR(25) NULL,
  `published` VARCHAR(25) NULL,
  `summary` MEDIUMTEXT NULL,
  `content` LONGTEXT NULL,
  `aritist_genre_0` VARCHAR(60) NULL,
  `aritist_genre_1` VARCHAR(60) NULL,
  `aritist_genre_2` VARCHAR(60) NULL,
  `aritist_genre_3` VARCHAR(60) NULL,
  `aritist_genre_4` VARCHAR(60) NULL,
  `track_genre_0` VARCHAR(60) NULL,
  `track_genre_1` VARCHAR(60) NULL,
  `track_genre_2` VARCHAR(60) NULL,
  `track_genre_3` VARCHAR(60) NULL,
  `track_genre_4` VARCHAR(60) NULL,
  `music_genre` VARCHAR(45) NULL,
  `gender` VARCHAR(15) NULL,
  `birthday_date` VARCHAR(25) NULL,
  `age` INT NULL,
  PRIMARY KEY (`artist_url`),
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
  `artist_url` VARCHAR(60) NOT NULL,
  `URI` VARCHAR(45) NULL,
  `daceability` DOUBLE NULL,
  `energy` DOUBLE NULL,
  `key_song` INT NULL,
  `loudness` DOUBLE NULL,
  `mode_song` INT NULL,
  `speechiness` DOUBLE NULL,
  `acousticness` DOUBLE NULL,
  `instrumentalness` DOUBLE NULL,
  `liveness` DOUBLE NULL,
  `valence` DOUBLE NULL,
  `tempo` DOUBLE NULL,
  `duration_ms` DOUBLE NULL,
  `duration_mins` INT NULL,
  `popularity` INT NULL,
  `release_date` VARCHAR(15) NULL,
  PRIMARY KEY (`artist_url`),
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
