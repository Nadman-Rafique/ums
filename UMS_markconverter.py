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
    o = x*(y/Tm) 
    # o = obtained mark converted to the max mark in the standard scale for the subject and unit
    return  o
def type_selection_ums(type_selection,s,U):
    if type_selection == 1 : 
            Tm = input_with_validation(" Input the total mark for the paper >>> ", "Invalid input. Please enter a valid integer for the total mark.",0)  
            while True:                    
                o = marks(Tm,s,U) 
                gb = {(1,1,0): (69,63,0), (1,2): (65,60,0), (1,3): (69,64,0), (1,4): (70,64,0), (1,5): (75,70,0), (1,6): (75,70,0), 
                (2,1): (80,0,0), (2,2): (80,0,0), (2,3): (50,0,0), (2,4): (90,0,0), (2,5): (90,0,0), (2,6): (50,0,0),
                (3,1): (80,0,0), (3,2): (80,0,0), (3,3): (50,0,0), (3,4): (90,0,0), (3,5): (90,0,0), (3,6): (50,0,0), 
                (4,1): (80,0,0), (4,2): (80,0,0), (4,3): (50,0,0), (4,4): (90,0,0), (4,5): (90,0,0), (4,6): (50,0,0),
                (5,1): (75,0,0), (5,2): (75,0,0), (5,3): (75,0,0), (5,4): (75,0,0), (5,5): (75,0,0), (5,6): (75,0,0), (5,7): (75,0,0) }
                # gb = grade boundaries for the subject and unit  if not found it will be equal to (0,0) which means that the standard scale will be used without any adjustments and 
                # the third element is the reduction factor for the standard scale.
                gb_max = gb.get((s,U,0), (0,0,0))[0]
                gb_min = gb.get((s,U,0), (0,0,0))[1]          
                             
                Grades =[[ o , gb_max , gb_min , 100 , 90 ], [ o , 64 , 55 , 89 , 80 ],
                         [ o , 54 , 50 , 79 , 70  ],[ o , 49 , 45 , 69 , 60 ], 
                         [ o , 44 , 40 , 59 , 50 ], [ o , 39 , 30 , 49 , 40 ],
                         [ o , 29 , 0 ,  39 , 0 ] ]
                # Grades = list of lists where each inner list represents a grade boundary and the corresponding UMS marks. The first element is the obtained mark, the second and third elements 
                # are the upper and lower grade boundaries, and the fourth and fifth elements are the corresponding UMS marks for those boundaries.
                for grade in Grades :
                    if o >= grade[2]:
                        ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                        if ums > 100:
                            print("UMS Mark = 100")
                        elif ums <= 100 :
                            print(f"UMS mark = {ums}")
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
                    Grades =[  [ o , 70 , A, 100 , 90 ], [ o , A - 1 , a , 89 , 80 ],[ o , a -1  , b , 79 , 70  ],[ o , b-1 , c , 69 , 60 ], [ o , c -1  , d , 59 , 50 ], [ o , d - 1 , d-10 , 49 , 40 ],[ o , d-11 , 0 ,  39 , 0 ] ]
                    for grade in Grades :
                        if o >= grade[2]:
                            ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                            if ums > 100:
                                print("UMS Mark = 100")
                            elif ums <= 100 :
                                print(f"UMS mark = {ums}")
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
    print("  Welcome to the Standard edexcel UMS Converter  ") 
    subject = ['1. Pure Mathematics hello' , 
               '2. Physics', 
               '3. Chemistry ' , 
               '4. Biology' , 
               '5. Further Pure Mathematics' 
               ]
    print(subject)
    s = input_with_validation("Select subject >>>>  ", "Invalid subject selection. Please choose a valid subject number.",1)
    unit = {1: ['1. P1', '2. P2', '3. P3', '4. P4', '5. M1', '6. S1'], 
            2: ['1. Unit 1', '2. Unit 2', '3. Unit 3', '4. Unit 4', '5. Unit 5', '6. Unit 6'], 
            3: ['1. Unit 1', '2. Unit 2', '3. Unit 3', '4. Unit 4', '5. Unit 5', '6. Unit 6'],
            4: ['1. Unit 1', '2. Unit 2', '3. Unit 3', '4. Unit 4', '5. Unit 5', '6. Unit 6'], 
            5: ['1. FP1', '2. FP2', '3. FP3', '4. S2', '5. M2', '6. S3' , '7. S3'] }
    print(unit.get (s, "Invalid subject selection. Please choose a valid subject number."))
    U = input_with_validation("Select unit >>>>  ", "Invalid unit selection. Please choose a valid unit number.",1)
    type_selection = input_with_validation("1. Standard UMS or 2. Custom UMS >>  ", "Invalid selection. Please enter 1 or 2.",1)
    type_selection_ums(type_selection,s,U)

        
if __name__ == "__main__":
    keep_running = "y" 
    while keep_running == "y":
        main()
        keep_running = input("Do you want to run the program again (yes: y / No : N)")
    print("Program closed. Have a great day!")
    