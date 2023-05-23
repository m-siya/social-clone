-- user table
CREATE TABLE user(
		user_id int NOT NULL,
        username varchar(30) NOT NULL UNIQUE,
        email varchar(255) NOT NULL UNIQUE,
        dob date,
        mobile varchar(255),
        password varchar(255) NOT NULL,
        CONSTRAINT user_pk PRIMARY KEY (user_id)
);

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



        
        