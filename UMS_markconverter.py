def converter(o,m,n,Rm,rm):
        return rm + abs((Rm - rm)*((o-n)/(m-n)))
 # o = obtained mark  m = max mark  n = minimum mark   Rm = Max of garde  rm = minimum of grade
def marks(Tm,s,U):
    # Tm = total mark  s = subject  U = unit
    m_su = {(1,1): 75, (1,2): 75, (1,3): 75, (1,4): 75, (1,5): 75, (1,6): 75, 
            (2,1): 80, (2,2): 80, (2,3): 50, (2,4): 90, (2,5): 90, (2,6): 50,
            (3,1): 80, (3,2): 80, (3,3): 50, (3,4): 90, (3,5): 90, (3,6): 50, 
            (4,1): 80, (4,2): 80, (4,3): 50, (4,4): 90, (4,5): 90, (4,6): 50,
            (5,1): 75, (5,2): 75, (5,3): 75, (5,4): 75, (5,5): 75, (5,6): 75}
    y = m_su.get((s,U), Tm)
    # y = max mark for the subject and unit  if not found it will be equal to total mark
    x = input_with_validation(" Input the mark obtained >>> ","Invalid input. Please enter a valid integer for the obtained mark.",0)
    # x = obtained mark
    o = x*(y/round(Tm)) 
    # o = obtained mark converted to the max mark in the standard scale for the subject and unit
    return  o
