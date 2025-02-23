# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

# doubles=[x*2 for x in range(1,11)]
# print(doubles)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits = [f.upper() for f in fruits]
fruit_char= [f[0].upper() for f in fruits]
# print(fruit_char)

numbers=[1,2,-1,-2,3,-3]
positive_num=[n for n in numbers if n>0]
negative_num=[n for n in numbers if n<0]
even_num = [n for n in numbers if n%2==0]
odd_num = [n for n in numbers if n%2!=0]

# print(even_num)
# print(odd_num)

grades = [69 , 77 , 53 , 44, 90]
passing_grades = [g for g in grades if g>=60]
failing_grades = [g for g in grades if g<60]
print(passing_grades)
