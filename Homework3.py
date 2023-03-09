print('Welcome to GC Property Managment!')


def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        print(f"Searching for apartments in {city} with a maximum rent of {max_rent}, at least {min_beds}"
              f" bedrooms, and pets allowed")
    else:
        print(f'Searching for apartments in {city} with a maximum rent of {max_rent}, at least {min_beds} '
              f'bedrooms, and no pets allowed')


apt_search1('Detroit', 2500, 2, True)

print("Welcome to GC Property Managment!")


def apt_search2(city, max_rent, min_beds=3, pets_allowed=False):
    if pets_allowed:
        print(f"Searching for apartments in {city} with a maximum rent of {max_rent}, at least {min_beds}"
              f" bedrooms, and pets allowed")
    else:
        print(f'Searching for apartments in {city} with a maximum rent of {max_rent}, at least {min_beds} '
              f'bedrooms, and no pets allowed')


apt_search2('Detroit', 2000, 5)
apt_search2('Detroit', 2500)
apt_search2('Detroit', 2300, pets_allowed=True)

plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(100))

squared_number = lambda y: y ** 2
print(squared_number(5))

concatenate_strings = lambda z: "- " + z
print(concatenate_strings('hello'))

divide_by_three = lambda f: f / 3
print(divide_by_three(9))
