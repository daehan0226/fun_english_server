schema="""
CREATE TABLE IF NOT EXISTS `user` (
    `id`                    INT(11) NOT NULL AUTO_INCREMENT,
    `name`                  VARCHAR(12) UNIQUE,
    `email`                 VARCHAR(100),
    `password`              VARCHAR(200) NOT NULL,
    `salt`                  VARCHAR(20) NOT NULL,
    `user_type`             INT(3) DEFAULT 2,
    `login_counting`        INT(5) DEFAULT 0,
    `create_datetime`       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `update_datetime`       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `verb` (
    `id`                    INT(11) NOT NULL AUTO_INCREMENT,
    `present`               VARCHAR(50) UNIQUE,
    `past`                  VARCHAR(50),
    `participle`            VARCHAR(50),
    `is_irregular`          INT(3),
    `learn_level`           INT(3),
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `sentence` (
    `id`                 INT(11) NOT NULL AUTO_INCREMENT,
    `text`               VARCHAR(200) UNIQUE,
    `learn_level`        INT(3),
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `verb_sentence` (
    `id`              INT(11) NOT NULL AUTO_INCREMENT,
    `verb_id`         INT(11),
    `sentence_id`     INT(11),
    PRIMARY KEY(`id`, `verb_id`, `sentence_id`),
    CONSTRAINT FOREIGN KEY (`verb_id`) REFERENCES `fun_english`.`verb` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (`sentence_id`) REFERENCES `fun_english`.`sentence` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);
"""

# CREATE TABLE IF NOT EXISTS `session` (
#     `id`                    INT(11) NOT NULL AUTO_INCREMENT,
#     `user_id`               INT(11) NOT NULL,
#     `token`                 VARCHAR(100) NOT NULL,
#     `last_call_datetime`    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY(`id`,`user_id`,`token`),
#     CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `task_tracker`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS `task_group` (
#     `id`                    INT(11) NOT NULL AUTO_INCREMENT,
#     `title`                 VARCHAR(50),
#     `text`                  VARCHAR(200),
#     `repeat_type`           INT(3) DEFAULT 0,
#     `user_id`               INT(11) NOT NULL,
#     `selected_date`         TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `end_date`              TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `create_datetime`       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `update_datetime`       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY(`id`),
#     CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `task_tracker`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS `task` (
#     `id`                    INT(11) NOT NULL AUTO_INCREMENT,
#     `group_id`              INT(11),
#     `checked`               INT(3) DEFAULT 0,
#     `datetime`              TIMESTAMP NOT NULL,
#     PRIMARY KEY(`id`),
#     CONSTRAINT FOREIGN KEY (`group_id`) REFERENCES `task_tracker`.`task_group` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS `link` (
#     `id`                    INT(11) NOT NULL AUTO_INCREMENT,
#     `url`                   VARCHAR(1000),
#     `description`           VARCHAR(200),
#     `image_url`             VARCHAR(1000),
#     `user_id`               INT(11) NOT NULL,
#     PRIMARY KEY(`id`),
#     CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `task_tracker`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
# );

# CREATE TABLE IF NOT EXISTS `task_group_link` (
#     `id`                    INT(11) NOT NULL AUTO_INCREMENT,
#     `task_group_id`         INT(11),
#     `link_id`               INT(11),
#     PRIMARY KEY(`id`, `task_group_id`, `link_id`),
#     CONSTRAINT FOREIGN KEY (`task_group_id`) REFERENCES `task_tracker`.`task_group` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
#     CONSTRAINT FOREIGN KEY (`link_id`) REFERENCES `task_tracker`.`link` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
# );
