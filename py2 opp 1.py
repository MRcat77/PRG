name = input("Enter your name: ")
movie = input("Enter your favourite games (separated by comma): ")

movies_list = movie.split(",")
clean_movies = []

for movie in movies_list:
    movie = movie.strip().title()

    if movie != "":
        clean_movies.append(movie)
clean_movies.sort()


comment = ""
if len(clean_movies) < 3:
    comment = "You should watch more movies!"

elif len(clean_movies) >= 5:
    comment = "Nice movie collection!"

else:
    comment = "You are a movie enthusiast!"

title = name.title() + "'s Movie Collection"
len_title = len(title)
if len_title > 40:
    len_border = len_title + 4
    print("\n" + "*" * len_border)
    print(f"* {title.center(len_title)} *")
    print("*" * len_border)
    print(f"* {len_title * " "} *")
else:
    print("\n" + "*" * 40)
    print(f"* {title.center(36)} *")
    print("*" * 40)
    print(f"* {36 * " "} *")
    len_title = 36

counter = 1

def display_movie(number, movie):
    entry = f"{number}. {movie}"
    print(f"* {entry.ljust(len_title)} *")

for movie in clean_movies:
    display_movie(counter, movie)
    counter += 1

print(f"* {len_title * " "} *")
print(f"* {comment.center(len_title)} *")
print((len_title+ 4) * "*")