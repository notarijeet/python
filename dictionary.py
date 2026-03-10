# cook your dish here
#dictionary

student = {'name':'john','age':25,'courses':['math','compsci']}
print(student);
print(student['courses']);
print(student['age']);
print(student['name']);
print(student.get('name'));
print(student.get('phone','not found'));
student['name'] = 'arijeet';
print(student.get('name'));
student['age'] = 30;
print(student.get('age'));

del student['age']
print(student)

print(student.values());
print(student.items());

