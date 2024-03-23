#Create a normal and comprehensive list that will display the codes.
codes = [14, 15, 16, 17, 18, 19, 20]

'''print("This is a Normal List: ")
print(codes)

#Create a normal and comprehensive list that will add the codes together for auditing purpose.
codeSum = []

sum = 0
for n in codes:
    sum += n


codeSum.append(sum)
print()
print("This is the sum of a normal list: ")
print(codeSum)

#Comprehensive list
codes = [14, 15, 16, 17, 18, 19, 20]

codeSum = sum([n for n in codes])
print()
print("This is a comprehensive list: ")
#print(codeSum)

#codeSum = sum([n for n in codes])

print()
print("This is the sum to of the comprehensive list: ")
print(codeSum)'''

#Create a normal and comprehensive list that will display only codes that are tracked by odd numbers

#This is a norml list
'''my_codes = []

for n in codes:
    if (n%2!=0):
        my_codes.append(n)

print(my_codes)'''

#This is a comprehensive list
'''my_codes = [n for n in codes if n%2!=0]

print(my_codes)'''

#Create a set to display the list of codes.
set_list = {14,15,16,17,18,19,20}

print("this is a set lis: ")
print(set_list)

