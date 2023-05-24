CREATE TABLE post(
	post_id_bin binary(16),
	post_id_text varchar(36) generated always as
        (insert(
			insert(
				insert(
					insert(hex(post_id_bin), 9, 0, '-'), 
					14,0,'-'), 
				19,0,'-'),
			24,0,'-')
		) virtual,
    created_on datetime DEFAULT current_timestamp,
    user_id binary(16),
    likes int DEFAULT 0,
    content varchar(2000) NOT NULL,
    CONSTRAINT post_pk PRIMARY KEY (post_id_bin)
);

-- reposts
CREATE TABLE repost (
	post_id binary(16),
    reposted_from_user_id binary(16),
    reposted_by_user_id binary(16)
);

CREATE TABLE post_likes(
	user_id binary(16),
	post_id binary(16),
    PRIMARY KEY (user_id, post_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id_bin),
    FOREIGN KEY (post_id) REFERENCES post(post_id_bin)
);

-- foreign keys
-- post references user.user_id_bin
ALTER TABLE post 
	ADD FOREIGN KEY (user_id) REFERENCES user(user_id_bin);

-- repost references post.post_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (post_id) REFERENCES post(post_id_bin);
    
-- repost references user.user_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (reposted_from_user_id) REFERENCES user(user_id_bin);
    
-- repost references user.user_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (reposted_by_user_id) REFERENCES user(user_id_bin);

-- functions
DELIMITER $$
CREATE FUNCTION add_post(user_id binary(16), content varchar(2000))  
RETURNS boolean
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

    