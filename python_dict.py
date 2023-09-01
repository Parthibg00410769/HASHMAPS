locations = {
    'North America': {'USA': ['Mountain View', 'Atlanta']},
    'Asia': {
        'India': ['Bangalore'],
        'China': ['Shanghai']
    },
    'Africa': {'Egypt': ['Cairo']}
}

print("1")
#us_cities = sorted(locations['North America']['USA'])
for country, city in locations['North America'].items():
    for city1 in sorted(city):
        print(f"{city1} - {country}")

print("2")
for country, cities in locations['Asia'].items():
    for city in sorted(cities):
        print("{} - {}".format(city, country))