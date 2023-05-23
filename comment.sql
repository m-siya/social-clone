CREATE TABLE comment(
	comment_id int,
    post_id int,
    user_id int,
    likes int DEFAULT 0,
    content varchar(2000) NOT NULL,
    CONSTRAINT comment_pk PRIMARY KEY (comment_id)
);

-- foreign keys
-- comment references repost.reposted_by_user_id 
ALTER TABLE comment 
	ADD FOREIGN KEY (user_id) REFERENCES repost.reposted_by_user_id ;

-- repost references post.post_id
ALTER TABLE comment
	ADD FOREIGN KEY (post_id) REFERENCES repost.post_id;