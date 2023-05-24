-- user table
-- the final result is a string with the format of a UUID
--  (Universally Unique Identifier), represented as
--  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, where x represents a 
--  hexadecimal digit.

CREATE TABLE user(
		user_id_bin binary(16),
        user_id_text varchar(36) generated always as
        (insert(
			insert(
				insert(
					insert(hex(user_id_bin), 9, 0, '-'), 
					14,0,'-'), 
				19,0,'-'),
			24,0,'-')
		) virtual,
        username varchar(30) NOT NULL UNIQUE,
        email varchar(255) NOT NULL UNIQUE,
        dob date,
        mobile varchar(255),
        password varchar(255) NOT NULL,
        CONSTRAINT user_pk PRIMARY KEY (user_id_bin)
);

-- insert into user (user_id_bin,username, email, password)
--   values(unhex(replace(uuid(),'-','')), 'Andromeda', 'andr', 'andr');
--   
-- select user_id_text, username from user; 
 
CREATE TABLE user_follows_tag(
	user_id int,
    tag_name varchar(255)
);

-- foreign keys
-- user_follows_tag references user.user_id
ALTER TABLE user_follows_tag 
	ADD FOREIGN KEY (user_id) REFERENCES user.user_id;

-- user_follows_tag references tag_tag_name    
ALTER TABLE user_follows_tag 
	ADD FOREIGN KEY (tag_name) REFERENCES tag.tag_name;



        
        