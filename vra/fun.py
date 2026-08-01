###########x=10/0
      #print(x)
#except:
   #print("An exception occurred.")

#def myfunction(name,age):
 #print(f"the name is{name}")
 #Function ko call karna
# myfunction("ali",18)
 #.2 Try-except block
 #try:
     #x=10/0
     #print(x)
 #except:
 # print("An exception occurrd.")


#def divide(x,y):
    #try:
        # rasult=x/y
     #    print("Result:",rasult)
    #except ZeroDivisionError:
       #print("Cannot divide by zero")
        
#divide(2,10)



#class myclass1:
   #{'Category': 'Tech', 'Profit': 300},
    #]

# Logic
#or item in data:
    #   status = "Needs Improvement"
        
    #print(f"Category: {category:<10} | Profit: {profit:<5} | Status: {status}")

# ==========================================
# 🎯 PART 2: AUTOMATIC GRADE & STATUS SYSTEM
# ==========================================

print("\n" + "=" * 40)
print("       PERFORMANCE EVALUATION")
print("=" * 40)

# 1. Bushra Ka Grade Check Karna
print("🔍 Checking Bushra's Status:")
if bushra_marks >= 90:
    bushra_grade = "A+"
elif bushra_marks >= 80:
    bushra_grade = "A"
elif bushra_marks >= 70:
    bushra_grade = "B"
else:
    bushra_grade = "Fail"

print(f"   • Marks : {bushra_marks}")
print(f"   • Grade : {bushra_grade}")

print("-" * 40)

# 2. Zuhair Ka Grade Check Karna
print("🔍 Checking Zuhair's Status:")
if zuhair_marks >= 90:
    zuhair_grade = "A+"
elif zuhair_marks >= 80:
    zuhair_grade = "A"
elif zuhair_marks >= 70:
    zuhair_grade = "B"
else:
    zuhair_grade = "Fail"

print(f"   • Marks : {zuhair_marks}")
print(f"   • Grade : {zuhair_grade}")

print("=" * 40)

# 3. Position Decision (Kiske Zyada Marks Hain?)
if bushra_marks > zuhair_marks:
    print("🏆 Top Scorer: Bushra!")
elif zuhair_marks > bushra_marks:
    print("🏆 Top Scorer: Zuhair!")
else:
    print("🤝 Both have Equal Marks!")

print("=" * 40)