def type_selection_ums(type_selection,s,U):
    if type_selection == 1 : 
            Tm = input_with_validation(" Input the total mark for the paper >>> ", "Invalid input. Please enter a valid integer for the total mark.",0)  
            while True:                    
                o = marks(Tm,s,U) 
                gb = {(1,1,0): (69,63,6), (1,2,0): (65,60,6), (1,3,0): (69,64,5), (1,4,0): (70,64,6), (1,5,0): (75,70,7), (1,6,0): (75,70,8), 
                (2,1,0): (75,65,7), (2,2,0): (73,63,7), (2,3,0): (44,41,4), (2,4,0): (90,80,7), (2,5,0): (87,79,7), (2,6,0): (48,43,4),
                (3,1,0): (80,72,7), (3,2,0): (76,69,8), (3,3,0): (46,43,5), (3,4,0): (90,81,7), (3,5,0): (80,73,6), (3,6,0): (43,39,5),
                (4,1,0): (66,60,5), (4,2,0): (70,64,6), (4,3,0): (48,45,4), (4,4,0): (67,61,5), (4,5,0): (74,67,5), (4,6,0): (48,45,3),
                (5,1,0): (75,70,6), (5,2,0): (75,71,5), (5,3,0): (75,64,5), (5,4,0): (74,67,6), (5,5,0): (70,62,5), (5,6,0): (75,70,6), (5,7,0): (74,70,6) }
                # gb = grade boundaries for the subject and unit  if not found it will be equal to (0,0) which means that the standard scale will be used without any adjustments and 
                # the third element is the reduction factor for the standard scale.
                gb_max = gb.get((s,U,0), (0,0,0))[0]
                gb_min = gb.get((s,U,0), (0,0,0))[1]          
                reduction_factor = gb.get((s,U,0), (0,0,0))[2]  
                def grade_boundaries(gb_max, gb_min, reduction_factor,grade,maximum):
                    base = gb_min if maximum == 1 else gb_max
                    return base - reduction_factor * grade - grade
                    # grade_boundaries function calculates the lower boundary for a given grade(1 for A , 2 for b and so on) based on the maximum and minimum grade boundaries and the reduction factor. 
                    # It uses a dictionary to store the calculated boundaries for each grade.
                if s in (2, 3, 4) and U in (1, 2, 4, 5):
                    Rm = 120
                elif s in (2, 3, 4) and U in (3, 6):
                    Rm = 60 
                else:
                    Rm = 100
                # Maximum UMS mark for the subject and unit varies based on the subject and unit selection.
                # For certain subjects and units, the maximum UMS mark is 120 or 60; otherwise it is 100.
                Grades =[[ o , gb_max , gb_min , Rm , Rm*0.9 ], [ o , gb_min-1 , grade_boundaries(gb_max, gb_min, reduction_factor,1,1) , Rm*0.9 -1 , Rm*0.8 ],#A
                         [ o , grade_boundaries(gb_max, gb_min, reduction_factor,1,1)-2 , grade_boundaries(gb_max, gb_min, reduction_factor,2,1) , Rm*0.8 -1 , Rm*0.7 ],#B
                         [ o , grade_boundaries(gb_max, gb_min, reduction_factor,2,1)-1 , grade_boundaries(gb_max, gb_min, reduction_factor,3,1) , Rm*0.7 -1 , Rm*0.6 ],#C 
                         [ o , grade_boundaries(gb_max, gb_min, reduction_factor,3,1)-1 , grade_boundaries(gb_max, gb_min, reduction_factor,4,1) , Rm*0.6 -1 , Rm*0.5 ],#D
                         [ o , grade_boundaries(gb_max, gb_min, reduction_factor,4,1)-1 , grade_boundaries(gb_max, gb_min, reduction_factor,5,1) , Rm*0.5 -1 , Rm*0.4 ],#E
                         [ o , grade_boundaries(gb_max, gb_min, reduction_factor,5,1)-1 , 0 ,  Rm*0.4 -1 , 0 ] ] #U
                # Grades = list of lists where each inner list represents a grade boundary and the corresponding UMS marks. The first element is the obtained mark, the second and third elements 
                # are the upper and lower grade boundaries, and the fourth and fifth elements are the corresponding UMS marks for those boundaries.
                for grade in Grades :
                    if o >= grade[2]:
                        ums = round(converter( o, grade[1],grade[2], grade[3],grade[4]))
                        if (s in (2, 3) and U in (1, 2, 4, 5)):
                            if ums > 120:
                                print("UMS Mark = 120")
                            else:
                                print(f"UMS mark = {min(ums, 120)}")
                        elif (s in (2, 3) and U in (3, 6)):
                            if ums > 60:
                                print("UMS Mark = 60")
                            else:
                                print(f"UMS mark = {min(ums, 60)}")
                        else:
                            if ums > 100:
                                print("UMS Mark = 100")
                            else:
                                print(f"UMS mark = {min(ums, 100)}")
                        break
                another = input("Do you want to convert another mark with the same boundaries (yes: y / No : N) ")
                if another != "y":
                    break
                                           
    elif type_selection == 2 :
                Tm= input_with_validation(" Input the total mark for the paper >>> ", "Invalid input. Please enter a valid integer for the total mark.",0)
                A = input_with_validation(" Input the lower boundary for A* >> ", "Invalid input. Please enter a valid integer ",0)
                a = input_with_validation(" Input the lower boundary for A >>  ", "Invalid input. Please enter a valid integer ",0)
                b = input_with_validation(" Input the lower boundary for B >>  ", "Invalid input. Please enter a valid integer ",0)
                c = input_with_validation(" Input the lower boundary for C >>  ", "Invalid input. Please enter a valid integer ",0)
                d = input_with_validation(" Input the lower boundary for D >>  ", "Invalid input. Please enter a valid integer ",0)
                while True:
                    o = marks(Tm,s,U)
                    if s in (2, 3, 4) and U in (1, 2, 4, 5):
                        Rm = 120
                    elif s in (2, 3, 4) and U in (3, 6):
                        Rm = 60 
                    else:
                        Rm = 100
                    # Maximum UMS mark for the subject and unit varies based on the subject and unit selection.
                    # For certain subjects and units, the maximum UMS mark is 120 or 60; otherwise it is 100.
                    Grades =[  [ o , 70, A, Rm , Rm*0.9 ], [ o, A-1, a, Rm*0.9 -1 , Rm*0.8 ],
                               [ o , a-1, b, Rm*0.8 -1 , Rm*0.7 ], [ o, b-1, c, Rm*0.7 -1 , Rm*0.6 ], 
                               [ o , c-1, d, Rm*0.6 -1 , Rm*0.5 ], [ o , d-1, d-10, Rm*0.5 -1 , Rm*0.4 ],
                               [ o , d-11, 0, Rm*0.4 -1 , 0 ] ]
                    for grade in Grades :
                        if o >= grade[2]:
                            ums = round(converter( o, grade[1],grade[2], grade[3],grade[4]))
                            if (s in (2, 3) and U in (1, 2, 4, 5)):
                                if ums > 120:
                                    print("UMS Mark = 120")
                                else:
                                    print(f"UMS mark = {min(ums, 120)}")
                            elif (s in (2, 3) and U in (3, 6)):
                                if ums > 60:
                                    print("UMS Mark = 60")
                                else:
                                    print(f"UMS mark = {min(ums, 60)}")
                            else:
                                if ums > 100:
                                    print("UMS Mark = 100")
                                else:
                                    print(f"UMS mark = {min(ums, 100)}")
                            break
                    another = input("Do you want to convert another mark with the same boundaries (yes: y / No : N) ")
                    if another != "y":
                        break  
