/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE = @@TIME_ZONE */;
/*!40103 SET TIME_ZONE = '+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;

DROP TABLE IF EXISTS `beaten`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `beaten` (
  `id`        INT(11)      NOT NULL AUTO_INCREMENT,
  `timestamp` TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `article`   VARCHAR(256) NOT NULL,
  `diff`      VARCHAR(512) NOT NULL,
  `user`      VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `beaten` WRITE;
/*!40000 ALTER TABLE `beaten`
  DISABLE KEYS */;
INSERT INTO `beaten` VALUES
  (1, '2010-10-27 07:46:51', 'MainTable tennis', 'http://en.wikipedia.org/w/index.php?diff=393159117&oldid=393158834',
   ''),
  (2, '2010-10-27 07:48:11', 'MainStarfish', 'http://en.wikipedia.org/w/index.php?diff=393159248&oldid=393131604', ''),
  (3, '2010-10-27 07:48:12', 'MainHealth', 'http://en.wikipedia.org/w/index.php?diff=393159250&oldid=392809441', ''),
  (4, '2010-10-27 07:48:13', 'MainFantastic', 'http://en.wikipedia.org/w/index.php?diff=393159251&oldid=387813481', ''),
  (5, '2010-10-27 07:54:34', 'MainSaffron terror', 'http://en.wikipedia.org/w/index.php?diff=393159967&oldid=390088525', ''),
  (6, '2010-10-27 10:01:38', 'Finite set', 'http://en.wikipedia.org/w/index.php?diff=393175004&oldid=384866071', 'ClueBot'),
  (7, '2010-10-27 13:42:17', '1920s', 'http://en.wikipedia.org/w/index.php?diff=393206139&oldid=392069031', 'ClueBot'),
  (8, '2010-10-27 13:43:40', 'SM Supermalls', 'http://en.wikipedia.org/w/index.php?diff=393206465&oldid=392806332', 'ClueBot'),
  (9, '2010-10-27 20:39:51', 'Subject complement', 'http://en.wikipedia.org/w/index.php?diff=393285034&oldid=393284850', ''),
  (10, '2010-10-27 20:41:22', 'Michael Cera', 'http://en.wikipedia.org/w/index.php?diff=393285372&oldid=393260211', 'Philip Trueman'),
  (11, '2010-10-27 21:59:11', 'Urolagnia', 'http://en.wikipedia.org/w/index.php?diff=393299817&oldid=392544653', ''),
  (12, '2010-10-27 21:59:28', 'Anacaona', 'http://en.wikipedia.org/w/index.php?diff=393299865&oldid=391513485', ''),
  (13, '2010-10-27 21:59:33', 'Modernism', 'http://en.wikipedia.org/w/index.php?diff=393299825&oldid=393117270', ''),
  (14, '2010-10-28 10:40:51', 'Xavier Thompson', 'http://en.wikipedia.org/w/index.php?diff=393398071&oldid=393397793', ''),
  (15, '2010-10-28 23:41:56', 'Iroquois', 'http://en.wikipedia.org/w/index.php?diff=393518575&oldid=393462012', 'ClueBot'),
  (16, '2010-10-28 23:42:20', 'Common Mudpuppy', 'http://en.wikipedia.org/w/index.php?diff=393518632&oldid=393492925', 'ClueBot'),
  (17, '2010-10-29 02:45:59', 'Longfields-Davidson Heights Secondary School', 'http://en.wikipedia.org/w/index.php?diff=393541815&oldid=392678011', 'ClueBot'),
  (18, '2010-10-29 03:18:03', 'Roman', 'http://en.wikipedia.org/w/index.php?diff=393545514&oldid=393189978', 'ClueBot'),
  (19, '2010-10-29 03:19:19', 'Four (drink)', 'http://en.wikipedia.org/w/index.php?diff=393545657&oldid=393543180', 'ClueBot'),
  (20, '2010-10-29 03:20:00', 'Tiananmen Square', 'http://en.wikipedia.org/w/index.php?diff=393545736&oldid=393545656', 'ClueBot'),
  (21, '2010-10-29 04:30:54', 'Panic disorder', 'http://en.wikipedia.org/w/index.php?diff=393552677&oldid=392325143', 'ClueBot'),
  (22, '2010-11-02 18:40:32', 'Cyanobacteria', 'http://en.wikipedia.org/w/index.php?diff=394423495&oldid=394423039', 'Caltas'),
  (23, '2010-11-02 18:49:28', 'Chromium', 'http://en.wikipedia.org/w/index.php?diff=394425109&oldid=393441195', 'ClueBot'),
  (24, '2010-11-02 18:53:54', 'Djimi Traoré', 'http://en.wikipedia.org/w/index.php?diff=394426003&oldid=393286198', 'ClueBot'),
  (25, '2010-11-02 19:37:38', 'Javier Willy', 'http://en.wikipedia.org/w/index.php?diff=394433645&oldid=394429904', 'Javier willy wiki'),
  (26, '2010-11-02 19:39:48', 'Drake & Josh', 'http://en.wikipedia.org/w/index.php?diff=394434023&oldid=394415245', 'ClueBot'),
  (27, '2010-11-02 19:48:36', 'Women\'s suffrage', 'http://en.wikipedia.org/w/index.php?diff=394436522&oldid=394431861', 'ClueBot'),
  (28, '2010-11-02 19:48:42', 'Columbidae', 'http://en.wikipedia.org/w/index.php?diff=394436600&oldid=394436487', 'PIGEONSTEELE'),
  (29, '2010-11-02 19:58:30', 'The Magic Flute', 'http://en.wikipedia.org/w/index.php?diff=394438500&oldid=394437264', 'ClueBot'),
  (30, '2010-11-02 20:18:27', 'Joe Montana', 'http://en.wikipedia.org/w/index.php?diff=394442049&oldid=394425103', 'ClueBot'),
  (31, '2010-11-02 20:20:26', 'Marilyn Monroe', 'http://en.wikipedia.org/w/index.php?diff=394442441&oldid=394273187', 'ClueBot'),
  (32, '2010-11-02 20:41:35', 'Alaska', 'http://en.wikipedia.org/w/index.php?diff=394446469&oldid=394446101', 'Wayne Olajuwon'),
  (33, '2010-11-02 21:17:47', 'Andrew Carnegie', 'http://en.wikipedia.org/w/index.php?diff=394452881&oldid=394450649', 'Caltas'),
  (34, '2010-11-02 21:21:10', 'Tanzania', 'http://en.wikipedia.org/w/index.php?diff=394453453&oldid=394452362', 'Caltas'),
  (35, '2010-11-02 21:22:26', 'Tea Party movement', 'http://en.wikipedia.org/w/index.php?diff=394453638&oldid=394451813', 'Alpha Quadrant (alt)'),
  (36, '2010-11-02 21:26:54', 'Hernando de Soto', 'http://en.wikipedia.org/w/index.php?diff=394454519&oldid=394453700', 'Caltas'),
  (37, '2010-11-02 21:52:26', 'Idaho', 'http://en.wikipedia.org/w/index.php?diff=394459202&oldid=394313828', 'Elassint'),
  (38, '2010-11-02 22:45:28', 'Neurosurgery', 'http://en.wikipedia.org/w/index.php?diff=394468741&oldid=394140129', 'ClueBot'),
  (39, '2010-11-02 23:10:40', 'Pica (disorder)', 'http://en.wikipedia.org/w/index.php?diff=394473111&oldid=394423474', 'ClueBot'),
  (40, '2010-11-02 23:32:25', 'Light-emitting diode', 'http://en.wikipedia.org/w/index.php?diff=394476813&oldid=394406642', 'ClueBot'),
  (41, '2010-11-02 23:41:17', 'Terry Fox', 'http://en.wikipedia.org/w/index.php?diff=394478353&oldid=394470823', 'Ruy Pugliesi'),
  (42, '2010-11-02 23:42:05', 'Play Radio', 'http://en.wikipedia.org/w/index.php?diff=394478543&oldid=376249896',
   'ClueBot'),
  (43, '2010-11-02 23:48:25', 'List of countries by population',
   'http://en.wikipedia.org/w/index.php?diff=394479704&oldid=394479322', 'ClueBot'),
  (44, '2010-11-02 23:57:54', 'Handicap', 'http://en.wikipedia.org/w/index.php?diff=394481477&oldid=374818122',
   'ClueBot'),
  (45, '2010-11-03 00:00:39', 'Cytoplasm', 'http://en.wikipedia.org/w/index.php?diff=394482006&oldid=394053486',
   'ClueBot'),
  (46, '2010-11-03 00:02:54', 'Voluntary association',
   'http://en.wikipedia.org/w/index.php?diff=394482477&oldid=391473012', 'ClueBot'),
  (47, '2010-11-03 00:10:18', 'Coal', 'http://en.wikipedia.org/w/index.php?diff=394483869&oldid=394262114', 'Slon02'),
  (48, '2010-11-03 00:15:48', 'Cherokee', 'http://en.wikipedia.org/w/index.php?diff=394484943&oldid=394316694',
   'Slon02'),
  (49, '2010-11-03 00:19:50', 'Métis people (Canada)',
   'http://en.wikipedia.org/w/index.php?diff=394485756&oldid=390425233', 'Slon02'),
  (50, '2010-11-03 00:21:44', 'Charles I of England',
   'http://en.wikipedia.org/w/index.php?diff=394486039&oldid=394291197', 'Slon02');
