-- This DB was used to test my DB schema!!! Finally DB was maked by Django


-- DATABASE --


-- create new database (if it doesn't exist)
CREATE DATABASE cloud_storage_clean_sql DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
-- Use the newly created database
USE cloud_storage_clean_sql;


-- TABLES --


-- Create the User table
CREATE TABLE IF NOT EXISTS user (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(150) NOT NULL,
	token VARCHAR(255) NULL,
	is_active BOOLEAN NOT NULL DEFAULT 1,
	is_staff BOOLEAN NOT NULL DEFAULT 0,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT user_id_pk PRIMARY KEY (id)
);
CREATE INDEX user_email_index ON user(email);

-- Create the Profile table
CREATE TABLE IF NOT EXISTS profile (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL UNIQUE,
	nickname VARCHAR(150) NOT NULL DEFAULT 'User',
	photo VARCHAR(255) NOT NULL DEFAULT '/path/to/photo.png',
	CONSTRAINT profile_id_pk PRIMARY KEY (id),
	CONSTRAINT profile_user_fk FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Create the Folder table
CREATE TABLE IF NOT EXISTS folder (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	name VARCHAR(50) NOT NULL,
	parent_id INT NULL,
	recycle_bin BOOLEAN NOT NULL DEFAULT 0,
	star BOOLEAN NOT NULL DEFAULT 0,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT folder_id_pk PRIMARY KEY (id),
	CONSTRAINT folder_user_fk FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
	CONSTRAINT folder_parent_id_fk FOREIGN KEY (parent_id) REFERENCES folder(id) ON DELETE CASCADE
);
CREATE INDEX folder_user_index ON folder(user_id);

-- Create the File table
CREATE TABLE IF NOT EXISTS file (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	size VARCHAR(20) NOT NULL,
	path VARCHAR(255) NOT NULL,
	folder_id INT NOT NULL,
	recycle_bin BOOLEAN NOT NULL DEFAULT 0,
	star BOOLEAN NOT NULL DEFAULT 0,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT file_id_pk PRIMARY KEY (id),
	CONSTRAINT file_folder_fk FOREIGN KEY (folder_id) REFERENCES folder(id) ON DELETE RESTRICT
);
CREATE INDEX file_user_index ON file(folder_id);


-- Create the Review table
CREATE TABLE IF NOT EXISTS review (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NULL,
	review_text TEXT NOT NULL,
	CONSTRAINT review_id_pk PRIMARY KEY (id),
    CONSTRAINT review_user_fk FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE SET NULL
);
CREATE INDEX review_user_index ON review(user_id);

-- TRIGGERS


-- Create the AddProfile trigger for adding profile for just created user
DELIMITER //
CREATE TRIGGER add_profile AFTER INSERT ON user
FOR EACH ROW BEGIN
	DECLARE inserted_id INT;
	SELECT NEW.id INTO inserted_id;

	INSERT INTO profile (user_id, nickname, photo) VALUES
		(inserted_id, CONCAT('User_', inserted_id), DEFAULT);
END;
//
DELIMITER ;


-- Create the AddRootFolder trigger for adding root folder for just created user
DELIMITER //
CREATE TRIGGER add_roop_folder AFTER INSERT ON user
FOR EACH ROW BEGIN
    DECLARE inserted_id INT;
    SELECT NEW.id INTO inserted_id;

    INSERT INTO folder (user_id, name) VALUES (inserted_id, '/');
END;
//
DELIMITER ;
