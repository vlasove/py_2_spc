def film_creator(TITLE, AUTHOR, ACTORS, YEAR, JANRE):
    f = Film()
    f.title = TITLE
    f.author = AUTHOR
    f.actors = ACTORS 
    f.year = YEAR 
    f.janre = JANRE 
    return f 


f1 = film_creator("a", "b", "c", "d", "e")