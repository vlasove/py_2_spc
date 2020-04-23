from models.vacancy import Vacancy

v = Vacancy("Python Developer", "Yandex", 120000)
v1 = Vacancy("Python Dev + JS", "Avito", 115000)

v.save()
v1.save()