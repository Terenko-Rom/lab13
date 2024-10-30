class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population
    def __del__(self):
        print(f"Видалення міста {self.name}")
    def display(self):
        print(f"Місто: {self.name}, Країна: {self.country}, Населення (тис.): {self.population}")
def create_city_list(n):
    cities = []
    for i in range(n):
        name = input("Введіть назву міста: ")
        country = input("Введіть країну: ")
        population = int(input("Введіть кількість населення (тис): "))
        city = City(name, country, population)
        cities.append(city)
    return cities
city_list = create_city_list(3)
for city in city_list:
    city.display()