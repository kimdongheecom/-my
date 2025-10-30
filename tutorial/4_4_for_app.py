


persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]

print(persons[0][2])


for person in persons:
    print(person[0]+','+person[1]+','+person[2])

person=['egoing', 'Seoul', 'Web']

name=person[0]
city=person[1]
job=person[2]
print(name, city, job)

name,city,job=['egoing', 'Seoul', 'Web']
print(name, city, job)

for name,city,job in persons:
    print(name+','+city+','+job)







