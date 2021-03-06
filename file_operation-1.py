# Open a file
print('File Opening in normal read mode-> rb')
fo = open("data/data1.txt", "r")
print("Name of the file: ", fo.name)
print(fo.read())
print("Closed or not : ", fo.closed)
fo.close()
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
# print("Softspace flag : ", fo.softspace)
print('*********************************')
# Open a file
print('File Opening in binary mode-> rb')
fo = open("data/data1.txt", "rb")
print("Name of the file: ", fo.name)
print(fo.read())
print("Closed or not : ", fo.closed)
fo.close()
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
# print("Softspace flag : ", fo.softspace)
print('*********************************')
# Open a file
print('File Opening in binary mode-> rb+/r+b')
fo = open("data/data1.txt", "r+b")
print("Name of the file: ", fo.name)
print(fo.read())
print("Closed or not : ", fo.closed)
fo.close()
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
# print("Softspace flag : ", fo.softspace)
print('*********************************')
# Open a file with encoding
print('File Opening with Encoding')
fo = open("data/data1.txt", "r", encoding='utf-8')
print("Name of the file: ", fo.name)
print(fo.read())
print("Closed or not : ", fo.closed)
fo.close()
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
