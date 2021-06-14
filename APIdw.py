#importing  necessary packages
import swapi
import mysql.connector as mysql
import csv

#connecting to the mysql dw database located in the mysqlDB2 container
db = mysql.connect(
    #the host is db2 since that is how it was initialized from the docker-compose.yml file
    host='db2',
    user='user',
    password='mySQLuser!@',
    database='dw',
    port='3306',
    #using the correct authentication plugin since mysql_native_password is not the default
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

#creating an insert query to be used for the dw.Starship_Film table
query_insert = "INSERT INTO dw.Starship_Film (starship_film_id, starship_name, film_appeared, film_made) VALUES (%s,%s,%s,%s)"
starship_film_id = 1

#retrieve all starships from the swapi api
#and create a loop to interate through all the different starships
starships = swapi.get_all('starships')
for x in starships.iter():
    starship_name = x.name
    #removing the first and last characters in the string as it has "[" and "]"
    film_list_str = str(x.get_films().items)[1:-1]
    #creating a string list using a comma separator
    film_list = list(film_list_str.split(","))
    #loop through the string list
    for y in range(len(film_list)):
        #providing a reset value, this variable is used below for the film object
        film = 0
        #creating a series of if, else if statements
        #used to match the film string value to retrieve title and release date information
        #(the strip function is used in case the string has empty spaces
        #at the beginning or end, in case the comma separation brought in any empty spaces)
        if film_list[y].strip() == '<Film - A New Hope>':
            film = swapi.get_film(1)
            film_appeared = film.title
            film_made = film.release_date
        elif film_list[y].strip() == '<Film - The Empire Strikes Back>':
            film = swapi.get_film(2)
            film_appeared = film.title
            film_made = film.release_date
        elif film_list[y].strip() == '<Film - Return of the Jedi>':
            film = swapi.get_film(3)
            film_appeared = film.title
            film_made = film.release_date
        elif film_list[y].strip() == '<Film - The Phantom Menace>':
            film = swapi.get_film(4)
            film_appeared = film.title
            film_made = film.release_date
        elif film_list[y].strip() == '<Film - Attack of the Clones>':
            film = swapi.get_film(5)
            film_appeared = film.title
            film_made = film.release_date
        elif film_list[y].strip() == '<Film - Revenge of the Sith>':
            film = swapi.get_film(6)
            film_appeared = film.title
            film_made = film.release_date
        #executing the query to insert each row of the starship_film data
        cursor.execute(query_insert,(starship_film_id,starship_name,film_appeared,film_made))
        starship_film_id = starship_film_id + 1
        y = y + 1

#commit to write to database
db.commit()


##below was used at first to create a csv file showing a summary of Starship_Film table
##attempting to see if there are any noticeable demographic correlation
##between starships and films (does the date of when the film was made
##or the film itself have correlation with the starship?)
##however, the file may be writing to a location in the container
##so it may be difficult to locate and open repeatedly
# cursor.execute("SELECT poster_content, film_appeared, film_made FROM dw.Starship_Film ORDER BY film_made ASC, poster_content DESC")
# print(cursor.fetchall())

# query_result_rows = cursor.fetchall()
# column_names = [i[0] for i in cursor.description]
# file_path = open('/tmp/dwStarship_FilmSummary.csv', 'w')
# output_file = csv.writer(file_path)
# output_file.writerow(column_names)
# output_file.writerows(query_result_rows)
# file_path.close()

#closing the db connection to prevent affecting the database accidentally
#after completing all tasks from this file
db.close()