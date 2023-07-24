CREATE USER 'dba'@'localhost' 
	IDENTIFIED BY 'password';
    

CREATE USER 'api'@'localhost'
		IDENTIFIED BY 'password';

CREATE DATABASE social_clone
	DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci; 
    
USE social_clone;
    
CREATE ROLE 'api_role', 'developer_role';

GRANT ALL privileges on social_clone.* TO 'developer_role';
GRANT ALL PRIVILEGES ON social_clone.* TO 'dba'@'localhost';

-- GRANT CONNECT ON DATABASE social_demo TO social_demo_api_role;
-- GRANT USAGE ON SCHEMA PUBLIC TO social_demo_api_role;

GRANT 'developer_role' TO 'dba'@'localhost';
GRANT 'api_role' TO 'api'@'localhost';


