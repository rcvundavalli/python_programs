dataFile = """
"Ravindranad",3,23.45
"Siva Kumar",4,34.43
"Suresh",18,12.34
"Ramesh",10, 18,98
"""

lines = [line for line in dataFile.splitlines() if line != ""]
print(lines)

lines.sort(key = lambda x:x.split(",")[1])
print(lines)


lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)
student_tuples = [
   ('john', 'A', 15),
   ('jane', 'B', 12),
    ('dave', 'B', 10),
 ]
print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age


student_tuples.sort(
  key = lambda l: (l[0], l[2])
)
print(student_tuples)

x = [10, 23, 43, 11]
for x[-1] in x:
    print(x[-1])
