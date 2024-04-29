a=input("Enter Your Name")
b=input("Enter Your Class")
c=input("Enter Your Section")

pm=float(input("Enter Your Physics Marks"))
cm=float(input("Enter Your Chemistry Marks"))
mm=float(input("Enter Your Maths Marks"))
em=float(input("Enter Your English Marks"))
csm=float(input("Enter Your CS Marks"))

d=pm+cm+mm+em+csm

up=(d/200)*100

if up>=95:
  grade="A"

elif up>=75:
  grade="B"

elif up>=50:
  grade="C"

elif up>=30:
  grade="D"

elif up<15:
  grade="E"


print("            Report Card            ")
print("________________________________________")
print("Name: ", a, "Class: ", b, "Section: ", c)
print("________________________________________")
print("Subjects:")
print("Maths"  ,mm)
print("English"  ,em)
print("Chemistry"  ,cm)
print("Physics"  ,pm)
print("Computer Science"  ,csm)
print("________________________________________")
print("Persentage:"  ,up)
print("Total Marks:"  ,d)
print("________________________________________")

print("Congratulations You Got" ,grade, "Grade")
