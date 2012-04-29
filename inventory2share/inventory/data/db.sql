PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
INSERT INTO "auth_permission" VALUES(1,'Can add permission',1,'add_permission');
INSERT INTO "auth_permission" VALUES(2,'Can change permission',1,'change_permission');
INSERT INTO "auth_permission" VALUES(3,'Can delete permission',1,'delete_permission');
INSERT INTO "auth_permission" VALUES(4,'Can add group',2,'add_group');
INSERT INTO "auth_permission" VALUES(5,'Can change group',2,'change_group');
INSERT INTO "auth_permission" VALUES(6,'Can delete group',2,'delete_group');
INSERT INTO "auth_permission" VALUES(7,'Can add user',3,'add_user');
INSERT INTO "auth_permission" VALUES(8,'Can change user',3,'change_user');
INSERT INTO "auth_permission" VALUES(9,'Can delete user',3,'delete_user');
INSERT INTO "auth_permission" VALUES(10,'Can add message',4,'add_message');
INSERT INTO "auth_permission" VALUES(11,'Can change message',4,'change_message');
INSERT INTO "auth_permission" VALUES(12,'Can delete message',4,'delete_message');
INSERT INTO "auth_permission" VALUES(13,'Can add content type',5,'add_contenttype');
INSERT INTO "auth_permission" VALUES(14,'Can change content type',5,'change_contenttype');
INSERT INTO "auth_permission" VALUES(15,'Can delete content type',5,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(16,'Can add session',6,'add_session');
INSERT INTO "auth_permission" VALUES(17,'Can change session',6,'change_session');
INSERT INTO "auth_permission" VALUES(18,'Can delete session',6,'delete_session');
INSERT INTO "auth_permission" VALUES(19,'Can add site',7,'add_site');
INSERT INTO "auth_permission" VALUES(20,'Can change site',7,'change_site');
INSERT INTO "auth_permission" VALUES(21,'Can delete site',7,'delete_site');
INSERT INTO "auth_permission" VALUES(22,'Can add unit',8,'add_unit');
INSERT INTO "auth_permission" VALUES(23,'Can change unit',8,'change_unit');
INSERT INTO "auth_permission" VALUES(24,'Can delete unit',8,'delete_unit');
INSERT INTO "auth_permission" VALUES(25,'Can add category',9,'add_category');
INSERT INTO "auth_permission" VALUES(26,'Can change category',9,'change_category');
INSERT INTO "auth_permission" VALUES(27,'Can delete category',9,'delete_category');
INSERT INTO "auth_permission" VALUES(28,'Can add item',10,'add_item');
INSERT INTO "auth_permission" VALUES(29,'Can change item',10,'change_item');
INSERT INTO "auth_permission" VALUES(30,'Can delete item',10,'delete_item');
INSERT INTO "auth_permission" VALUES(31,'Can add inventory type',11,'add_inventorytype');
INSERT INTO "auth_permission" VALUES(32,'Can change inventory type',11,'change_inventorytype');
INSERT INTO "auth_permission" VALUES(33,'Can delete inventory type',11,'delete_inventorytype');
INSERT INTO "auth_permission" VALUES(34,'Can add inventory',12,'add_inventory');
INSERT INTO "auth_permission" VALUES(35,'Can change inventory',12,'change_inventory');
INSERT INTO "auth_permission" VALUES(36,'Can delete inventory',12,'delete_inventory');
INSERT INTO "auth_permission" VALUES(37,'Can add inventory entry',13,'add_inventoryentry');
INSERT INTO "auth_permission" VALUES(38,'Can change inventory entry',13,'change_inventoryentry');
INSERT INTO "auth_permission" VALUES(39,'Can delete inventory entry',13,'delete_inventoryentry');
INSERT INTO "auth_permission" VALUES(40,'Can add log entry',14,'add_logentry');
INSERT INTO "auth_permission" VALUES(41,'Can change log entry',14,'change_logentry');
INSERT INTO "auth_permission" VALUES(42,'Can delete log entry',14,'delete_logentry');
CREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
);
CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
CREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
);
CREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
);
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "password" varchar(128) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "is_superuser" bool NOT NULL,
    "last_login" datetime NOT NULL,
    "date_joined" datetime NOT NULL
);
INSERT INTO "auth_user" VALUES(1,'root','','','desales@pv.com','sha1$85c07$b94d1340a6cfe1b9e865b08033d022afa594bcf9',1,1,1,'2012-01-31 15:43:18.998000','2012-01-31 15:42:48.853000');
CREATE TABLE "auth_message" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "message" text NOT NULL
);
CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
INSERT INTO "django_content_type" VALUES(1,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(2,'group','auth','group');
INSERT INTO "django_content_type" VALUES(3,'user','auth','user');
INSERT INTO "django_content_type" VALUES(4,'message','auth','message');
INSERT INTO "django_content_type" VALUES(5,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(7,'site','sites','site');
INSERT INTO "django_content_type" VALUES(8,'unit','inv','unit');
INSERT INTO "django_content_type" VALUES(9,'category','inv','category');
INSERT INTO "django_content_type" VALUES(10,'item','inv','item');
INSERT INTO "django_content_type" VALUES(11,'inventory type','inv','inventorytype');
INSERT INTO "django_content_type" VALUES(12,'inventory','inv','inventory');
INSERT INTO "django_content_type" VALUES(13,'inventory entry','inv','inventoryentry');
INSERT INTO "django_content_type" VALUES(14,'log entry','admin','logentry');
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
INSERT INTO "django_session" VALUES('c7c5f0200b284bf0917171f357e7f9ad','MTI1ZDNjYzEwYWY1ZGNjY2U2NTRmMWM5ZWQzNTdmOTA5ZTdlZDEwYzqAAn1xAShVEl9hdXRoX3Vz
ZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED
VQ1fYXV0aF91c2VyX2lkcQRLAXUu
','2012-02-14 15:43:19.014000');
CREATE TABLE "django_site" (
    "id" integer NOT NULL PRIMARY KEY,
    "domain" varchar(100) NOT NULL,
    "name" varchar(50) NOT NULL
);
INSERT INTO "django_site" VALUES(1,'example.com','example.com');
CREATE TABLE "inv_unit" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "plural_name" varchar(50) NOT NULL
);
INSERT INTO "inv_unit" VALUES(1,'Bag','Bags');
INSERT INTO "inv_unit" VALUES(2,'Bar','Bars');
INSERT INTO "inv_unit" VALUES(3,'Piece','Pieces');
CREATE TABLE "inv_category" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL
);
INSERT INTO "inv_category" VALUES(1,'Dairy');
INSERT INTO "inv_category" VALUES(2,'Fruit');
INSERT INTO "inv_category" VALUES(3,'Dry Goods');
INSERT INTO "inv_category" VALUES(4,'Laundry');
INSERT INTO "inv_category" VALUES(5,'Vegetables');
CREATE TABLE "inv_item" (
    "id" integer NOT NULL PRIMARY KEY,
    "category_id" integer NOT NULL REFERENCES "inv_category" ("id"),
    "unit_id" integer NOT NULL REFERENCES "inv_unit" ("id"),
    "name" varchar(50) NOT NULL,
    "reorder_limit" integer unsigned
);
INSERT INTO "inv_item" VALUES(1,1,3,'Butter',NULL);
INSERT INTO "inv_item" VALUES(2,1,3,'Cheese',NULL);
INSERT INTO "inv_item" VALUES(3,1,3,'Eggs',NULL);
INSERT INTO "inv_item" VALUES(4,1,3,'Milk',NULL);
INSERT INTO "inv_item" VALUES(5,1,3,'Yogurt',NULL);
INSERT INTO "inv_item" VALUES(6,2,3,'Apples',NULL);
INSERT INTO "inv_item" VALUES(7,2,3,'Bananas',NULL);
INSERT INTO "inv_item" VALUES(8,2,3,'Blueberries',NULL);
INSERT INTO "inv_item" VALUES(9,2,3,'Melon',NULL);
INSERT INTO "inv_item" VALUES(10,1,3,'Oranges',NULL);
INSERT INTO "inv_item" VALUES(11,3,3,'Pasta',NULL);
INSERT INTO "inv_item" VALUES(12,3,3,'Rice',NULL);
INSERT INTO "inv_item" VALUES(13,3,3,'Bread Crumbs',NULL);
INSERT INTO "inv_item" VALUES(14,4,1,'Bleach',NULL);
INSERT INTO "inv_item" VALUES(15,4,1,'Detergent',NULL);
INSERT INTO "inv_item" VALUES(16,4,3,'Fabric Softener',NULL);
INSERT INTO "inv_item" VALUES(17,5,3,'Artichokes',NULL);
INSERT INTO "inv_item" VALUES(18,5,3,'Broccoli',NULL);
INSERT INTO "inv_item" VALUES(19,5,3,'Cabbage',NULL);
INSERT INTO "inv_item" VALUES(20,5,3,'Celery',NULL);
INSERT INTO "inv_item" VALUES(21,5,3,'Cucumbers',NULL);
INSERT INTO "inv_item" VALUES(22,5,3,'Garlic',NULL);
INSERT INTO "inv_item" VALUES(23,5,3,'Lettuce',NULL);
INSERT INTO "inv_item" VALUES(24,5,3,'Potatoes',NULL);
INSERT INTO "inv_item" VALUES(25,5,3,'Onions',NULL);
CREATE TABLE "inv_inventorytype" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(20) NOT NULL
);
INSERT INTO "inv_inventorytype" VALUES(1,'Simple');
INSERT INTO "inv_inventorytype" VALUES(2,'Detailed');
CREATE TABLE "inv_inventory" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "ttype_id" integer NOT NULL REFERENCES "inv_inventorytype" ("id")
);
CREATE TABLE "inv_inventoryentry" (
    "id" integer NOT NULL PRIMARY KEY,
    "item_id" integer NOT NULL REFERENCES "inv_item" ("id"),
    "inventory_id" integer NOT NULL REFERENCES "inv_inventory" ("id"),
    "isexist" bool NOT NULL,
    "isreorder" bool NOT NULL,
    "exist_quantity" integer unsigned,
    "reorder_quantity" integer unsigned
);
CREATE TABLE "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY,
    "action_time" datetime NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "content_type_id" integer REFERENCES "django_content_type" ("id"),
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint unsigned NOT NULL,
    "change_message" text NOT NULL
);
INSERT INTO "django_admin_log" VALUES(1,'2012-01-31 15:45:21.556000',1,9,'1','Dairy',1,'');
INSERT INTO "django_admin_log" VALUES(2,'2012-01-31 15:45:30.913000',1,9,'2','Fruit',1,'');
INSERT INTO "django_admin_log" VALUES(3,'2012-01-31 15:47:03.002000',1,9,'3','Dry Goods',1,'');
INSERT INTO "django_admin_log" VALUES(4,'2012-01-31 15:47:14.812000',1,9,'4','Laundry',1,'');
INSERT INTO "django_admin_log" VALUES(5,'2012-01-31 15:48:13.776000',1,9,'5','Vegetables',1,'');
INSERT INTO "django_admin_log" VALUES(6,'2012-01-31 15:49:20.674000',1,11,'1','Simple',1,'');
INSERT INTO "django_admin_log" VALUES(7,'2012-01-31 15:49:28.363000',1,11,'2','Detailed',1,'');
INSERT INTO "django_admin_log" VALUES(8,'2012-01-31 15:50:27.516000',1,8,'1','Bag',1,'');
INSERT INTO "django_admin_log" VALUES(9,'2012-01-31 15:50:32.276000',1,8,'2','Bar',1,'');
INSERT INTO "django_admin_log" VALUES(10,'2012-01-31 15:51:11.095000',1,8,'3','Piece',1,'');
INSERT INTO "django_admin_log" VALUES(11,'2012-01-31 15:51:15.016000',1,10,'1','Butter',1,'');
INSERT INTO "django_admin_log" VALUES(12,'2012-01-31 15:51:24.060000',1,10,'2','Cheese',1,'');
INSERT INTO "django_admin_log" VALUES(13,'2012-01-31 15:51:34.880000',1,10,'3','Eggs',1,'');
INSERT INTO "django_admin_log" VALUES(14,'2012-01-31 15:51:47.969000',1,10,'4','Milk',1,'');
INSERT INTO "django_admin_log" VALUES(15,'2012-01-31 15:52:00.600000',1,10,'5','Yogurt',1,'');
INSERT INTO "django_admin_log" VALUES(16,'2012-01-31 15:52:12.796000',1,10,'6','Apples',1,'');
INSERT INTO "django_admin_log" VALUES(17,'2012-01-31 15:52:21.175000',1,10,'7','Bananas',1,'');
INSERT INTO "django_admin_log" VALUES(18,'2012-01-31 15:52:30.244000',1,10,'8','Blueberries',1,'');
INSERT INTO "django_admin_log" VALUES(19,'2012-01-31 15:54:26.095000',1,10,'9','Melon',1,'');
INSERT INTO "django_admin_log" VALUES(20,'2012-01-31 15:54:34.785000',1,10,'10','Oranges',1,'');
INSERT INTO "django_admin_log" VALUES(21,'2012-01-31 15:55:08.727000',1,10,'11','Pasta',1,'');
INSERT INTO "django_admin_log" VALUES(22,'2012-01-31 15:55:42.202000',1,10,'12','Rice',1,'');
INSERT INTO "django_admin_log" VALUES(23,'2012-01-31 15:55:58.141000',1,10,'13','Bread Crumbs',1,'');
INSERT INTO "django_admin_log" VALUES(24,'2012-01-31 15:56:11.746000',1,10,'14','Bleach',1,'');
INSERT INTO "django_admin_log" VALUES(25,'2012-01-31 15:56:21.398000',1,10,'15','Detergent',1,'');
INSERT INTO "django_admin_log" VALUES(26,'2012-01-31 15:56:34.317000',1,10,'16','Fabric Softener',1,'');
INSERT INTO "django_admin_log" VALUES(27,'2012-01-31 15:56:46.942000',1,10,'17','Artichokes',1,'');
INSERT INTO "django_admin_log" VALUES(28,'2012-01-31 15:56:54.763000',1,10,'18','Broccoli',1,'');
INSERT INTO "django_admin_log" VALUES(29,'2012-01-31 15:57:02.193000',1,10,'19','Cabbage',1,'');
INSERT INTO "django_admin_log" VALUES(30,'2012-01-31 15:57:09.558000',1,10,'20','Celery',1,'');
INSERT INTO "django_admin_log" VALUES(31,'2012-01-31 15:57:17.433000',1,10,'21','Cucumbers',1,'');
INSERT INTO "django_admin_log" VALUES(32,'2012-01-31 15:57:26.291000',1,10,'22','Garlic',1,'');
INSERT INTO "django_admin_log" VALUES(33,'2012-01-31 15:57:36.985000',1,10,'23','Lettuce',1,'');
INSERT INTO "django_admin_log" VALUES(34,'2012-01-31 15:57:46.876000',1,10,'24','Potatoes',1,'');
INSERT INTO "django_admin_log" VALUES(35,'2012-01-31 15:57:53.548000',1,10,'25','Onions',1,'');
CREATE INDEX "auth_permission_1bb8f392" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_425ae3c4" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_1e014c8f" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_user_permissions_403f60f" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_1e014c8f" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_403f60f" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_425ae3c4" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_message_403f60f" ON "auth_message" ("user_id");
CREATE INDEX "django_session_3da3d3d8" ON "django_session" ("expire_date");
CREATE INDEX "inv_item_42dc49bc" ON "inv_item" ("category_id");
CREATE INDEX "inv_item_cac2c6" ON "inv_item" ("unit_id");
CREATE INDEX "inv_inventory_6ad6c501" ON "inv_inventory" ("ttype_id");
CREATE INDEX "inv_inventoryentry_67b70d25" ON "inv_inventoryentry" ("item_id");
CREATE INDEX "inv_inventoryentry_7214473" ON "inv_inventoryentry" ("inventory_id");
CREATE INDEX "django_admin_log_403f60f" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_1bb8f392" ON "django_admin_log" ("content_type_id");
COMMIT;
