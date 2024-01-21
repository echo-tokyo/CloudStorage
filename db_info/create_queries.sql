-- Create two users (trigger automatic create two profiles for these users)
INSERT INTO user (email, password, token) VALUES
	('ejyou.user@gmail.com', 'fredcv123', 'vw4hog5hvwirejfwk34t745twihw4gok5jowig5thwgo478'),
	('dudkovdy@gmail.com', 'qwerty123', 'vnrewioh4h3pp2f9hgbj3321i0w598gneiasoi34hgwkrfwsb');

-- Select all info about user
SELECT user.id, user.email, user.password, user.token, profile.nickname, profile.photo, user.created_at
FROM user INNER JOIN profile ON user.id=profile.user_id;

-- Create folders and files
INSERT INTO folder (user_id, name, parent_id) VALUES
	(1, 'my_docs', 1),
	(1, 'my_music', 1),
	(2, 'work', 2),
	(1, 'college', 3),
	(1, 'personal', 3),
	(2, 'general', 5);

INSERT INTO file (name, path, folder_id) VALUES
	('schedule', '/home/file1.txt', 6),
	('movies', '/home/movies_to_watch.txt', 7),
	('tz', '/home/my_tz.docx', 8);

-- Select folders
SELECT * FROM folder;
