from operator import indexOf
"""
s = 'Python'
for each in s :
    print(each)
    print(indexOf(s, each))
"""
print ('--------------------------------------------')

num = int(input("Enter a positive number:  "))
while num <= 0 :
    num = int(input("Enter a positive number:  "))
print(f" you inter the {num}  ")

print ('-------------------------------------------')

answer = input('inter yes or no:')
while not(answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('inter yes or no:')

print(f"you have entered {answer}")