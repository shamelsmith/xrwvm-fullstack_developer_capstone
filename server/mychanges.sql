BEGIN;
--
-- Create model CarMake
--
CREATE TABLE "djangoapp_carmake" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "description" text NOT NULL);
--
-- Create model CarModel
--
CREATE TABLE "djangoapp_carmodel" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "dealer_id" integer NULL, "name" varchar(100) NOT NULL, "type" varchar(10) NOT NULL, "year" integer NOT NULL, "car_make_id" bigint NOT NULL REFERENCES "djangoapp_carmake" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "djangoapp_carmodel_car_make_id_8851cef1" ON "djangoapp_carmodel" ("car_make_id");
COMMIT;
