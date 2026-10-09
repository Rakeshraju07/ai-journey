students = {}
students["Asha"]= 82


def add_student(students,name,score):
  if score<0:
    print("Score can't be negative")
  else:
    
    if name in students:
      print(f"{name} Already exists")
    else:
      students[name] = score

def update_score(students, name , new_score):
  if name in students:
    if new_score<0:
      print("Score cannot be negative")
    else:
      students[name] = new_score
      print(f"{name} score updated successfully")
  else:
    print(f"{name} not found")

def average_score(students):
  if len(students)==0:
    return 0
  total = sum(students.values())
  return total/len(students)

def topper(students):
  best_name = None
  best_score = -1
  for name,score in students.items():
    if score > best_score:
      best_score = score
      best_name = name
  return best_name

def show_all(students):
  for name,score in students.items():
    print(f"{name}: {score}")
  

add_student(students, "Ravi", 67)    # should add
add_student(students, "Ravi", 50)    # should refuse
add_student(students, "Meera", -5)   # should refuse                     # {'Ravi': 67}

update_score(students, "Asha", 90)
update_score(students, "Karan", 75)
print(students)  
average = average_score(students)
print(average)
print(topper(students))   # Asha
print(topper({}))  
show_all(students)