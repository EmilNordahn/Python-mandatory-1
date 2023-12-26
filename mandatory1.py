# Mandatory assignment 1
# (1)

directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}



print("(1)\nThese directors are not employees: ", directors.difference(employees), "\n")

print("These directors are also employees: ", directors.intersection(employees), "\n")

print("These managers are on the board", management.intersection(directors), " \nThat is: ", len(management.intersection(directors)), "\n")

print("These managers are also employees: ", management.intersection(employees), "\n")

print("These employees are employees, managers and on the board of directors: ", management.intersection(employees.intersection(directors)), "\n")

print("These employees are neither managers nor on the board: ", employees.difference(management).difference(directors), "\n")

# (2)

datastruct = {'a':'Alpha','b':'Beta','g':'Gamma'}

tupleList = []

for key, value in datastruct.items():
    tupleList.append((key, value))

print("\n\n(2)\n", tupleList)

# (3)

setA = {'a', 'e', 'i', 'o', 'u', 'y'}
setB = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

print("\n\n(3)\nUnion: ", setA.union(setB))
print("\nUnion: ", setA|setB)
print("\nSymmetric Difference: ", setA.symmetric_difference(setB))
print("\nSymmetric Difference: ", setA^setB)
print("\nDifference(left): ", setA.difference(setB))
print("\nDifference(right): ", setB.difference(setA))
print("\nDifference(left): ", setA-setB)
print("\nDifference(right): ", setB-setA)
print("\nDisjoint: ", setA.intersection(setB))
print("\nDisjoint: ", setA&setB)

# (4)

givenDate = '8-MAR-85'

monthDict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

def translateDate(date):
    translatedDate = date.split("-")
    translatedDate[1] = monthDict[translatedDate[1].upper()]
    translatedDate[0] = int(translatedDate[0])
    translatedDate[2] = int(translatedDate[2])


    return tuple(translatedDate)

print("\n\n(4)\n", translateDate(givenDate))

# (5)

friendsInvited = {'Simon', 'Rob', 'Anna', 'Earl', 'Julie', 'Karla'}
friendsRSVP = {'Anna', 'Rob', 'Florence', 'Julie'}

print("\n\n(5)\nFriends who haven't RSVP'd: ", friendsInvited.difference(friendsRSVP),
      "\nFriends who RSVP'd but weren't invited: ", friendsRSVP.difference(friendsInvited),
      "\nFriends who are invited but haven't RSVP'd", friendsInvited.intersection(friendsRSVP))

# (6) 

print("\n\n(6)\n")

students = {'Simon': 12, 'Rob': 55, 'Anna': 85, 'Earl': 63, 'Julie': 74, 'Karla': 87}


def gradeStudents(students):

    studentOutput = []
    while True:

        print(students.keys(), "\nWhich student's grade should be updated? (leave empty to end)")

        studentInput = input()
    
        if studentInput is "":
            for s, g in students.items():
                if g >= 85: 
                    studentOutput.append(s)
            break
        elif studentInput not in students.keys():
            print(studentInput, "is not a valid student name")
            continue 
        else:
            print("What is the grade of ", studentInput, "?")
            students[studentInput] = int(input())
    print("Students with a grade larger than or equal to 85: ", studentOutput)
    
gradeStudents(students)