/*!40000 ALTER TABLE `beaten`
  ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `cluster_node`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cluster_node` (
  `node` VARCHAR(256) NOT NULL,
  `type` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`type`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = latin1;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `commentid` INT(11)      NOT NULL AUTO_INCREMENT,
  `revertid`  INT(11)      NOT NULL,
  `timestamp` TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `userid`    INT(11)      NOT NULL,
  `user`      VARCHAR(128) NOT NULL,
  `comment`   TEXT         NOT NULL,
  PRIMARY KEY (`commentid`),
  KEY `revertid` (`revertid`),
  KEY `userid` (`userid`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments`
  DISABLE KEYS */;
INSERT INTO `comments` VALUES
  (2, 12345, '2010-12-08 05:28:15', -1, 'Anonymous2',
   'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tellus mi, ornare at pellentesque nec, eleifend ut felis. Pellentesque lorem libero, sollicitudin at ultricies interdum, ultrices non nunc. Duis in sapien ac mauris tempus tristique. Integer enim urna, imperdiet quis blandit nec, congue in purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce in mauris eget libero feugiat luctus. Vestibulum risus lorem, sodales non ullamcorper ut, lobortis at sapien. Morbi nec ante leo. Ut iaculis tempus risus imperdiet porta. Quisque tristique viverra enim id placerat. Ut egestas congue lacus. Morbi id tortor sit amet ante vulputate tristique. Proin purus lacus, rutrum a luctus non, feugiat quis risus. Etiam fermentum placerat porttitor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer suscipit ultrices est at rhoncus.\r\n\r\nEtiam commodo dapibus erat vitae interdum. Donec sem dui, pharetra vel ornare ut, aliquam ac arcu. Donec sem ligula, posuere et iaculis id, sollicitudin vitae mi. Vestibulum sed odio libero, vitae ultricies purus. Nullam euismod pellentesque sem ac vehicula. Sed est arcu, condimentum eget semper nec, vulputate at sapien. Phasellus in erat ac leo congue interdum sed quis libero. Sed mattis sodales arcu, eget ullamcorper mauris adipiscing et. Duis cursus laoreet rhoncus. Quisque mi metus, posuere sed dignissim sed, convallis et nisi. Nulla facilisi. Nam non lectus in nunc mollis eleifend at a tortor. Nullam vel orci sapien, imperdiet feugiat purus. Pellentesque scelerisque sapien sit amet urna rutrum pulvinar. Suspendisse iaculis, magna nec posuere pharetra, neque augue congue risus, non pharetra nulla leo quis mi. Etiam urna felis, rutrum ut aliquet at, pulvinar ut enim. Pellentesque euismod tellus sit amet lorem fermentum sed lacinia nisl tempus. Nunc leo ligula, commodo sed elementum at, cursus non eros. Nunc pharetra accumsan libero id sagittis. Suspendisse id lacus vel ipsum viverra porta in at elit.\r\n\r\nCras feugiat, urna hendrerit placerat ultricies, quam diam imperdiet neque, ut lacinia massa tortor non arcu. Donec et diam tellus. Etiam varius auctor quam, a rhoncus purus malesuada et. Aenean in elit odio. Nulla facilisi. Donec a nulla et arcu venenatis scelerisque. Quisque in bibendum diam. Quisque et bibendum massa. In orci dolor, blandit id congue vel, eleifend nec lectus. Nulla porttitor massa et odio interdum faucibus. Phasellus varius vehicula neque, et tristique erat faucibus id. Nam placerat nulla sit amet nunc placerat nec condimentum nibh porta. Maecenas hendrerit nibh ac nisi tincidunt mollis. Vestibulum sed odio eu erat pharetra pharetra. Mauris vel nibh semper elit hendrerit fermentum. Sed vel arcu orci, eget lobortis arcu. Nulla vestibulum consectetur est ut accumsan. Vestibulum consequat ultrices vehicula.\r\n\r\nNullam vehicula velit vel velit tincidunt condimentum. Proin porta lectus quis tellus adipiscing ut cursus neque euismod. Nulla congue gravida convallis. Sed ut lectus ligula. Mauris convallis, lacus quis vulputate tristique, nibh dui faucibus ipsum, ut convallis enim felis sit amet elit. Donec sit amet vulputate tellus. Etiam nec orci rutrum orci ultrices aliquam. Sed tempus scelerisque urna at dictum. Sed eget lacus molestie leo sodales pellentesque et a leo. Curabitur fermentum erat in libero bibendum consectetur. Morbi ut massa id mi ultrices gravida. Cras et mauris metus, sit amet rhoncus tortor. Curabitur laoreet facilisis fermentum. Pellentesque imperdiet lacus vel turpis dignissim vestibulum. Duis tincidunt leo eget libero dapibus tincidunt.\r\n\r\nSuspendisse sed posuere quam. Aliquam facilisis ligula vel elit adipiscing a molestie nibh scelerisque. Duis id eros non nisl gravida dapibus. Praesent tortor elit, pellentesque a volutpat id, dapibus varius augue. Proin ac nulla non mi vestibulum pharetra. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis at est ligula, a posuere purus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin fringilla purus vel purus porta ut vulputate mi pellentesque. Mauris ultrices venenatis molestie. Proin pharetra ligula ut velit sagittis dictum. Etiam a aliquam ligula.'),
  (3, 13652, '2010-12-08 06:14:22', -1, 'Anonymous', 'It was a mistake.'),
  (4, 13652, '2010-12-08 06:14:37', -1, 'Anonymous', 'This is another comment.'),
  (5, 13652, '2010-12-08 06:14:51', -1, 'Cobi', 'This is even more of a comment.'),
  (6, 13652, '2010-12-08 20:51:58', -1, 'Anonymous', 'Mistake, yeah, right.'),
  (7, 13652, '2010-12-08 20:53:03', -1, 'HK',
   'Who doesn\'t like smell of poo in the morning? Obviously, good faith edit.'),
  (8, 12345, '2010-12-08 22:29:42', 1, 'Cobi', 'This is another test.'),
  (9, 12345, '2010-12-08 22:53:48', -2, 'System', 'Cobi has marked this report as \"Invalid\".'),
  (10, 12345, '2010-12-08 22:54:39', -2, 'System', 'Cobi has marked this report as \"Deferred to Review Interface\".');
