CREATE TABLE post(
	post_id_bin binary(16),
	post_id_text varchar(36),
    created_on datetime DEFAULT current_timestamp,
    user_id varchar(36),
    likes int DEFAULT 0,
    content varchar(2000) NOT NULL,
    CONSTRAINT post_pk PRIMARY KEY (post_id_text)
);

-- reposts
CREATE TABLE repost (
	repost_id_text varchar(36),
	post_id varchar(36),
    reposted_from_user_id varchar(36),
    reposted_by_user_id varchar(36),
    CONSTRAINT repost_id_text PRIMARY KEY (repost_id_text)
);

CREATE TABLE post_likes(
	post_likes_id_text varchar(36),
	user_id varchar(36),
	post_id varchar(36),
    PRIMARY KEY (post_likes_id_text),
    FOREIGN KEY (user_id) REFERENCES user(user_id_text),
    FOREIGN KEY (post_id) REFERENCES post(post_id_text)
);

-- foreign keys
-- post references user.user_id_bin
ALTER TABLE post 
	ADD FOREIGN KEY (user_id) REFERENCES user(user_id_text);

-- repost references post.post_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (post_id) REFERENCES post(post_id_text);
    
-- repost references user.user_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (reposted_from_user_id) REFERENCES user(user_id_text);
    
-- repost references user.user_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (reposted_by_user_id) REFERENCES user(user_id_text);

-- functions
DELIMITER $$
CREATE FUNCTION add_post(user_id binary(16), content varchar(2000))  
RETURNS boolean deterministic
	BEGIN
		INSERT INTO post (post_id_bin, user_id, content) 
			VALUES (unhex(replace(uuid(),'-','')), user_id, content);
    return true;    
	END$$

CREATE FUNCTION remove_post(post_id binary(16)) 
RETURNS boolean deterministic
	BEGIN
		DELETE FROM post WHERE post_id_bin = post_id;
    return TRUE;    
	END$$    

-- like post functions
CREATE FUNCTION like_post(user_id binary(16), post_id binary(16))  
RETURNS boolean deterministic
	BEGIN
		INSERT INTO post_likes(user_id_bin, post_id_bin) 
			VALUES (user_id, post_id);
    return true;    
	END$$

CREATE FUNCTION unlike_post(user_id binary(16), post_id binary(16))
RETURNS boolean deterministic
	BEGIN
		DELETE FROM post_likes 
        WHERE post_id_bin = post_id AND user_id_bin = user_id;
    return TRUE;    
	END$$    

    