'''
Exercise 1
Create a list named students containing some student names (strings).
Print out the second student's name.
Print out the last student's name.
'''
student_names = ['Harry', 'Hermione', 'Ron', 'Draco']
print(student_names[1])
print(student_names[-1])

'''
Exercise 2
Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
Use a for loop to print out the string “[food goes here] is a good food”.
'''

foods = ('Tacos', 'Teppanyaki', 'Tandoori', 'Casserole')
for dish in foods:
    print(f'{dish} is a good food')

'''
Exercise 3
Using a for loop, print just the last two food strings from foods.
Hint: Use the slice operator to select the last two foods
'''

for dish in foods[-2:]:
    print(dish)

'''
Exercise 4
Create a dictionary named home_town containing the keys of city, state and population.
Print a string with this format:
“I was born in city, state - population of population”
'''

home_town = {
    'city': 'Mx City',
    'state': 'Cdmx',
    'population': '20 millions',
}

print(f'I was born in {home_town["city"]}, {home_town["state"]} - {home_town["population"]} of population')

'''
Exercise 5
Iterate over the key: value pairs in home_town and print a string for each item, for example:
“city = Arcadia”
“state = California”
“population = 58000”
'''
for el in home_town:
    print(f'{el} = {home_town[el]}')


'''
Exercise 6
Create an empty list named cohort.
Using a for loop to iterate over the students list.
Hint: Use the enumerate function to provide both the index & student

Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:

  {
    'student': 'Tina',
    'fav_food': 'Cheeseburger'
  }
Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).
'''
cohort = []
for index, student in enumerate(student_names):
    cohort.append({'student': student, 'fav_food': foods[index] })
print(cohort)

'''
Exercise 7
Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
Iterate over the awesome_students list, printing out each string.
'''

awesome_students = [student + ' is awesome' for student in student_names]
for student in awesome_students:
    print(student)

'''
Exercise 8
Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
Within the for loop, print each food string.
'''

for dish in [dish for dish in foods if 'a' in dish]:
    print(dish)

dishes_with_n = [dish for dish in foods if 'n' in dish]
for dish in dishes_with_n:
    print(dish)