/*!40000 ALTER TABLE `comments`
  ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reports` (
  `revertid`   INT(11)      NOT NULL,
  `timestamp`  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `reporterid` INT(11)      NOT NULL,
  `reporter`   VARCHAR(128) NOT NULL,
  `status`     INT(11)      NOT NULL,
  PRIMARY KEY (`revertid`),
  KEY `reporterid` (`reporterid`),
  KEY `status` (`status`),
  CONSTRAINT `reports_ibfk_1` FOREIGN KEY (`revertid`) REFERENCES `vandalism` (`id`)
    ON DELETE CASCADE
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `reports` WRITE;
/*!40000 ALTER TABLE `reports`
  DISABLE KEYS */;
INSERT INTO `reports`
VALUES
  (15, '2016-04-23 19:52:41', -1, 'Anonymous', 1), (20, '2015-05-30 14:09:00', -1, 'Pubes', 2),
  (25, '2015-06-07 10:57:57', -1, 'Anonymous', 1),
  (42, '2015-01-26 22:41:44', -1, '<a href=http://www.bbc.co.uk/news/magazine-18892510>http://www.bbc.co.uk/news/magazine-18892510</a>', 1),
  (69, '2014-10-02 12:54:03', -1, 'Anonymous', 1), (352, '2016-05-15 15:12:53', -1, 'Anonymous', 1),
  (435, '2012-05-12 14:37:15', -1, 'Greg', 1), (3453, '2015-06-07 11:03:53', -1, 'VIETNAM', 1),
  (12345, '2010-12-09 01:27:38', -1, 'Anonymous', 1), (12663, '2015-10-22 22:46:21', -1, 'Bradley', 0),
  (13548, '2010-12-09 00:38:01', -1, 'Anonymous', 1), (13579, '2015-01-26 22:42:21', -1, 'Anonamos', 1),
  (13652, '2010-12-09 01:13:12', -1, 'Anonymous', 1), (15719, '2013-02-19 18:32:33', -1, 'Anonymous', 5),
  (18044, '2012-09-02 01:03:07', -1, 'Import Script', 4), (18956, '2012-05-12 14:38:10', -1, 'Anonymous', 1),
  (28062, '2010-12-17 03:25:47', 8, 'Logan', 1), (34974, '2015-01-26 22:43:05', -1, 'chloe', 2),
  (34998, '2010-12-18 01:21:11', -1, 'Import Script', 7), (36506, '2015-01-26 22:43:16', -1, 'Anonymous', 2),
  (44363, '2010-12-18 05:41:30', -1, 'Import Script', 7), (45604, '2010-12-17 06:07:01', -1, 'Import Script', 7),
  (45613, '2010-12-09 01:13:23', -1, 'Anonymous', 1), (46513, '2010-12-17 06:22:18', -1, 'Import Script', 7);
