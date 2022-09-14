database_name = "cinema_database.txt"

movie_name = 0
movie_date = 1
movie_cost = 2
movie_viewers = 3

movies_list = []
index_max_viewed_movie = -1
with open(database_name, "r") as cinema_file:
    index = 0
    for movie_session in cinema_file:
        value_list = list(movie_session.split())
        movies_list.append(value_list)
        if index_max_viewed_movie == -1 or\
                int(movies_list[index_max_viewed_movie][movie_viewers]) < int(value_list[movie_viewers]):

            index_max_viewed_movie = index
        index += 1

print(f"Most viewed movie: {movies_list[index_max_viewed_movie]}\n")

date_input = input("Input date (DD.MM.YYYY): ")
for movie in movies_list:
    if movie[movie_date] == date_input:
        print(f"Movie Title  : {movie[movie_name]}")
        print(f"Movie date   : {movie[movie_date]}")
        print(f"Movie cost   : {movie[movie_cost]}")
        print(f"Movie viewers: {movie[movie_viewers]}")


