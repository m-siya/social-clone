CREATE TABLE follower (
	follower_id_text varchar(36),
	user_id varchar(36),
    is_followed_by_id varchar(36),
    PRIMARY KEY (follower_id_text),
    FOREIGN KEY (user_id) REFERENCES user(user_id_text),
    FOREIGN KEY (is_followed_by_id) REFERENCES user(user_id_text)
);

DELIMITER $$
CREATE FUNCTION add_follower(user_id binary(16), follower_id binary(16)) 
RETURNS boolean deterministic
	BEGIN
		INSERT INTO follower(user_id, follower_id) VALUES (user_id, follower_id);
    return true;    
	END$$

CREATE FUNCTION remove_follower(user_id binary(16), follower_id binary(16)) 
RETURNS boolean deterministic
	BEGIN
		DELETE FROM follower WHERE user_id = user_id AND follower_id = follower_id;
    return TRUE;    
	END$$

CREATE PROCEDURE get_followers(user_id binary(16)) 
	BEGIN
		CREATE TABLE followers AS SELECT follower_id FROM follower WHERE user_id = user_id;
	END$$

    