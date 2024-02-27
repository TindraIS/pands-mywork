'''
Questions
What are the variable types of the following variables in the code above
a. numberOfQuestions: int
b. averageAge: float
c. debugMode: boolean
d. name: string
e. ages: empty list
f. months: tuple
g. months[1]: string
h. book: dictionary
i. stuff: list
j. stuff[2]: boolean
k. someone: dictionary
l. someone["firstname"]: string
m. me: dictionary
n. me["teaching"]: list
o. me["teaching"][0]["semester"]: int
p is a trick question look at it carefully
p. me["teaching"][0]["coursename"]: it doesn't exist
'''

numberOfQuestions = 5
print(type(numberOfQuestions))
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
print(type(months[1]))
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
}
]
}
print(type( me["teaching"][0]["semester"]))
print(type( me["teaching"]))


#----------------------------------------------------------

months_year = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

#summer_months = (months_year[4],months_year[5],months_year[6])
summer_months = months_year[4:7]
print(summer_months)


#----------------------------------------------------------

import random as rd

random_list = []
list_size = 10 

for i in range(0,list_size):
    random_number = rd.randint(1,101)
    random_list.append(random_number)
print(f'Queue is {random_list}')

while len(random_list) > 0:
    current_number = random_list.pop(0)
    print(f'Current number is {current_number} and queue is {random_list}')

print('The queue is empty.')

#----------------------------------------------------------

dictionary = {
    "student" : "Mary",
    "modules" : [
        {
            "module_name" : "Programming",
            "module_grade" : 45,
        },
        {
            "module_name" : "History",
            "module_grade" : 99,
        }
    ]
}

print("Student: {}".format(dictionary["student"]))

for module in dictionary["modules"]:
    print("\t {} \t: {}".format(module["module_name"], module["module_grade"]))