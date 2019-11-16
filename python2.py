'''
1.	Take 2 input, calculate in all mathematics operations.;
2.	Make a list of 5 students height. Calculate the average of it.;
3.	Input 2 numbers and continuously finds out “Greater” or “Smaller” in several times. Break when they will be Equal.;
4.	Create a list named food, such as
foods = [ ‘Burger’, ‘Sandwich’, ‘Pizza’ ]

Add ‘Candy’ and ‘Coca Cola’ in the list. Remove Pizza from the list.;
'''

'''
python assainment.2
'''
'''
#problem 1
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print("Addition : ", num1+num2,'\n', "subtraction: ",num1-num2,'\n', "multiplication: ", num1*num2, '\n',"divided: ", num1/num2)
'''

'''
#problem 2
height = [ 6.02, 5.07, 4.7, 12.7]
summation = sum(height)
print("average: ", summation /50)
'''
'''
#problem 3
for nums in range(5):
    firstNum =int(input("enter 1: "))
    secondNum = int(input("enter 2: "))

    if firstNum > secondNum:
        print(firstNum, "is Greater")
    elif firstnum == secondNum:
            break
    else: print(secondNum,"is grater")
'''
'''
#problem 4
foods = ['Burger', 'Sandwich', 'Pizza']

foods.append('Candy')
foods.append('Coca Cola')

foods.remove('Pizza')
print(foods)
'''
