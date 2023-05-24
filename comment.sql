CREATE TABLE comment(
	comment_id_bin binary(16),
	comment_id_text varchar(36) generated always as
        (insert(
			insert(
				insert(
					insert(hex(comment_id_bin), 9, 0, '-'), 
					14,0,'-'), 
				19,0,'-'),
			24,0,'-')
		) virtual,
    post_id binary(16),
    user_id binary(16),
    likes int DEFAULT 0,
    content varchar(2000) NOT NULL,
    CONSTRAINT comment_pk PRIMARY KEY (comment_id_bin)
);

-- foreign keys
-- comment references repost.reposted_by_user_id 
ALTER TABLE comment 
	ADD FOREIGN KEY (user_id) REFERENCES repost.reposted_by_user_id ;

-- repost references post.post_id
ALTER TABLE comment
	ADD FOREIGN KEY (post_id) REFERENCES repost.post_id;