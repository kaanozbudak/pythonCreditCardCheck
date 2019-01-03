import json
import random
import string
import names

data = {}
data['people'] = []
for x in range(5000):
    age = random.randint(15, 70)
    alphabet_array = []
    for x in list(string.ascii_lowercase):
        alphabet_array.append(x)
    salary = random.randint(0, 10000)
    # name = ""
    # for x in range(6):
    #     name += alphabet_array[random.randint(0,25)]

    name = names.get_full_name()

    cities = ['istanbul', 'ankara', 'izmir', 'aydin', 'bursa', 'antalya', 'manisa', 'denizli', 'mugla', 'balikesir']

    city = cities[random.randint(0,9)]
    data['people'].append({
        'name': name,
        'age': age,
        'state': city,
        'salary': salary
    })
with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
