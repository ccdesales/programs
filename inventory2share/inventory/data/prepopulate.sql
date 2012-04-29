--CREATE TABLE "inv_unit" (
--    "id" integer NOT NULL PRIMARY KEY,
--    "name" varchar(50) NOT NULL,
--    "plural_name" varchar(50) NOT NULL
--);
INSERT INTO "inv_unit" VALUES(1,'Bag','Bags');
INSERT INTO "inv_unit" VALUES(2,'Bar','Bars');
INSERT INTO "inv_unit" VALUES(3,'Piece','Pieces');
--CREATE TABLE "inv_category" (
--    "id" integer NOT NULL PRIMARY KEY,
--    "name" varchar(50) NOT NULL
--);
INSERT INTO "inv_category" VALUES(1,'Dairy');
INSERT INTO "inv_category" VALUES(2,'Fruit');
INSERT INTO "inv_category" VALUES(3,'Dry Goods');
INSERT INTO "inv_category" VALUES(4,'Laundry');
INSERT INTO "inv_category" VALUES(5,'Vegetables');
--CREATE TABLE "inv_item" (
--    "id" integer NOT NULL PRIMARY KEY,
--    "category_id" integer NOT NULL REFERENCES "inv_category" ("id"),
--    "unit_id" integer NOT NULL REFERENCES "inv_unit" ("id"),
--    "name" varchar(50) NOT NULL,
--    "reorder_limit" integer
--);
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
--CREATE TABLE "inv_inventorytype" (
--    "id" integer NOT NULL PRIMARY KEY,
--    "name" varchar(20) NOT NULL
--);
INSERT INTO "inv_inventorytype" VALUES(1,'Simple');
INSERT INTO "inv_inventorytype" VALUES(2,'Detailed');
--CREATE TABLE "inv_inventory" (
--    "id" integer NOT NULL PRIMARY KEY,
--    "name" varchar(30) NOT NULL,
--    "ttype_id" integer NOT NULL REFERENCES "inv_inventorytype" ("id")
--);
