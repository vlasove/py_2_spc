class Film:
    title = ""
    author = ""
    actors = []
    year = 0
    janre = ''

def film_creator(TITLE, AUTHOR, ACTORS, YEAR, JANRE):
    f = Film()
    f.title = TITLE
    f.author = AUTHOR
    f.actors = ACTORS 
    f.year = YEAR 
    f.janre = JANRE 
    return f 

f1 = film_creator("HP", "Rawling", ['a','b'], 2001, 'adventure')
f2 = film_creator("LOTR", "Tolkin", ['c','d'], 2002, 'adventure')

films = [f1, f2]