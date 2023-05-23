CREATE TABLE post(
	post_id int,
    created_on datetime DEFAULT current_timestamp,
    user_id int,
    likes int DEFAULT 0,
    content varchar(2000) NOT NULL,
    CONSTRAINT post_pk PRIMARY KEY (post_id)
);

-- reposts
CREATE TABLE repost (
	post_id int,
    reposted_from_user_id int,
    reposted_by_user_id int
);

-- foreign keys
-- post references user.user_id 
ALTER TABLE post 
	ADD FOREIGN KEY (user_id) REFERENCES user.user_id;

-- repost references post.post_id
ALTER TABLE repost 
	ADD FOREIGN KEY (post_id) REFERENCES post.post_id;
    
-- repost references user.user_id
ALTER TABLE repost 
	ADD FOREIGN KEY (reposted_from_user_id) REFERENCES user.user_id;
    
-- repost references user.user_id
ALTER TABLE post 
	ADD FOREIGN KEY (reposted_by_user_id) REFERENCES user.user_id;


    

    