def input_with_validation(prompt, error_message,Int_float):
    while True:
        try:
            if Int_float == 1:
                return int(input(prompt))
            else:
                return float(input(prompt))
        except ValueError:
            print(error_message)
def main():
    print("  Welcome to the Standard Edexcel UMS Converter  ") 
    subject = ['1. Pure Mathematics ' , 
               '2. Physics', 
               '3. Chemistry ' , 
               '4. Biology' , 
               '5. Further Pure Mathematics' 
               ]
    for item in subject:
        print(item)
    while True:
        s = input_with_validation("Select subject >>>>  ", "Invalid subject selection. Please choose a valid subject number.",1)
        if s in range(0,6):
            break
        print("Invalid subject selection. Please choose a valid subject number.")
    unit = {1: ['1. P1', '2. P2', '3. P3', '4. P4', '5. M1', '6. S1'], 
            2: ['1. Unit 1', '2. Unit 2', '3. Unit 3', '4. Unit 4', '5. Unit 5', '6. Unit 6'], 
            3: ['1. Unit 1', '2. Unit 2', '3. Unit 3', '4. Unit 4', '5. Unit 5', '6. Unit 6'],
            4: ['1. Unit 1', '2. Unit 2', '3. Unit 3', '4. Unit 4', '5. Unit 5', '6. Unit 6'], 
            5: ['1. FP1', '2. FP2', '3. FP3', '4. S2', '5. M2', '6. M3' , '7. S3'] }
    print(unit.get (s, "Invalid subject selection. Please choose a valid subject number."))
    while True:
        if s == 5:
            U = input_with_validation("Select unit >>>>  ", "Invalid unit selection. Please choose a valid unit number.",1)
            if U in range(0,8):
                break
            print("Invalid unit selection. Please choose a valid unit number.")
        else:
            U = input_with_validation("Select unit >>>>  ", "Invalid unit selection. Please choose a valid unit number.",1)
            if U in range(0,7):
                break
            print("Invalid unit selection. Please choose a valid unit number.")
    while True:
        type_selection = input_with_validation(" 1. Standard scale with grade boundaries \n 2. Standard scale with custom grade boundaries ", "Invalid selection. Please choose either 1 or 2.",1)
        if type_selection in [1,2]:
            break
        print("Invalid selection. Please choose either 1 or 2.")
    type_selection_ums(type_selection,s,U)

        
if __name__ == "__main__":
    keep_running = "y" 
    while keep_running == "y":
        main()
        keep_running = input("Do you want to run the program again (yes: y / No : N)")
    print("Program closed. Have a great day!")
    