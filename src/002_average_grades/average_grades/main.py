def main():

    print('Hello lets average your grades: ')

    grades=[]

    while True:
        grade=input("enter your grade or type 'done' for seeing result : ")

        if grade=="done":
            break

        try:
            grades.append(float(grade))
        except ValueError:
            print("only grade or 'finish' for stop")
       

    if len(grades) == 0:
        return "no grades entered"
    
    return sum(grades) / len(grades)
if __name__ == "__main__":
    print(main())
