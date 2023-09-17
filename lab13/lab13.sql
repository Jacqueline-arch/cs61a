.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, MIN(smallest) FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b 
  where a.pet = b.pet and a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT seven FROM students AS a, numbers AS b where a.time = b.time and a.number = 7 and b.'7' = 'True';


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;

CREATE TABLE lowest_prices_helper AS
  SELECT name, MIN(MSRP/rating) FROM products GROUP BY category;
CREATE TABLE shopping_list AS
  SELECT name, store FROM lowest_prices_helper, lowest_prices where name = item;


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) FROM shopping_list AS a, stores AS b where a.store = b.store;

