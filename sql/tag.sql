CREATE TABLE tag(
	tag_name varchar(255),
    CONSTRAINT tag_pk PRIMARY KEY (tag_name)
);

CREATE TABLE post_tag(
	post_tag_id_text varchar(36),
	post_id varchar(36),
	tag_name varchar(255),
    PRIMARY KEY (post_tag_id_text)
);

CREATE TABLE comment_tag(
	comment_tag_id_text varchar(36),
	comment_id varchar(36),
	tag_name varchar(255),
    PRIMARY KEY (comment_tag_id_text)
);

CREATE TABLE user_follows_tag(
	user_follows_tag_id_text varchar(36),
	user_id varchar(36),
    tag_name varchar(255),
    PRIMARY KEY (user_follows_tag_id_text)
);

-- foreign keys
-- user_follows_tag references user.user_id
ALTER TABLE user_follows_tag 
	ADD FOREIGN KEY (user_id) REFERENCES user(user_id_text);

-- user_follows_tag references tag_tag_name    
ALTER TABLE user_follows_tag 
	ADD FOREIGN KEY (tag_name) REFERENCES tag(tag_name);
    
-- post_tag references rpost.post_id
ALTER TABLE post_tag 
	ADD FOREIGN KEY (post_id) REFERENCES post(post_id_text) ;

-- post_tag references tag.tag_name   
ALTER TABLE post_tag 
	ADD FOREIGN KEY (tag_name) REFERENCES tag(tag_name);

-- comment_tag references comment.comment_id_bin
ALTER TABLE comment_tag 
	ADD FOREIGN KEY (comment_id) REFERENCES comment(comment_id_text) ;
    
-- comment_tag references tag.tag_name
ALTER TABLE comment_tag 
	ADD FOREIGN KEY (tag_name) REFERENCES tag(tag_name);
    

