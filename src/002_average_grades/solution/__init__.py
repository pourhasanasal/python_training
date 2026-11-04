def average_grades():
    print('Hello lets average your grades: ')

    grades=[]

    while True:
        grade=input("enter your grade or type 'finish' for seeing result : ")

        if grade=="finish":
            break

        try:
            grades.append(float(grade))
        except ValueError:
            print("only grade or 'finish' for stop")
       

    if len(grades) == 0:
        return "no grades entered"
    
    return sum(grades) / len(grades)

print(average_grades())



