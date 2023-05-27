CREATE TABLE comment(
	comment_id_bin binary(16),
	comment_id_text varchar(36),
    post_id binary(16),
    user_id binary(16),
    likes int DEFAULT 0,
    content varchar(2000) NOT NULL,
    CONSTRAINT comment_pk PRIMARY KEY (comment_id_bin)
);

CREATE TABLE comment_likes(
	user_id binary(16),
	comment_id binary(16),
    PRIMARY KEY (user_id, comment_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id_bin),
    FOREIGN KEY (comment_id) REFERENCES comment(comment_id_bin)
);


-- foreign keys
-- comment references repost.reposted_by_user_id 
ALTER TABLE comment 
	ADD FOREIGN KEY (user_id) REFERENCES repost(reposted_by_user_id) ;

-- repost references post.post_id
ALTER TABLE comment
	ADD FOREIGN KEY (post_id) REFERENCES repost(post_id);
    
-- like comment functions
DELIMITER $$
CREATE FUNCTION like_comment(user_id binary(16), comment_id binary(16))  
RETURNS boolean deterministic
	BEGIN
		INSERT INTO comment_likes(user_id_bin, comment_id_bin) 
			VALUES (user_id, comment_id);
    return true;    
	END$$

CREATE FUNCTION unlike_comment(user_id binary(16), comment_id binary(16))
RETURNS boolean deterministic
	BEGIN
		DELETE FROM comment_likes 
        WHERE comment_id_bin = comment_id AND user_id_bin = user_id;
    return TRUE;    
	END$$ 