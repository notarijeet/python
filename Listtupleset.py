#List , Tuples and Set

courses = ['History','Math','Physics']

courses_2 = ['Art','Education']

courses.extend(courses_2)

print(len(courses))

print(courses[0])
print(courses[2])

print(courses[-1])

print(courses[0:2])

print(courses)

courses.pop();

print(courses)

courses.reverse();
print(courses)

courses.sort()
print(courses)

print('Art' in courses)

print('Math' in courses)

#Loop
for item in courses:
    print(item)


course_str = ', '.join(courses)
print(course_str)


#Tuples
cs_courses = ('namaste','chamaste','simaste','dimaste')
print(cs_courses)


#Set: it does not allow duplicates

sems = {'history','pistory','distory','distory'};
print(sems)

#union , difference , intersection


#Empty list
empty_list = []
empty_list = list()


#Empty tuple
empty_tuple = ()
empty_tuple = tuple()


#Empty sets
empty_set = {}
empty_set = set();
