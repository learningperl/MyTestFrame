/*
Navicat MySQL Data Transfer

Source Server         : 2G-Will
Source Server Version : 50722
Source Host           : 112.74.191.10:3306
Source Database       : test_project

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-08-08 16:55:19
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `id` int(8) unsigned NOT NULL AUTO_INCREMENT COMMENT 'userid',
  `nickname` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '昵称',
  `describe` varchar(128) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '个人介绍',
  `username` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pwd` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
  PRIMARY KEY (`id`,`username`),
  UNIQUE KEY `username` (`username`) USING BTREE,
  UNIQUE KEY `password` (`username`,`pwd`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('1', 'Will_Testing', '擅长Python、Java自动化开发；是特斯汀学院最可爱的老师', 'Will', '123456');
INSERT INTO `userinfo` VALUES ('2', '土匪老师', '一个狂野的技术型男，当一个土匪有文化有技术，你懂的！', '土匪', 'tufei');
INSERT INTO `userinfo` VALUES ('3', '青鸿', '一个才华与美貌并存的男子。才华已经比脸还大咯', '青鸿', 'qinghong');
INSERT INTO `userinfo` VALUES ('4', '卡卡', '一个帅气的小伙子', '卡卡', 'kaka');