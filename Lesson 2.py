"""
Topics:
- Input and Output
- Strings
- String Manipulation
- split(), strip(), title(), upper()
- Lists
- if / elif / else
- For-each loops
- Counter-controlled loops
- String formatting
- ljust(), center(), rjust()
- User-defined functions

====================================================
INPUT AND STRING MANIPULATION
====================================================
#Store users name in a variable. The order matters, first method (strip()) runs before the next (capitalize())
name = input("Enter your name: ").strip().capitalize()  
print("Hi "+name)
"""

#Stores the users games as a string
games = input("Enter your favourite games (separated by comma): ")
print(games)

#Removes whitespaces in string
#games = games.replace(" ", "")  #Remove all spaces from the string
#Create the list of games entered by the user

game_list = games.split(",")

print (game_list)

#Prepare the list, this just creates an empty list we can use to store processed (.strip().title()) strings.
clean_games = []

#Clean the games and remove blank entries
for game in game_list:  # for-each loop

    #Clean the game name, removing leading/trailing spaces and capitalising the first letter of each word
    game = game.strip().title()

    #Remove blank entries, in case the user entered a comma with no game name
    if game != "":
        clean_games.append(game)


print("\nCleaned Games")
#Goes through each game in the list, and prints each game
for game in clean_games:
    print(game)



#FOR LOOP (With counter)
print("\nCounter Example")
#Print the same list of games, but adding an incrementing counter for each element.
#Initialize a counter variable to 1, count starts at 1
counter = 1
#For every game in the list of cleaned games, print the game with a number in front of it, and increase the counter by 1
for game in clean_games:

    #Using an "f-string" to include variables into printed text. (optionally: print(counter,"- ",game))
    print(f"{counter}- {game}")
    #Increasae the counter for each loop (iteration), so the next printed item will be 1 higher
    counter += 1
    
"""

#IF / ELIF / ELSE

# if the length of the list is less than 3, print a message
if len(clean_games) < 3:
    print("You need more favourite games!")
# if the length of the list is between 3 and 5, print a different message
elif len(clean_games) <= 5:
    print("Nice collection!")
# if the length of the list is greater than 5, print a different message, since this is the last condition, we can use else instead of elif
else:
    print("You are a serious gamer!")




#STRING ALIGNMENT

#Print a new line and a border of 40 asterisks
print("\n" + "*" * 40)

#Create a title using the users name, and convert it to uppercase
title = f"{name.upper()}'S FAVOURITE GAMES"

#Print the title, centered, with a border of asterisks on either side
print("*" + title.center(38) + "*")

#Print another border of 40 asterisks
print("*" * 40)









#DEMONSTRATION 6 - FUNCTIONS

#this function prints a border of 40 asterisks
def print_border():
    print("*" * 40)


#this function cleans the game name, removing leading/trailing spaces and capitalising the first letter of each work
def clean_game(game):
    return game.strip().title()


#this function displays the title
def create_title(name):
    return f"{name.upper()}'S FAVOURITE GAMES"


#this function displays the game entry with a number and proper formatting (Number. gameName)
def display_game(number, game):

    entry = f"{number}. {game}"

    print("* " + entry.ljust(36) + "*")



print("\nFunction Demonstration")

#Call the border function
print_border()
#Call the create_title function, passing in the users name, and print the result
print("*" + create_title(name).center(38) + "*")
#Call the border function again
print_border()

#initialize the counter variable to 1, count starts at 1
counter = 1
#For every game in the list of cleaned games, call the display_game function, passing in the counter
for game in clean_games:

    display_game(counter, game)

    counter += 1

#print the border again
print_border()



"""

#==== When creating functions, be aware of existing function names ====


"""
TASK 1 - Movie Collection Display

1. Ask for the user's name.
2. Ask for favourite movies separated by commas.
3. Clean the movie names, no unnecessary whitespaces, proper capitalization.
4. Remove blank entries.

5. Display a message using if/elif/else, based on how many movies the user entered:

   < 3 movies      = You should watch more movies!
   3-5 movies      = Nice movie collection!
   > 5 movies      = You are a movie enthusiast!

6. Use center() for the title.
7. Use ljust() for movie entries.
8. Create and use functions:

   ..one that prints a border
   ..one that cleans the movie name
   ..one that displays the movie entry with a number and proper formatting (Number. movieName)

9. Display the final movie collection.

The end result should look like this (With your input ofcourse):
Enter your name: Sarah

Enter your favourite movies (comma separated):
the matrix, inception, interstellar

****************************************
*      SARAH'S MOVIE COLLECTION        *
****************************************

Nice movie collection!

* 1. The Matrix                        *
* 2. Inception                         *
* 3. Interstellar                      *

****************************************
"""
# Your solution goes here
# Refer to lesson examples and build the solution.
#---------










#----------

"""
TASK 2 - MEDIUM - Skills Report

1. Ask for student name.
2. Ask for course name.
3. Ask for skills separated by commas, (ex: Python, Javascript, CloudSec, Azure, InfoSec, etc)
4. Clean all entries.
5. Remove duplicates.
6. Remove blank entries.
7. Display an assessment:

   1-3 skills = Beginner Level
   4-6 skills = Developing Skills
   7+ skills  = Strong Skills

8. create and use functions:

   print_border()
   clean_skill(skill)
   display_skill(number, skill)
   get_assessment(total_skills)

9. Use the following string formatting methods to to display the result:

   center()
   ljust()
   rjust()

10. Display a formatted report.

The end result should look like this (with your input ofcourse):
Enter student name: John Smith

Enter course name: Software Development

Enter skills (comma separated):
python, html, css, javascript, python

**************************************************
*           STUDENT SKILLS REPORT                *
**************************************************

Student : John Smith
Course  : Software Development

Assessment : Developing Skills

Skills

* 1. Python                                     *
* 2. Html                                       *
* 3. Css                                        *
* 4. Javascript                                 *

                                   Total Skills: 4
**************************************************
"""

# Your solution goes here
# Refer to lesson examples and build the solution.
#-----------------







"""
Additional tasks:
- Sort items alphabetically.
- Ask for a favourite item and highlight it.
- Save the results to a text file.
- Allow multiple users to be entered.
"""
