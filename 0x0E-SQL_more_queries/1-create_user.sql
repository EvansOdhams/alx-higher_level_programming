sudo mysql -u root

-- Now you are in the MySQL shell
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'Diplomas19' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
