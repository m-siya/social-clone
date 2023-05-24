CREATE TABLE tag(
	tag_name varchar(255),
    CONSTRAINT tag_pk PRIMARY KEY (tag_name)
);

CREATE TABLE post_tag(
	post_id binary(16),
	tag_name varchar(255)
);

CREATE TABLE comment_tag(
	comment_id binary(16),
	tag_name varchar(255)
);

-- foreign keys
-- post_tag references repost.post_id
ALTER TABLE post_tag 
	ADD FOREIGN KEY (post_id) REFERENCES repost(post_id) ;

-- post_tag references tag.tag_name   
ALTER TABLE post_tag 
	ADD FOREIGN KEY (tag_name) REFERENCES tag(tag_name);

-- comment_tag references comment.comment_id_bin
ALTER TABLE comment_tag 
	ADD FOREIGN KEY (comment_id) REFERENCES comment(comment_id_bin) ;
    
-- comment_tag references tag.tag_name
ALTER TABLE comment_tag 
	ADD FOREIGN KEY (tag_name) REFERENCES tag(tag_name);
    