/*!40000 ALTER TABLE `reports`
  ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userid`         INT(11)      NOT NULL AUTO_INCREMENT,
  `username`       VARCHAR(128) NOT NULL,
  `password`       VARCHAR(128) NOT NULL,
  `email`          VARCHAR(128) NOT NULL,
  `admin`          TINYINT(1)   NOT NULL,
  `superadmin`     TINYINT(1)   NOT NULL,
  `next_on_review` TINYINT(1)            DEFAULT '0',
  PRIMARY KEY (`userid`),
  UNIQUE KEY `username` (`username`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users`
  DISABLE KEYS */;
INSERT INTO `users` VALUES (-2, 'System', '', 'SYSTEM', 1, 1, 0),
  (1, 'Cobi', '', 'xxx@xxx.xxx', 1, 1, 0),
  (2, 'crispy', '', 'xxx@xxx.xxx', 0, 1, 0),
  (3, 'SnoFox', '', 'xxx@xxx.xxx', 0, 0, 0),
  (4, 'A930913', '', 'xxx@xxx.xxx', 1, 0, 0),
  (5, 'rsshaw', '', 'xxx@xxx.xxx', 0, 0, 0),
  (6, 'Damian', '', 'xxx@xxx.xxx', 1, 1, 1);
/*!40000 ALTER TABLE `users`
  ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `vandalism`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vandalism` (
  `id`        INT(11)      NOT NULL AUTO_INCREMENT,
  `timestamp` TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user`      VARCHAR(256) NOT NULL,
  `article`   VARCHAR(256) NOT NULL,
  `heuristic` VARCHAR(64)  NOT NULL,
  `regex`     VARCHAR(2048)         DEFAULT NULL,
  `reason`    VARCHAR(512) NOT NULL,
  `diff`      VARCHAR(512) NOT NULL,
  `old_id`    INT(11)      NOT NULL,
  `new_id`    INT(11)      NOT NULL,
  `reverted`  TINYINT(1)   NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `vandalism` WRITE;
/*!40000 ALTER TABLE `vandalism`
  DISABLE KEYS */;
