/*
Navicat MySQL Data Transfer

Source Server         : cfsfine
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : student_management_system

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2020-04-18 22:43:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 学生
-- ----------------------------
DROP TABLE IF EXISTS `学生`;
CREATE TABLE `学生` (
  `学号` varchar(255) NOT NULL,
  `班级号` varchar(255) DEFAULT NULL,
  `姓名` varchar(255) DEFAULT NULL,
  `性别` varchar(255) DEFAULT NULL,
  `年龄` int(255) DEFAULT NULL,
  `系号` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`学号`),
  KEY `name` (`姓名`) USING BTREE,
  KEY `dn2` (`系号`),
  KEY `cn1` (`班级号`),
  CONSTRAINT `cn1` FOREIGN KEY (`班级号`) REFERENCES `班级` (`班级号`) ON DELETE SET NULL ON UPDATE SET NULL,
  CONSTRAINT `dn2` FOREIGN KEY (`系号`) REFERENCES `院系` (`系号`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 学生
-- ----------------------------
INSERT INTO `学生` VALUES ('1170300101', '1703001', '张思', '男', '21', '00013');
INSERT INTO `学生` VALUES ('1170300102', '1703001', '高晋鹏', '男', '22', '00013');
INSERT INTO `学生` VALUES ('1170300103', '1703001', '王五', '男', '20', '00013');
INSERT INTO `学生` VALUES ('1170300104', '1703001', '王竹', '女', '21', '00013');
INSERT INTO `学生` VALUES ('1170300105', '1703001', '李丽', '女', '21', '00013');
INSERT INTO `学生` VALUES ('1170300201', '1703002', '李亚伟', '男', '21', '00014');
INSERT INTO `学生` VALUES ('1170300202', '1703002', '高春', '女', '21', '00014');
INSERT INTO `学生` VALUES ('1170300203', '1703002', '王鹏', '男', '21', '00014');
INSERT INTO `学生` VALUES ('1170300204', '1703002', '赵海生', '男', '21', '00014');
INSERT INTO `学生` VALUES ('1170300205', '1703002', '李涯之', '男', '21', '00014');
INSERT INTO `学生` VALUES ('1170300206', '1703002', '陈佳丽', '女', '21', '00014');
INSERT INTO `学生` VALUES ('1170300207', '1703002', '何丽', '女', '21', '00014');
INSERT INTO `学生` VALUES ('1170300301', null, '陈逢深', '男', '21', '00013');

-- ----------------------------
-- Table structure for 学生成绩
-- ----------------------------
DROP TABLE IF EXISTS `学生成绩`;
CREATE TABLE `学生成绩` (
  `学号` varchar(255) NOT NULL,
  `课号` varchar(255) NOT NULL,
  `成绩` double(255,2) DEFAULT NULL,
  PRIMARY KEY (`学号`,`课号`),
  KEY `con1` (`课号`),
  KEY `sn1` (`学号`) USING BTREE,
  CONSTRAINT `con1` FOREIGN KEY (`课号`) REFERENCES `课程` (`课号`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sn1` FOREIGN KEY (`学号`) REFERENCES `学生` (`学号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 学生成绩
-- ----------------------------
INSERT INTO `学生成绩` VALUES ('1170300101', '10001', '56.00');
INSERT INTO `学生成绩` VALUES ('1170300101', '10003', '75.33');
INSERT INTO `学生成绩` VALUES ('1170300102', '10001', '78.33');
INSERT INTO `学生成绩` VALUES ('1170300102', '10003', '62.54');
INSERT INTO `学生成绩` VALUES ('1170300103', '10001', '65.98');
INSERT INTO `学生成绩` VALUES ('1170300103', '10003', '92.54');
INSERT INTO `学生成绩` VALUES ('1170300104', '10001', '76.88');
INSERT INTO `学生成绩` VALUES ('1170300104', '10003', '54.23');
INSERT INTO `学生成绩` VALUES ('1170300105', '10001', '79.86');
INSERT INTO `学生成绩` VALUES ('1170300105', '10003', '78.69');
INSERT INTO `学生成绩` VALUES ('1170300201', '10002', '54.31');
INSERT INTO `学生成绩` VALUES ('1170300201', '10004', '51.01');
INSERT INTO `学生成绩` VALUES ('1170300202', '10002', '93.24');
INSERT INTO `学生成绩` VALUES ('1170300202', '10004', '98.21');
INSERT INTO `学生成绩` VALUES ('1170300203', '10002', '93.44');
INSERT INTO `学生成绩` VALUES ('1170300203', '10004', '91.98');
INSERT INTO `学生成绩` VALUES ('1170300204', '10002', '49.34');
INSERT INTO `学生成绩` VALUES ('1170300204', '10004', '60.78');
INSERT INTO `学生成绩` VALUES ('1170300205', '10002', '65.78');
INSERT INTO `学生成绩` VALUES ('1170300205', '10004', '78.34');
INSERT INTO `学生成绩` VALUES ('1170300206', '10002', '86.28');
INSERT INTO `学生成绩` VALUES ('1170300206', '10004', '88.65');
INSERT INTO `学生成绩` VALUES ('1170300207', '10002', '85.23');
INSERT INTO `学生成绩` VALUES ('1170300207', '10004', '68.32');

-- ----------------------------
-- Table structure for 教师
-- ----------------------------
DROP TABLE IF EXISTS `教师`;
CREATE TABLE `教师` (
  `教师编号` varchar(255) NOT NULL,
  `系号` varchar(255) DEFAULT NULL,
  `姓名` varchar(255) DEFAULT NULL,
  `性别` varchar(255) DEFAULT NULL,
  `年龄` int(255) DEFAULT NULL,
  PRIMARY KEY (`教师编号`),
  KEY `name` (`姓名`),
  KEY `dn1` (`系号`),
  CONSTRAINT `dn1` FOREIGN KEY (`系号`) REFERENCES `院系` (`系号`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 教师
-- ----------------------------
INSERT INTO `教师` VALUES ('00001', '00013', '程间', '男', '39');
INSERT INTO `教师` VALUES ('00002', '00014', '邓雅雯', '女', '37');
INSERT INTO `教师` VALUES ('00003', '00013', '王丽媛', '女', '54');
INSERT INTO `教师` VALUES ('00004', '00014', '赵刚', '男', '29');
INSERT INTO `教师` VALUES ('00005', '00013', '陈逢深', '男', '34');

-- ----------------------------
-- Table structure for 班级
-- ----------------------------
DROP TABLE IF EXISTS `班级`;
CREATE TABLE `班级` (
  `班级号` varchar(255) NOT NULL,
  `人数` int(255) DEFAULT NULL,
  PRIMARY KEY (`班级号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 班级
-- ----------------------------
INSERT INTO `班级` VALUES ('1703001', '5');
INSERT INTO `班级` VALUES ('1703002', '7');

-- ----------------------------
-- Table structure for 班级成绩
-- ----------------------------
DROP TABLE IF EXISTS `班级成绩`;
CREATE TABLE `班级成绩` (
  `班级号` varchar(255) NOT NULL,
  `课号` varchar(255) NOT NULL,
  `平均成绩` double(255,2) DEFAULT NULL,
  `不及格人数` int(255) DEFAULT NULL,
  PRIMARY KEY (`课号`,`班级号`),
  KEY `cn2` (`班级号`),
  KEY `con2` (`课号`) USING BTREE,
  CONSTRAINT `cn2` FOREIGN KEY (`班级号`) REFERENCES `班级` (`班级号`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `con2` FOREIGN KEY (`课号`) REFERENCES `课程` (`课号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 班级成绩
-- ----------------------------
INSERT INTO `班级成绩` VALUES ('1703001', '10001', '71.41', '1');
INSERT INTO `班级成绩` VALUES ('1703002', '10002', '75.37', '2');
INSERT INTO `班级成绩` VALUES ('1703001', '10003', '72.67', '1');
INSERT INTO `班级成绩` VALUES ('1703002', '10004', '76.76', '1');

-- ----------------------------
-- Table structure for 课程
-- ----------------------------
DROP TABLE IF EXISTS `课程`;
CREATE TABLE `课程` (
  `课号` varchar(255) NOT NULL,
  `课程名` varchar(255) DEFAULT NULL,
  `教师编号` varchar(255) DEFAULT NULL,
  `学分` double(255,1) DEFAULT NULL,
  `学时` int(255) DEFAULT NULL,
  `系号` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`课号`),
  KEY `name` (`课程名`),
  KEY `tn1` (`教师编号`),
  KEY `dn3` (`系号`),
  CONSTRAINT `dn3` FOREIGN KEY (`系号`) REFERENCES `院系` (`系号`) ON DELETE SET NULL ON UPDATE SET NULL,
  CONSTRAINT `tn1` FOREIGN KEY (`教师编号`) REFERENCES `教师` (`教师编号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 课程
-- ----------------------------
INSERT INTO `课程` VALUES ('10001', '自然语言处理', '00003', '45.0', '64', '00013');
INSERT INTO `课程` VALUES ('10002', '计算建模', '00002', '3.0', '48', '00014');
INSERT INTO `课程` VALUES ('10003', '信息检索', '00001', '3.5', '52', '00013');
INSERT INTO `课程` VALUES ('10004', '高级算法', '00004', '4.5', '64', '00014');

-- ----------------------------
-- Table structure for 辅导员
-- ----------------------------
DROP TABLE IF EXISTS `辅导员`;
CREATE TABLE `辅导员` (
  `系号` varchar(255) NOT NULL,
  `辅导员编号` varchar(255) NOT NULL,
  `姓名` varchar(255) DEFAULT NULL,
  `性别` varchar(255) DEFAULT NULL,
  `电话` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`系号`,`辅导员编号`),
  KEY `name` (`姓名`),
  KEY `dn4` (`系号`) USING BTREE,
  CONSTRAINT `dn4` FOREIGN KEY (`系号`) REFERENCES `院系` (`系号`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 辅导员
-- ----------------------------
INSERT INTO `辅导员` VALUES ('00013', '00001', '夏威', '男', '13199449255');
INSERT INTO `辅导员` VALUES ('00013', '00002', '邓超', '男', '18981010370');
INSERT INTO `辅导员` VALUES ('00014', '00001', '王丽', '女', '18981010730');

-- ----------------------------
-- Table structure for 院系
-- ----------------------------
DROP TABLE IF EXISTS `院系`;
CREATE TABLE `院系` (
  `系号` varchar(255) NOT NULL,
  `学院名` varchar(255) DEFAULT NULL,
  `系名` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`系号`),
  KEY `dna` (`系名`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 院系
-- ----------------------------
INSERT INTO `院系` VALUES ('00013', '计算机学院', '自然语言处理');
INSERT INTO `院系` VALUES ('00014', '计算机学院', '计算机科学');

-- ----------------------------
-- View structure for 学生成绩（姓名）
-- ----------------------------
DROP VIEW IF EXISTS `学生成绩（姓名）`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `学生成绩（姓名）` AS select `学生`.`系号` AS `系号`,`学生`.`班级号` AS `班级号`,`学生`.`学号` AS `学号`,`学生`.`姓名` AS `姓名`,`学生成绩`.`课号` AS `课号`,`课程`.`课程名` AS `课程名`,`学生成绩`.`成绩` AS `成绩` from ((`学生` join `学生成绩` on((`学生成绩`.`学号` = `学生`.`学号`))) join `课程` on((`学生成绩`.`课号` = `课程`.`课号`))) ;

-- ----------------------------
-- View structure for 教师教授课程
-- ----------------------------
DROP VIEW IF EXISTS `教师教授课程`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `教师教授课程` AS select `课程`.`课号` AS `课号`,`课程`.`课程名` AS `课程名`,`教师`.`教师编号` AS `教师编号`,`教师`.`姓名` AS `姓名` from (`课程` join `教师` on((`课程`.`教师编号` = `教师`.`教师编号`))) ;

-- ----------------------------
-- View structure for 院系辅导员联系方式
-- ----------------------------
DROP VIEW IF EXISTS `院系辅导员联系方式`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `院系辅导员联系方式` AS select `院系`.`学院名` AS `学院名`,`院系`.`系名` AS `系名`,`辅导员`.`辅导员编号` AS `辅导员编号`,`辅导员`.`姓名` AS `姓名`,`辅导员`.`电话` AS `电话` from (`院系` join `辅导员` on((`辅导员`.`系号` = `院系`.`系号`))) ;
DROP TRIGGER IF EXISTS `class_num+`;
DELIMITER ;;
CREATE TRIGGER `class_num+` AFTER INSERT ON `学生` FOR EACH ROW begin
 update 班级
 set 人数 = (select count(*) from 学生 where 学生.班级号 = 班级.班级号);
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `class_num-`;
DELIMITER ;;
CREATE TRIGGER `class_num-` AFTER DELETE ON `学生` FOR EACH ROW begin
 update 班级
 set 人数 = (select count(*) from 学生 where 学生.班级号 = 班级.班级号);
end
;;
DELIMITER ;
