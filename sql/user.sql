-- user table
-- the final result is a string with the format of a UUID
--  (Universally Unique Identifier), represented as
--  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, where x represents a 
--  hexadecimal digit.

CREATE TABLE user(
		user_id_bin binary(16),
        user_id_text varchar(36),
        username varchar(30) NOT NULL UNIQUE,
        email varchar(255) NOT NULL UNIQUE,
        dob date,
        mobile varchar(255),
        password varchar(255) NOT NULL,
        CONSTRAINT user_pk PRIMARY KEY (user_id_text)
);

-- insert into user (user_id_bin,username, email, password)
--   values(unhex(replace(uuid(),'-','')), 'Andromeda', 'andr', 'andr');
--   
-- select user_id_text, username from user; 
 


-- functions
DELIMITER $$
CREATE FUNCTION create_user(username varchar(30), email varchar(255), password varchar(255))  
RETURNS boolean deterministic
	BEGIN
		INSERT INTO user (user_id_bin, username, email, password) 
			VALUES (unhex(replace(uuid(),'-','')), username, email, md5(password));
    return true;    
	END$$
    
CREATE FUNCTION add_dob(user_id binary(16), dob date)
RETURNS boolean deterministic
	BEGIN
		UPDATE user 
		SET dob = dob 
        WHERE user_id_bin = user_id;
	return true;
	END $$

CREATE FUNCTION add_mobile(user_id binary(16), mobile varchar(255))
RETURNS boolean deterministic
	BEGIN
		UPDATE user 
		SET mobile = mobile
        WHERE user_id_bin = user_id;
	return true;
	END $$

		



        
        