INSERT INTO `vandalism` VALUES
  (1, '2010-10-27 07:37:06', 'Reader7664', 'MainJennifer González', '', NULL, 'ANN scored at 0.966318',
      'http://en.wikipedia.org/w/index.php?diff=393158009&oldid=393116897', 393116897, 393158009, 0),
  (2, '2010-10-27 07:40:30', '141.31.148.2', 'MainFast food', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393158426&oldid=393158335', 393158335, 393158426, 0),
  (3, '2010-10-27 07:45:02', '84.55.222.4', 'MainIslamic calendar', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393158916&oldid=391999008', 391999008, 393158916, 0),
  (4, '2010-10-27 07:45:31', '75.166.160.135', 'MainJudy Greer', '', NULL, 'ANN scored at 0.98827', 'http://en.wikipedia.org/w/index.php?diff=393158972&oldid=393158812', 393158812, 393158972, 0),
  (5, '2010-10-27 07:46:21', '117.194.201.105', 'MainTriboelectric effect', '', NULL, 'ANN scored at 0.961966', 'http://en.wikipedia.org/w/index.php?diff=393159061&oldid=383708612', 383708612, 393159061, 0),
  (6, '2010-10-27 07:46:51', '82.204.12.2', 'MainTable tennis', '', NULL, 'ANN scored at 0.956871', 'http://en.wikipedia.org/w/index.php?diff=393159117&oldid=393158834', 393158834, 393159117, 0),
  (7, '2016-05-01 23:56:14', '82.204.12.2', 'MainTable tennis', '', NULL, 'ANN scored at 0.96383', 'http://en.wikipedia.org/w/index.php?diff=393159209&oldid=393159126', 393159126, 393159209, 1),
  (8, '2010-10-27 07:48:11', '202.162.102.94', 'MainStarfish', '', NULL, 'ANN scored at 0.98009', 'http://en.wikipedia.org/w/index.php?diff=393159248&oldid=393131604', 393131604, 393159248, 0),
  (9, '2010-10-27 07:48:12', '58.178.64.233', 'MainHealth', '', NULL, 'ANN scored at 0.981494', 'http://en.wikipedia.org/w/index.php?diff=393159250&oldid=392809441', 392809441, 393159250, 0),
  (10, '2016-04-26 03:01:03', '85.15.230.182', 'MainFantastic', '', NULL, 'ANN scored at 0.930727', 'http://en.wikipedia.org/w/index.php?diff=393159251&oldid=387813481', 387813481, 393159251, 1),
  (11, '2010-10-27 07:48:31', '121.216.140.164', 'MainGondwana', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393159279&oldid=392783341', 392783341, 393159279, 0),
  (12, '2010-10-27 07:54:34', '59.92.15.95', 'MainSaffron terror', '', NULL, 'ANN scored at 0.959595', 'http://en.wikipedia.org/w/index.php?diff=393159967&oldid=390088525', 390088525, 393159967, 0),
  (13, '2010-10-27 08:04:17', '110.55.67.129', 'Arko', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393161214&oldid=381426453', 381426453, 393161214, 1),
  (14, '2010-10-27 08:04:43', '84.19.165.214', 'Rambha (actress)', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393161277&oldid=392856453', 392856453, 393161277, 1),
  (15, '2010-10-27 08:06:04', '82.204.12.2', 'Table tennis', '', NULL, 'ANN scored at 0.976651', 'http://en.wikipedia.org/w/index.php?diff=393161467&oldid=393161444', 393161444, 393161467, 1),
  (16, '2010-10-27 08:07:05', '110.55.67.129', 'Arko', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393161600&oldid=393161303', 393161303, 393161600, 0),
  (17, '2010-10-27 08:07:06', '84.28.191.142', 'Earl Hudson', '', NULL, 'ANN scored at 0.957308', 'http://en.wikipedia.org/w/index.php?diff=393161599&oldid=393019566', 393019566, 393161599, 1),
  (18, '2010-10-27 08:07:29', '121.96.132.233', 'Powerpuff Girls Z', '', NULL, 'ANN scored at 0.99173', 'http://en.wikipedia.org/w/index.php?diff=393161647&oldid=393060738', 393060738, 393161647, 0),
  (19, '2010-10-27 08:07:45', '220.239.120.214', 'Ryde Secondary College', '', NULL, 'ANN scored at 0.952752', 'http://en.wikipedia.org/w/index.php?diff=393161682&oldid=384187716', 384187716, 393161682, 1),
  (20, '2010-10-27 08:09:07', '80.179.7.161', 'Detection dog', '', NULL, 'ANN scored at 0.970839', 'http://en.wikipedia.org/w/index.php?diff=393161866&oldid=392849869', 392849869, 393161866, 1),
  (21, '2010-10-27 08:09:09', '87.186.62.112', 'Thylakoid', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393161872&oldid=393148651', 393148651, 393161872, 1),
  (22, '2010-10-27 08:09:57', '59.101.105.30', 'Katie Holmes', '', NULL, 'ANN scored at 0.959981', 'http://en.wikipedia.org/w/index.php?diff=393161971&oldid=393160709', 393160709, 393161971, 1),
  (23, '2010-10-27 08:10:21', '112.121.55.9', 'Flow network', '', NULL, 'ANN scored at 0.951409', 'http://en.wikipedia.org/w/index.php?diff=393162014&oldid=392940194', 392940194, 393162014, 1),
  (24, '2010-10-27 08:10:29', '110.33.173.11', 'Agnes Sampson', '', NULL, 'ANN scored at 0.992165', 'http://en.wikipedia.org/w/index.php?diff=393162032&oldid=369337899', 369337899, 393162032, 1),
  (25, '2010-10-27 08:10:31', '121.52.145.101', 'Grammatical conjunction', '', NULL, 'ANN scored at 0.952567', 'http://en.wikipedia.org/w/index.php?diff=393162039&oldid=393151362', 393151362, 393162039, 1),
  (26, '2010-10-27 08:11:36', '129.255.237.218', 'Glenbard East High School', '', NULL, 'ANN scored at 0.977481', 'http://en.wikipedia.org/w/index.php?diff=393162162&oldid=388041416', 388041416, 393162162, 1),
  (27, '2010-10-27 08:11:40', '99.31.228.11', 'The Revenge of the Shadow King', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393162169&oldid=390550315', 390550315, 393162169, 1),
  (28, '2010-10-27 08:12:25', '41.72.161.79', 'Biofuel', '', NULL, 'ANN scored at 0.973468', 'http://en.wikipedia.org/w/index.php?diff=393162264&oldid=393116907', 393116907, 393162264, 1),
  (29, '2010-10-27 08:12:27', 'Sujeetkrana', 'Classified advertising', '', NULL, 'ANN scored at 0.966379', 'http://en.wikipedia.org/w/index.php?diff=393162270&oldid=393162115', 393162115, 393162270, 1),
  (30, '2010-10-27 08:12:57', '122.106.104.9', 'Ben Hall (bushranger)', '', NULL, 'ANN scored at 0.979845', 'http://en.wikipedia.org/w/index.php?diff=393162331&oldid=393162171', 393162171, 393162331, 1),
  (31, '2010-10-27 08:12:57', '173.16.179.147', 'Dead Rising 2', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393162333&oldid=393097770', 393097770, 393162333, 1),
  (32, '2010-10-27 08:14:16', '122.106.104.9', 'Ben Hall (bushranger)', '', NULL, 'ANN scored at 1', 'http://en.wikipedia.org/w/index.php?diff=393162487&oldid=393162331', 393162331, 393162487, 0),
  (33, '2010-10-27 08:15:25', '74.190.14.221', 'Matt Diaz', '', NULL, 'ANN scored at 0.985815', 'http://en.wikipedia.org/w/index.php?diff=393162600&oldid=393162186', 393162186, 393162600, 1),
  (34, '2010-10-27 08:15:28', '74.196.112.37', 'Major League Baseball', '', NULL, 'ANN scored at 0.994178', 'http://en.wikipedia.org/w/index.php?diff=393162603&oldid=393134733', 393134733, 393162603, 1),
  (35, '2010-10-27 08:15:58', 'CiaranLinehan', 'Rosaleen Linehan', '', NULL, 'ANN scored at 0.953863', 'http://en.wikipedia.org/w/index.php?diff=393162661&oldid=391343451', 391343451, 393162661, 1),
  (36, '2010-10-27 08:16:05', '41.95.8.7', 'Star (classification)', '', NULL, 'ANN scored at 0.9662', 'http://en.wikipedia.org/w/index.php?diff=393162674&oldid=392425915', 392425915, 393162674, 1),
  (37, '2010-10-27 08:16:08', '129.255.237.218', 'Carl Sandburg High School', '', NULL, 'ANN scored at 0.983517', 'http://en.wikipedia.org/w/index.php?diff=393162680&oldid=392672944', 392672944, 393162680, 1),
  (38, '2010-10-27 08:16:11', '89.106.161.10', 'Constitutional monarchy', '', NULL, 'ANN scored at 0.960658', 'http://en.wikipedia.org/w/index.php?diff=393162688&oldid=393156153', 393156153, 393162688, 1),
  (39, '2010-10-27 08:16:42', '202.125.130.163', 'Heat treatment', '', NULL, 'ANN scored at 0.968055', 'http://en.wikipedia.org/w/index.php?diff=393162733&oldid=390475721', 390475721, 393162733, 1),
  (40, '2010-10-27 08:16:57', '110.36.52.79', 'Silica fume', '', NULL, 'ANN scored at 0.965678', 'http://en.wikipedia.org/w/index.php?diff=393162771&oldid=387924172', 387924172, 393162771, 1),
  (41, '2010-10-27 08:16:57', '202.56.124.129', 'Sikar district', '', NULL, 'ANN scored at 0.949436', 'http://en.wikipedia.org/w/index.php?diff=393162772&oldid=387600152', 387600152, 393162772, 1),
  (42, '2010-10-27 08:17:04', '202.59.76.115', 'Chiniotis', '', NULL, 'ANN scored at 1',
       'http://en.wikipedia.org/w/index.php?diff=393162792&oldid=391363014', 391363014, 393162792, 1),
  (43, '2010-10-27 08:17:05', '122.106.104.9', 'Ben Hall (bushranger)', '', NULL, 'ANN scored at 0.951919',
       'http://en.wikipedia.org/w/index.php?diff=393162798&oldid=393162487', 393162487, 393162798, 0),
  (44, '2010-10-27 08:17:08', '207.216.16.101', 'Genius', '', NULL, 'ANN scored at 0.976824',
       'http://en.wikipedia.org/w/index.php?diff=393162809&oldid=393162623', 393162623, 393162809, 1),
  (45, '2010-10-27 08:17:45', '110.174.203.217', 'Messy Little Raindrops', '', NULL, 'ANN scored at 0.960146',
       'http://en.wikipedia.org/w/index.php?diff=393162869&oldid=393021260', 393021260, 393162869, 1),
  (46, '2010-10-27 08:18:15', 'CiaranLinehan', 'Rosaleen Linehan', '', NULL, 'ANN scored at 0.953889',
       'http://en.wikipedia.org/w/index.php?diff=393162926&oldid=393162726', 393162726, 393162926, 0),
  (47, '2010-10-27 08:18:31', '92.82.172.157', 'Ximena Navarrete', '', NULL, 'ANN scored at 1',
       'http://en.wikipedia.org/w/index.php?diff=393162954&oldid=392642061', 392642061, 393162954, 1),
  (48, '2010-10-27 08:18:38', 'Sujeetkrana', 'Classified information', '', NULL, 'ANN scored at 0.966854',
       'http://en.wikipedia.org/w/index.php?diff=393162965&oldid=393062570', 393062570, 393162965, 1),
  (49, '2010-10-27 08:19:02', 'Sujeetkrana', 'Classified information', '', NULL, 'ANN scored at 0.962278',
       'http://en.wikipedia.org/w/index.php?diff=393163005&oldid=393162965', 393162965, 393163005, 0),
  (50, '2010-10-27 08:20:05', 'Special Cases', 'Genius', '', NULL, 'ANN scored at 1',
       'http://en.wikipedia.org/w/index.php?diff=393163130&oldid=393163119', 393163119, 393163130, 1);
/*!40000 ALTER TABLE `vandalism`
  ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE = @OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;