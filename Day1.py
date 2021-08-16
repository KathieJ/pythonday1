Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> name="Katherine"
>>> print(name)
Katherine
>>> age=14
>>> print(age)
14
>>> print("Hello"+ name)
HelloKatherine
>>> print("Hello" + name)
HelloKatherine
>>> print("Hello "+ name)
Hello Katherine
>>> age= str(age)
>>> print(age)
14
>>> print("Age of " + name + " is " + age)
Age of Katherine is 14
>>> 1500+200
1700
>>> myFriends= ["Mahika" , "Kanisha" , "Jiya" ]
>>> print(myFriends)
['Mahika', 'Kanisha', 'Jiya']
>>> print(myFriends[2])
Jiya
>>> print(myFriends[0])
Mahika
>>> destination= input("Where do you wanna go to Vacation")
Where do you wanna go to Vacation Maldives
>>> print(destination)
 Maldives
>>> pocketMoney= input("How much is your pocket money ? ")
How much is your pocket money ? 3000
>>> pocketMoney= int(input("How much is your pocket money ?"))
How much is your pocket money ? 3000
>>> if(pocketMoney > 1000):
	print("yes")

	
yes
>>> 
>>> if
SyntaxError: invalid syntax
>>> 
if(pocketMoney <1000):
	print("yes")
else:
	print("no")

	
no
>>> for a in myFriends:
	print(a)

	
Mahika
Kanisha
Jiya
>>> introString= input("Enter your name")
Enter your nameKatherine Jacob
>>> wordCount=wordCount+1
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    wordCount=wordCount+1
NameError: name 'wordCount' is not defined
>>> wordCount=0
>>> numberofCharacters=0
>>> for i in introString:
	