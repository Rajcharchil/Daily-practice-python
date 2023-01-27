#break rule
for i in range(1,20):
     if i==7:
         break
     print(i)
       
#=================================================        
#continue rule
for i in range(1,20):
    if i==7:
        continue
    print(i)
#===============================================================================
# Diamond star 
def triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i) + " *"*(i))

triangle(10)         
#==============================================================================
winning_number= 43
guess = 1
number = int(input("enter a number 1 to 100: "))
game_over= False

while not game_over:
    if number == winning_number:
        print(f"you are win and the guess number is {guess} times by you")
        game_over=False
        print('thanku for playing game')
        break

    else:   
        if number < winning_number:
            print('too low')
            guess += 1
            number = int(input('guess again: '))

        else:
            print('too high')
            guess += 1
            number = int(input('guess again: '))
#===================================================================================
n =" ram "
for i in range(14,0,-1):
    print(n,i)#


###====================================================================
name = 'harshit   '
for i in "mohit":
    print(name,i)
#==================================================================================
def add_three(a,b,c):
    return a+b+c

print(add_three(5,5,5)) 

##==============================================================================

def my_name(name):
    return (name[-1])
print(my_name("charchil"))

##================================================================================
def odd_even(num):
    if num%2 == 0:
        return ("even")
    else:
        print('odd')
print(odd_even(11112))    

##============================================================================
def odd_even(num):
    if num%2 == 0:
        return ("even")
    return 'odd'
    
print(odd_even(1123424))

##===============================================================================
def is_odd_even(num):

    if num%2 == 0:
        return True
    return False
print(is_odd_even(9))

##=======================================================================================
def is_odd_even(num):
    return num%2 == 0
print(is_odd_even(64))

##=============================================================================================
def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
num1 = int(input('enter a number: '))    
num2 = int(input('enter a number: '))
bigger = greater(num1,num2)
print(f'{bigger} is greater')  


##================================================================================================

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
#print(greatest(100,45,50,))  


num1=int(input(">"))
num2=int(input(">")) 
num3=int(input('>')) 

greater = greatest(num1,num2,num3)
print(f"{greater}is bigger")

#==============================================================================
##wrong code
def new_greatest(a,b,c):
     # bigger = greater(a,b)
     return greater(greater(a,b),c)
print(new_greatest(1000,100,10))
#==============================================================================
def is_plaindrom(word):
    reserved_word = word[::-1]
    if word == reserved_word:
        return True
    else:
        return False
print(is_plaindrom("naman")) 
print(is_plaindrom("horse"))   

##=================================================================================


def is_palindrom(word):
    if word == word[::-1]:
        return True
    return False
print(is_plaindrom(input())) 
print(is_plaindrom(input()))  

##=================================================================================

def is_palindrom(word):
    return word == word[::-1]
print(is_palindrom("naman"))
print(is_palindrom("abmmba"))
##=================================================================================


str1 = str('python')
str2 = 'python'
print(str1 == str2,str1 is str2)
##  output is true
#=================================================================================
# fibonacci series
for i in range(1,11):
     print(i, end =",")
#================

def fibonacci_seq(n):
    a=0
    b=1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for i in range (n-2):
            c = a+b
            a = b
            b = c
            print(b , end = " ")

print(fibonacci_seq(20))
#==============================================================================================
# scope
x = 5 # global varibale

def function():
    global x
    x = 7  # local variables
    return x

print(x)             # output is 5
print(function())       # output is 7
print(x)             # output is 7


#===============================================================================================
number = [1,2,3,4]
print(number)
print(number[3])

word = ['hey','think big','iphone']
print(word)
print(word[:2])

mixed = ['wonderfull',1,5,'ram',10,'infiniet','hanumaan']
print(mixed)
print(mixed[:])
mixed[1]='two' 
mixed[1:]='two'
print(mixed)



#===========================================================================
fruit=['papaya','pineapple']
fruits=['mango','grapes','apple','banana','apple']
fruits.append('apple')
fruits.insert(1,'orange')
fruits.extend(fruit)
print(fruits)
###
fruits.pop()
del fruits[3]
print(fruits)
fruits.remove('apple')
print(fruits)



#============================================================================
charchil_raj = 'yes iam ,charchil '.split(', ')
print(charchil_raj)



#### split method
name, age = input('enter your name and age: ').split(',')
print(name,age)
print(age)


##########  join method
charchil_raj = ['yes iam' ,'charchil']
print(','.join(charchil_raj))





        

