
  
# 1. Priyanshu's dictionary
priyanshu = { "name":"Priyansu Yadav",
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       } 
         
# 2. Prashant's dictionary
prashant = { "name":"Prashant Singh",
          "assignment" : [82, 56, 44, 30], 
          "test" : [80, 80], 
          "lab" : [67.90, 78.72] 
        } 
  
# 3. Pankaj's dictionary
pankaj = { "name" : "Pankaj Kesarkar",
          "assignment" : [77, 82, 23, 39], 
          "test" : [78, 77], 
          "lab" : [80, 80] 
        } 
          
# 4. Sule's dictionary
sule = { "name" : "Chetan Sule",
         "assignment" : [67, 55, 77, 21], 
         "test" : [40, 50], 
         "lab" : [69, 44.56] 
       } 
         
# 5. Abhishek's dictionary
abhishek = { "name" : "Abhishek Shriramwar",
        "assignment" : [29, 89, 60, 56], 
        "test" : [65, 56], 
        "lab" : [50, 40.6] 
      }
# 6. Lloyd's dictionary
lloyd = { "name" : "Lloyd Nadar",
        "assignment" : [49, 89, 50, 50],
        "test" : [60, 54],
        "lab" : [60, 42.6]
          }

  
# Function calculates average  
def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 
  
# Function calculates total average 
def calculate_total_average(students): 
    assignment = get_average(students["assignment"]) 
    test = get_average(students["test"]) 
    lab = get_average(students["lab"]) 
  

    return (0.1 * assignment +
            0.7 * test + 0.2 * lab) 
  # Calculate letter grade of each student 
def assign_letter_grade(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"
  

# average marks of the whole class 
def class_average_is(student_list): 
    result_list = [] 
  
    for student in student_list: 
        stud_avg = calculate_total_average(student) 
        result_list.append(stud_avg) 
        return get_average(result_list) 
  

students = [priyanshu, prashant, pankaj, sule, abhishek,lloyd]
  

# average marks and letter grade 
for i in students : 
    print(i["name"]) 
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
    print("Average marks of %s is : %s " %(i["name"], 
                         calculate_total_average(i))) 
                           
    print("Letter Grade of %s is : %s" %(i["name"], 
    assign_letter_grade(calculate_total_average(i)))) 
      
    print() 
  
  
# Calculate the average of whole class 
class_av = class_average_is(students) 
  
print( "Class Average is %s" %(class_av)) 
print("Letter Grade of the class is %s " 
        %(assign_letter_grade(class_av)))
