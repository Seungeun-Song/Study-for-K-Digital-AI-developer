-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.5.8-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- website 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `website` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `website`;

-- 테이블 website.backup_member 구조 내보내기
CREATE TABLE IF NOT EXISTS `backup_member` (
  `memberid` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(6) NOT NULL,
  `gender` enum('M','F') DEFAULT NULL,
  `memberAddress` varchar(50) DEFAULT NULL,
  `memberPhone` char(11) NOT NULL,
  `memberEmail` varchar(50) DEFAULT NULL,
  `modtype` char(2) DEFAULT NULL,
  `moddate` date DEFAULT NULL,
  `moduser` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`memberid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 website.board 구조 내보내기
CREATE TABLE IF NOT EXISTS `board` (
  `boardNo` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `name` char(6) NOT NULL,
  `title` mediumtext NOT NULL,
  `content` longtext NOT NULL,
  `views` int(11) NOT NULL DEFAULT 0,
  KEY `name` (`name`),
  KEY `boardNo` (`boardNo`),
  CONSTRAINT `FK_board_member` FOREIGN KEY (`name`) REFERENCES `member` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 website.comment_board 구조 내보내기
CREATE TABLE IF NOT EXISTS `comment_board` (
  `boardNo` int(11) NOT NULL,
  `name` varchar(6) NOT NULL,
  `date` mediumtext NOT NULL,
  `content` mediumtext NOT NULL,
  KEY `name` (`name`),
  KEY `boardNo` (`boardNo`),
  CONSTRAINT `FK_comment_board` FOREIGN KEY (`boardNo`) REFERENCES `board` (`boardNo`),
  CONSTRAINT `FK_comment_member` FOREIGN KEY (`name`) REFERENCES `member` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 website.comment_file 구조 내보내기
CREATE TABLE IF NOT EXISTS `comment_file` (
  `fileNo` int(11) NOT NULL,
  `name` varchar(6) NOT NULL,
  `date` date NOT NULL,
  `content` mediumtext NOT NULL,
  KEY `fileNo` (`fileNo`),
  KEY `name` (`name`),
  CONSTRAINT `FK_comment_file_fileupload` FOREIGN KEY (`fileNo`) REFERENCES `fileupload` (`fileNo`),
  CONSTRAINT `FK_comment_file_member` FOREIGN KEY (`name`) REFERENCES `member` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 website.fileupload 구조 내보내기
CREATE TABLE IF NOT EXISTS `fileupload` (
  `fileNo` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(6) NOT NULL,
  `date` date NOT NULL,
  `title` mediumtext NOT NULL,
  `extention` varchar(10) NOT NULL,
  `content` mediumtext NOT NULL,
  KEY `name` (`name`),
  KEY `fileNo` (`fileNo`),
  CONSTRAINT `FK_fileupload_member` FOREIGN KEY (`name`) REFERENCES `member` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 website.member 구조 내보내기
CREATE TABLE IF NOT EXISTS `member` (
  `memberID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(6) NOT NULL,
  `gender` enum('M','F') DEFAULT NULL,
  `memberAddress` varchar(50) DEFAULT NULL,
  `memberPhone` char(11) NOT NULL DEFAULT '0',
  `memberEmail` varchar(50) DEFAULT NULL,
  `mDate` date NOT NULL,
  PRIMARY KEY (`memberID`),
  KEY `FK_member_board_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 트리거 website.backupmember 구조 내보내기
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER backupmember
	AFTER update
	ON member
	FOR EACH ROW
BEGIN 
	INSERT INTO backup_member VALUES(OLD.memberID, OLD.name, OLD.gender, OLD.memberAddress,
		OLD.memberPhone, OLD.memberEmail, OLD.mDate,'수정', CURDATE(),CURRENT_USER());
		
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
