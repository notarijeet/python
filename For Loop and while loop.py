#Loops and Iteration

nums = [1,2,3,4,5]

#for loop


#it will print a number from starting of loop to end
# for num in nums:
#     if num==3:
#         print('found')
#         continue
#     print(num)


#it will print a pair
# for num in nums:
#     for letter in 'abc':
#         print(num,letter)

print("for loop from range 1 to 6")

nums = ['A','B','C','D','E']

for i in nums:
    print(i)


#printing range:
for i in range(10):
    print(i)

print("while loop")

x = 0
while x<10:
    if x==5:
        break
    print(x)
    x +=1
    
x = 1
while x<=5:
    print(x)
    x = x+1


print("Loop from 1 to 5")

for i in range(5):
    print(i)
