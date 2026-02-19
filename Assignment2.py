# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Sadaya Preston
# Assignment Number: Assignment 2
# Due Date: 2/18/26
# Purpose: This program reads a text file containing student names and 6 scores,
#          calculates each student's average, and prints all students in
#          descending order by their final average grade.
# Resources: Module_3-1 and Module_3-2 slides, stack overflow


#opening and reading the input file 
with open("Assignment2input.txt", "r") as file:
    lines = file.readlines()

#creating list to store results
students_averages = []

#loop every student in the file
for line in lines:
    line = line.strip() #newlinw character dupe
    if not line:
        continue #line is empty please skip to next line
    parts = line.split() #breaks line apart where there is space
    name = parts[0] #first item is students names
    #go through each item in parts[1:] convert it to int collect them into a list.
    scores = [int(score) for score in parts[1:]]
    #dividing and calculating the average
    average = sum(scores)/len(scores)
    average_total= round(average,2)
    #storing the result
    students_averages.append([name, average_total])

#storinig result in descending order by ave
students_averages.sort(key=lambda x: x[1], reverse=True)
#key=lambda x: x[1] tells python to sort by the 2nd item in each list (aka score ave)
#.sort() rearranges the list in place
#reverse=True means highest grade goes 1st

for student in students_averages:
    name    = student[0]    # First item is the name
    average = student[1]    # Second item is the average
    print(f"{name} {average:.2f}")
