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

-- foreign keys
-- post references user.user_id_bin
ALTER TABLE post 
	ADD FOREIGN KEY (user_id) REFERENCES user.user_id_bin;

-- repost references post.post_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (post_id) REFERENCES post.post_id_bin;
    
-- repost references user.user_id_bin
ALTER TABLE repost 
	ADD FOREIGN KEY (reposted_from_user_id) REFERENCES user.user_id_bin;
    
-- repost references user.user_id_bin
ALTER TABLE post 
	ADD FOREIGN KEY (reposted_by_user_id) REFERENCES user.user_id_bin;


    

    