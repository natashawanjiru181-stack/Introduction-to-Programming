# %% - this makes it Python Interactive Mode
# Level 1
# 1. Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
age=int(input('Enter your age:'))
if age>=18:
    print('You are old enough to drive')
if age<18:
    print('wait for the missing amount of years')

# %%
# 2. Use input(“Enter your age: ”) to get the age as input 
my_age=int(input('Enter my age')) 
print(my_age)

your_age=int(input('Enter your age'))
print(your_age)

#Compare the values of my_age and your_age using if … else.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, # You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
if my_age-your_age==1:
    print('year')
    
elif my_age-your_age>1:
     print('years')
    
else:my_age=your_age
print('custom text')

# %%
# 3. Get two numbers from the user using input prompt
a=int(input('Enter a number:'))
print(a)

b=int(input('Enter a number:'))
print(b)

# If a is greater than b return a is greater than b
#if a is less b return a is smaller than b,
# else a is equal to b
if a>b:
    print(' a is greater than b')
    
elif a<b:
    print('a is smaller than b')
    
else:
    print('a is equal to b')

# %%
# Level 2
# 1. Write a code which gives grades to students according to theirs scores:
# a) Create a dictionary where keys are student names and values are their scores.
a={'Tash':98, 'Mat':45, 'Sam':67, 'Liam':77, 'Kate':55 }

# b) Defines a function grade_if(score) that returns a grade (A–F) based on score ranges using if/elif/else. 
def grade_if(score: int) -> str:
    if score>= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
# c) Loops through the dictionary with for name, score in a.items() to access each student and score.
# Prints each student’s name, score, and computed grade using an f-string.
for name, score in a.items():
    print(f"{name}: {score} → {grade_if(score)}")



