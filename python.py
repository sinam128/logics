class student :
	def __init__ (self , name , code , grade ) :
		self.name = name 
		self.code = code 
		self.grade = grade
	def details (self) :
		print(f"Your name is {self.name} , your code is {self.code} and your grade is {self.grade} ")

a = input("Please Enter your name here : ")
b = int(input("Please Enter your student code here : "))
c = int(input("Enter the count of lessons you wanna enter : "))
list = []
list2 = []
list3= []
result = 0 
for inp in range(c) : 
	i = input("The Name of the lesson : ")
	g = float(input("The grade at this lesson : "))
	unit = int(input("Please Enter the units of lesson : "))
	list.append(i)
	list2.append(g)
	list3.append(unit)
	result += (list2[inp] * list3[inp])
p = 0 
for innn in list3 :
	p += innn 
student1 = student(a , b , result / p )
student1.details()
