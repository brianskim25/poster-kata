#importing  necessary packages
import swapi
import mysql.connector as mysql
import random
import decimal
import string

#connecting to the mysql salesdb database located in the mysqlDB container
db = mysql.connect(
    #the host is db since that is how it was initialized from the docker-compose.yml file
    host='db',
    user='user',
    password='mySQLuser!@',
    database='salesdb',
    port='3306',
    #using the correct authentication plugin since mysql_native_password is not the default
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

letters = string.ascii_lowercase
promo_code_list = ('radio','online','fan','textmsg','friend')

#creating an insert query to be used for the salesdb.Sales table
query_insert = "INSERT INTO salesdb.Sales (sales_id, poster_content, quantity, price, email, sales_rep, promo_code, poster_type, poster_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sales_id_people = 1

#loop for inserting people data to salesdb.Sales table
people = swapi.get_all('people')
for v in people.iter():
    poster_content = v.name
    #randomly assign a quantity between 1 and 10 (inclusive)
    quantity = random.randint(1,10)
    #random assign a price between 1.0 and 9.9 (inclusive)
    price = float(decimal.Decimal(random.randrange(10, 99))/10)
    #randomly assign a customer email
    #with 10 lowercase letters and append @gmail.com
    #(better logic can be written here to place more realistc fake customer emails)
    email = ''.join(random.choice(letters) for i in range(10))+'@gmail.com'
    #randomly assign a sales_rep email
    #with 10 lowercase letters and append @swposters.com
    #(better logic can be written here to place more realistc fake sales_rep emails)
    sales_rep = ''.join(random.choice(letters) for i in range(10))+'@swposters.com'
    #randomly assign a promo_code based on the promo_code list
    promo_code = random.choice(promo_code_list)
    poster_type = 'people'
    #obtain url string
    url = v.url
    #deleting the last string of url
    poster_url_delete_last_str = url[:-1]
    #logic to assign poster_number
    #(essentially, if there is not a "/" in the last two string values...
    # use the last two string characters as poster_number,
    # else use only the last string characters as poster_number)
    if poster_url_delete_last_str[-2].find('/') != -1:
        poster_number = poster_url_delete_last_str[-1]
    else:
        poster_number = poster_url_delete_last_str[-2:]
    #executing the query to insert each row of the sales data
    cursor.execute(query_insert,(sales_id_people,poster_content,quantity,price,email,sales_rep,promo_code,poster_type,poster_number))
    sales_id_people = sales_id_people + 1

#commit to write to database
db.commit()


#running a query to get the max sales_id currently in the salesdb.Sales table
query_max_sales_id = "SELECT MAX(sales_id) FROM salesdb.Sales"
cursor.execute(query_max_sales_id)
sales_id_max = cursor.fetchone()[0]
#essentially increment by 1 from the current max sales_id
sales_id_planets = sales_id_max + 1


#loop for inserting planets data to salesdb.Sales table
#(very similar approach to inserting people data)
planets = swapi.get_all('planets')
for x in planets.iter():
    poster_content = x.name
    quantity = random.randint(1,10)
    price = float(decimal.Decimal(random.randrange(10, 99))/10)
    email = ''.join(random.choice(letters) for i in range(10))+'@gmail.com'
    sales_rep = ''.join(random.choice(letters) for i in range(10))+'@swposters.com'
    promo_code = random.choice(promo_code_list)
    poster_type = 'planets'
    url = x.url
    poster_url_delete_last_str = url[:-1]
    if poster_url_delete_last_str[-2].find('/') != -1:
        poster_number = poster_url_delete_last_str[-1]
    else:
        poster_number = poster_url_delete_last_str[-2:]
    cursor.execute(query_insert,(sales_id_planets,poster_content,quantity,price,email,sales_rep,promo_code,poster_type,poster_number))
    sales_id_planets = sales_id_planets + 1

#commit to write to database
db.commit()


#running a query to get the max sales_id currently in the salesdb.Sales table
query_max_sales_id_new = "SELECT MAX(sales_id) FROM salesdb.Sales"
cursor.execute(query_max_sales_id_new)
sales_id_max_new = cursor.fetchone()[0]
#essentially increment by 1 from the current max sales_id
sales_id_starships = sales_id_max_new + 1


#loop for inserting starships data to salesdb.Sales table
#(very similar approach to inserting people and planets data)
starships = swapi.get_all('starships')
for y in starships.iter():
    poster_content = y.name
    quantity = random.randint(1,10)
    price = float(decimal.Decimal(random.randrange(10, 99))/10)
    email = ''.join(random.choice(letters) for i in range(10))+'@gmail.com'
    sales_rep = ''.join(random.choice(letters) for i in range(10))+'@swposters.com'
    promo_code = random.choice(promo_code_list)
    poster_type = 'starships'
    url = y.url
    poster_url_delete_last_str = url[:-1]
    if poster_url_delete_last_str[-2].find('/') != -1:
        poster_number = poster_url_delete_last_str[-1]
    else:
        poster_number = poster_url_delete_last_str[-2:]
    cursor.execute(query_insert,(sales_id_starships,poster_content,quantity,price,email,sales_rep,promo_code,poster_type,poster_number))
    sales_id_starships = sales_id_starships + 1

#commit to write to database
db.commit()

#closing the db connection to prevent affecting the database accidentally
#after completing all tasks from this file
db.close()