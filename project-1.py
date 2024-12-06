# Add new movies to my collection
## So i can keep track on all my movies 
# List all the movies in my collection
## So i can see what movies i already have
# Find a movie buy using the movie tile
## So i can locate a specific movie easily when the collection grows
# Decide where to store movies in code
# Decide what data we want to store for each movie
# Show the user a menu and let hem pick an option
# Implement each requirement in turn, each as a separate function


# Features: 
## First, The app must allow to add new movies to the collection
## The app must allow users to view all the movies in the collection
## The application must also allow users to find any particular movie by attribtes
import os
import csv


MENU_PROMT = "\nEnter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie by title, or 'q' to quit: "
MODE='year'
CHOICE='y'


def save_file(movies):
	fields=['name','director','year']
	path=os.getcwd()
	file_name = os.path.join(path,'movies.csv')
	with open(file_name,'w') as file:
		csv_file=csv.DictWriter(file,fieldnames=fields)
		csv_file.writeheader()
		csv_file.writerows(movies)
	file.close()

def open_file():
	with open('movies.csv','r') as file:
			data = list(csv.DictReader(file))
	file.close()
	return data

	

def add_movies():
		name = input("Enter the movie name: ")
		director = input("Enter the movie director: ")
		year = input("Enter the movie release year: ")
		movies.append({'name': name,
					 'director': director,
					 'year': year})
		save_file(movies)
def show_movies():
	for movie in movies:
			print(f"Movie: {movie['name']} | Director: {movie['director']} |  Year: {movie['year']}")
def find_movie():
	FIND_OPTIONS = "\n Find movies name, Enter 'y' to find base on 'Year', 'd' to find base on 'Director' "
	option = input(FIND_OPTIONS).lower()
	if option == 'y':
		mode='year'
		choice = input("Enter the year: ")
	elif option == 'd':
		mode='director'
		choice = input("Enter the director: ")
	for movie in movies:
		if movie[mode]==choice:
			print(f"Movie: {movie['name']} | Director: {movie['director']} |  Year: {movie['year']}")

user_options = {
	"a": add_movies,
	"l": show_movies,
	"f": find_movie
}

selection = input(MENU_PROMT)
movies=open_file()
while selection != 'q':
	if selection in user_options:
		selected_function = user_options[selection]
		selected_function()
	selection = input(MENU_PROMT)





