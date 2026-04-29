print("  Welecome to the Standard edexcel UMS Converter ") 
subject = [ "1. Pure Mathematics" , "2. Physics" , " 3. Chemistry " , "4. Biology" , "5. Further Pure Mathematics" ]
print(subject)
s = int(input( "  Choose your subject from above (e.g 2 for Physics )>>> " ))
def converter(o,m,n,Rm,rm):
    return rm + abs((Rm - rm)*((o-n)/(m-n)))
# o = obtained mark  m = max mark  n = minimum mark   Rm = Max of garde  rm = minimum of grade
if s == 1:
    print("Unit: 1. P1   2. P2   3. P3   4. P4   5.M1   6. S1")
    U= int(input("Select unit >>>>  "))
    if U == 1 :
        type_selection = int(input ( "1. Standard UMS or 2. Custom UMS >>  "))
        if type_selection == 1 : 
            x = int(input(" Obtained Marks:  "))
            Tm =int(input(" Total mark of the paper:  "))
            o = x*(75/Tm) 
            Grades =[  [ o , 70 , 65 , 100 , 90 ], [ o , 64 , 55 , 89 , 80 ],[ o , 54 , 50 , 79 , 70  ],[ o , 49 , 45 , 69 , 60 ], [ o , 44 , 40 , 59 , 50 ], [ o , 39 , 30 , 49 , 40 ],[ o , 29 , 0 ,  39 , 0 ] ]
            for grade in Grades :
                 if o >= grade[2]:
                    ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                    if ums > 100:
                        print(f"UMS Mark = 100")
                    elif ums <= 100 :
                        print(f"UMS mark = {ums}")
                    break
        elif type_selection == 2 :
            x = int(input(" Obtained Marks:  "))
            Tm =int(input(" Total mark of the paper:  "))
            o = x*(75/Tm) 
            A = int(input(" Input the lower boundary for A* >> "))
            a = int(input(" Input the lower boundary for A >>  "))
            b = int(input(" Input the lower boundary for B >>  "))
            c = int(input(" Input the lower boundary for C >>  "))
            d = int(input(" Input the lower boundary for D >>  "))
            Grades =[  [ o , 70 , A, 100 , 90 ], [ o , A - 1 , a , 89 , 80 ],[ o , a -1  , b , 79 , 70  ],[ o , b-1 , c , 69 , 60 ], [ o , c -1  , d , 59 , 50 ], [ o , d - 1 , d-10 , 49 , 40 ],[ o , d-11 , 0 ,  39 , 0 ] ]
            for grade in Grades :
                 if o >= grade[2]:
                    ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                    if ums > 100:
                        print(f"UMS Mark = 100")
                    elif ums <= 100 :
                        print(f"UMS mark = {ums}")
                    break
    elif U == 2 :
        type_selection = int(input ( "1. Standard UMS or 2. Custom UMS >>  "))
        if type_selection == 1 : 
            x = int(input(" Obtained Marks:  "))
            Tm =int(input(" Total mark of the paper:  "))
            o = x*(75/Tm) 
            Grades =[  [ o , 75 , 65 , 100 , 90 ], [ o , 64 , 55 , 89 , 80 ],[ o , 54 , 50 , 79 , 70  ],[ o , 49 , 45 , 69 , 60 ], [ o , 44 , 40 , 59 , 50 ], [ o , 39 , 30 , 49 , 40 ],[ o , 29 , 0 ,  39 , 0 ] ]
            for grade in Grades :
                if o >= grade[2]:
                    ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                    print(f"UMS Mark = {ums}")
                    break
        elif type_selection == 2 :
            x = int(input(" Obtained Marks:  "))
            Tm =int(input(" Total mark of the paper:  "))
            o = x*(75/Tm) 
            A = int(input(" Input the lower boundary for A* >> "))
            a = int(input(" Input the lower boundary for A >>  "))
            b = int(input(" Input the lower boundary for B >>  "))
            c = int(input(" Input the lower boundary for C >>  "))
            d = int(input(" Input the lower boundary for D >>  "))
            Grades =[  [ o , 75 , A, 100 , 90 ], [ o , A - 1 , a , 89 , 80 ],[ o , a -1  , b , 79 , 70  ],[ o , b-1 , c , 69 , 60 ], [ o , c -1  , d , 59 , 50 ], [ o , d - 1 , d-10 , 49 , 40 ],[ o , d-11 , 0 ,  39 , 0 ] ]
            for grade in Grades :
                 if o >= grade[2]:
                     ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                     print(f"UMS Mark = {ums}")
                     break
    elif U == 3 :
        type_selection = int(input ( "1. Standard UMS or 2. Custom UMS >>  "))
        if type_selection == 1 : 
            x = int(input(" Obtained Marks:  "))
            Tm =int(input(" Total mark of the paper:  "))
            o = x*(75/Tm) 
            Grades =[  [ o , 72 , 67 , 100 , 90 ], [ o , 66 , 60 , 89 , 80 ],[ o , 59 , 55 , 79 , 70  ],[ o , 54 , 47 , 69 , 60 ], [ o , 46 , 39 , 59 , 50 ], [ o , 38 , 30 , 49 , 40 ],[ o , 29 , 0 ,  39 , 0 ] ]
            for grade in Grades :
                 if o >= grade[2]:
                    ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                    if ums > 100:
                        print(f"UMS Mark = 100")
                    elif ums <= 100 :
                        print(f"UMS mark = {ums}")
                    break
        elif type_selection == 2 :
            x = int(input(" Obtained Marks:  "))
            Tm =int(input(" Total mark of the paper:  "))
            o = x*(75/Tm) 
            A = int(input(" Input the lower boundary for A* >> "))
            a = int(input(" Input the lower boundary for A >>  "))
            b = int(input(" Input the lower boundary for B >>  "))
            c = int(input(" Input the lower boundary for C >>  "))
            d = int(input(" Input the lower boundary for D >>  "))
            Grades =[  [ o , 75 , A, 100 , 90 ], [ o , A - 1 , a , 89 , 80 ],[ o , a -1  , b , 79 , 70  ],[ o , b-1 , c , 69 , 60 ], [ o , c -1  , d , 59 , 50 ], [ o , d - 1 , d-10 , 49 , 40 ],[ o , d-11 , 0 ,  39 , 0 ] ]
            for grade in Grades :
                 if o >= grade[2]:
                    ums = converter( o, grade[1],grade[2], grade[3],grade[4])
                    print(f"UMS Mark = {ums}")
                    break
                