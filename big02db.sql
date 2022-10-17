-- Cau lenh SQL de tao Database 'big02db'
-- Cau lenh SQL de tao Tables: Students, Subjects, Scores

DROP DATABASE IF EXISTS big02db;
CREATE DATABASE IF NOT EXISTS big02db;
USE big02db;

DROP TABLE IF EXISTS Students;
CREATE TABLE IF NOT EXISTS Students (
	`Code` VARCHAR(6),
    FullName NVARCHAR(25) NOT NULL,
    BirthDay DATETIME NOT NULL,
    Sex ENUM('0', '1') NOT NULL,
    `Address` NVARCHAR(250),
    Phone VARCHAR(10) UNIQUE, 
    Email VARCHAR(250) UNIQUE,
    PRIMARY KEY (Code),
    CHECK (`Code` LIKE 'PY%' AND LENGTH(Code) = 6 AND `Code` = UPPER(`Code`)),
    CHECK (BirthDay < sysdate()),
    CHECK (LENGTH(Phone) = 10)
);

DROP TABLE IF EXISTS Subjects;
CREATE TABLE IF NOT EXISTS Subjects (
	`Code` VARCHAR(5),
    `Name` NVARCHAR(25) NOT NULL UNIQUE,
    PRIMARY KEY (Code),
    CHECK (`Code` LIKE 'SUB%' AND LENGTH(Code) = 5 AND `Code` = UPPER(`Code`)) 

DROP TABLE IF EXISTS Scores;
CREATE TABLE IF NOT EXISTS Scores (
	StudentCode VARCHAR(6) NOT NULL,
    SubjectCode VARCHAR(5) NOT NULL,
    ProcessScore FLOAT NOT NULL,
    FinalTestScore FLOAT NOT NULL,
	PRIMARY KEY (StudentCode, SubjectCode),
    FOREIGN KEY (StudentCode) REFERENCES Students (Code) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (SubjectCode) REFERENCES Subjects (Code) ON DELETE CASCADE ON UPDATE CASCADE
);