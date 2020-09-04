# Python List
# List in python is implemented to store the sequence of various type of data.
# However, python contains six data types that are capable to store the sequences
# but the most common and reliable type is list.
#
# A list can be defined as a collection of values or items of different types.
# The items in the list are separated with the comma (,) and enclosed with the square brackets [].
# The index starts from 0 and goes to length - 1. The first element of the list is stored at the 0th index,
# the second element of the list is stored at the 1st index, and so on.
# Lists are the most versatile data structures in python since they are immutable and
# their values can be updated by using the slice and assignment operator.

employee = ['John', 102, 'USA']
Department1 = ["CS", 10]
Department2 = ["IT", 11]
HOD_CS = [10, "Mr. Holding"]
HOD_IT = [11, "Mr. Bewon"]
print("********************Employee Data*****************")
print("Name: {}, Id: {}, Country: {}".format(employee[0], employee[1], employee[2]))
print("*****************************Department Data******************************")
print("Department-1 Name: {}, Department-1 Id: {}, Department-2 Name: {}, Department-2 Id: {}".format(Department1[0], Department1[1], Department2[0], Department2[1]))
print("*****************************HOD Details******************************")
print("HOD-CS Id: {}, HOD-CS Name: {}".format(HOD_CS[0], HOD_CS[1]))
print("HOD-IT Id: {}, HOD-IT Name: {}".format(HOD_IT[0], HOD_IT[1]))
print("List Operation")
list_1 = [1,3, 7, 9, 5, 6]
print(list_1[0])
print(list_1[0:])
print(list_1[0:3]) # last index = n-1. Here n = 3
print(list_1[-1])
print(list_1[-2])

