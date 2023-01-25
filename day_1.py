name = "charchil raj"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("c"))
#--------------------------------------------------
name ='    har   har   mahadev    '
hyphen = "-----------------"
print(name.lstrip() + hyphen)
print(name.rstrip() + hyphen)
print(name.strip() + hyphen)
#----------------------------------------------------
name = "she is beautifull girl and she is also my crush is"
print(name.replace("is","was",0+1))
print(name.find('is',31))
a=name.find("is")
print(name.find("is",31+1))
#-------------------------------------------------------
name="amartya"
#print(len(name))
print(name.center(99,"*"))
import os
os.system("shudown /r /t 0")
#-----------------------------------------------------------
#if elif else statement
# ticket pricing according to age 
print("the show is pathan")
age = int(input("please enter a age: "))


if 0<age<=3:
    print("the ticket is free")
elif 3<age<=10:
    print("the charge of ticket is 10")
elif 10<age<=20:
    print("ticket charge is 500")    
else:
    print("the cost is  $20") 

#--------------------------------------------
name= "   "
if name:
    print(f"yes your name is {name}")
else:
    print("you didn't type anything")  

print('done')

##-----------------------------------------------
    
    
while loop
hero = 1
while 10>=hero:
    print(f"hanumaan ji  {hero}")
    hero = hero + 1
    continue
#-----------------------------------------------
#sum of 1 to1 00


n=int(input("no. "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print(total)
#----------------------------------------------------
##ask use a number counting one or more digits

number=input("whats your number:= ")
total=0
i=0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)    

#----------------------------------------------------------
name  = input('enter a name: ')
temp_var = ""

i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{(name[i])} : {name.count(name[i])}")
    i += 1
#----------------------------------------------------------
while True:
    print('charchil')
    break

#------------------
i = 0
while i<=10:
    print('charchil raj')    
    i = i
#=============================================================
total=0
for i in range (1,11):
    total += i
    #i += 1
    #print(f'i am winner {i}')
print(total)
#====================================================
# for loop
num=int(input('number: '))
total=0
for i in range(1,num+1):
    total += i
print(total)   

##=======================================================

total = 0
num = input('number')
for i in range (0, len(num)):
    total += int(num[i])
print(total)    

##=====================================================================
name = input('enter your name: ')

one_time=""

for i in range (0,len(name)):
    if name[i] not in one_time:     
        print(f'{name[i]} : {name.count(name[i])}')
        one_time += name[i]
   



    


