import json

ageStatement = ''
salaryStatement = ''
stateStatement = ''
nameLengthMax = 0

age = 0
salary = 0
name = ''
state = ''


def checkPerson(ageStatement, salaryStatement, stateStatement):
    if eval(ageStatement):
        if eval(salaryStatement):
            if eval(stateStatement):
                print 'yes you can'
            else:
                print 'city problem'
        else:
            print 'salary problem'
    else:
        print 'age problem'


with open('rule1.txt') as json_file:
    data = json.load(json_file)
    for f in data['rules']:
        ageStatement = f['ageStatement']
        salaryStatement = f['salaryStatement']
        stateStatement = f['stateStatement']
        print (ageStatement + ' ' + salaryStatement + ' ' + stateStatement + ' ')


with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        salary = p['salary']
        age = p['age']
        name = p['name']
        state = p['state']
        print (name + ' ' + str(age) + ' ' + state + ' ' + str(salary))
        checkPerson(ageStatement, salaryStatement, stateStatement)
