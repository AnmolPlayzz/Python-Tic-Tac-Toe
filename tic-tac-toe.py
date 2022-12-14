while True:
    print("""
        ----------------------------------------------------------
        |                      MAIN MENU                         |
        ----------------------------------------------------------
        |                                                        |
        |                                                        |
        |                 [1] Play Game                          |
        |                 [2] How to play?                       |
        |                 [3] Credits                            |
        |                                                        |
        |    Enter the respective number to select an option     |
        |                                                        |
        ----------------------------------------------------------
        """)
    mi=input(">>> ")
    if mi in "123" and mi!="":
        menu=int(mi)
        if menu==1:
            print("""
        ----------------------------------------------------------
        |                    GAME STARTED                        |
        |                       ======                           |
        |                    X GOES FIRST                        |
        ----------------------------------------------------------
        """)
            l="         "
            end=True
            done=""
            t="X"
            win=""
            while end!=False:
                while t=="X":
                    xi=input("X: ")
                    if xi in "123456789" and xi!="":
                        x=int(xi)-1
                        if x>=0 and x<=8:
                            if str(x) not in done:
                                l=l[0:x]+"X"+l[x+1:9]
                                done+=str(x)
                                t="O"
                            else:
                                print("""
That box is already occupied
Don't try to break our game -_-
                                """)
                                continue
                        else:
                            print("Enter a value from 1-9")
                    else:
                        print("Enter a value from 1-9")
                print("\n")
                print(" "+l[0]+" | "+l[1]+" | "+l[2]+"")
                print("-----------")
                print(" "+l[3]+" | "+l[4]+" | "+l[5]+"")
                print("-----------")
                print(" "+l[6]+" | "+l[7]+" | "+l[8]+"")
                if l[0]==l[1]==l[2]=="X" or l[3]==l[4]==l[5]=="X" or l[6]==l[7]==l[8]=="X" or l[0]==l[3]==l[6]=="X" or l[1]==l[4]==l[7]=="X" or l[2]==l[5]==l[7]=="X" or l[0]==l[4]==l[8]=="X" or l[2]==l[4]==l[6]=="X":
                    print("""
        -------------------------------------
                    Good Game 🎉
                      =====
                  X WON THE GAME!
        -------------------------------------
                    """)
                    end=False
                    break
                elif l[0]==l[1]==l[2]=="O" or l[3]==l[4]==l[5]=="O" or l[6]==l[7]==l[8]=="O" or l[0]==l[3]==l[6]=="O" or l[1]==l[4]==l[7]=="O" or l[2]==l[5]==l[7]=="O" or l[0]==l[4]==l[8]=="O" or l[2]==l[4]==l[6]=="O":
                    print("""
        -------------------------------------
                    Good Game 🎉
                      =====
                  O WON THE GAME!
        -------------------------------------
                    """)
                    end=False
                    break
                elif l.count("O")+l.count("X")==9:
                    print("""
        -------------------------------------
                   Good Game 🎉
                     =====
                      TIE
        -------------------------------------
                    """)
                    end=False
                    break
                else:
                    pass
                while t=="O":
                    oi=input("O: ")
                    if oi in "123456789" and oi!="":
                        o=int(oi)-1
                        if o>=0 and o<=8:
                            o=int(oi)-1
                            if str(o) not in done:
                                l=l[0:o]+"O"+l[o+1:9]
                                done+=str(o)
                                t="X"
                            else:
                                print("""
That box is already occupied
Don't try to break our game -_-
                                """)
                                continue
                        else:
                            print("Enter a value from 1-9")
                    else:
                        print("Enter a value from 1-9")
                print("\n")
                print(" "+l[0]+" | "+l[1]+" | "+l[2]+"")
                print("-----------")
                print(" "+l[3]+" | "+l[4]+" | "+l[5]+"")
                print("-----------")
                print(" "+l[6]+" | "+l[7]+" | "+l[8]+"")
                #Checks
                if l[0]==l[1]==l[2]=="X" or l[3]==l[4]==l[5]=="X" or l[6]==l[7]==l[8]=="X" or l[0]==l[3]==l[6]=="X" or l[1]==l[4]==l[7]=="X" or l[2]==l[5]==l[7]=="X" or l[0]==l[4]==l[8]=="X" or l[2]==l[4]==l[6]=="X":
                    print("""
        -------------------------------------
                    Good Game 🎉
                      =====
                  X WON THE GAME!
        -------------------------------------
                    """)
                    end=False
                    break
                elif l[0]==l[1]==l[2]=="O" or l[3]==l[4]==l[5]=="O" or l[6]==l[7]==l[8]=="O" or l[0]==l[3]==l[6]=="O" or l[1]==l[4]==l[7]=="O" or l[2]==l[5]==l[7]=="O" or l[0]==l[4]==l[8]=="O" or l[2]==l[4]==l[6]=="O":
                    print("""
        -------------------------------------
                   Good Game 🎉
                     =====
                 O WON THE GAME!
        -------------------------------------
                    """)
                    end=False
                    break
                elif l.count("O")+l.count("X")==9:
                    print("""
        -------------------------------------
                   Good Game 🎉
                     =====
                      TIE
        -------------------------------------
                    """)
                    end=False
                    break
                else:
                    pass
        elif menu==2:
            print("""
            ----------------------------------------------------------
                                   HOW TO PLAY
            ----------------------------------------------------------
                How to play:
                    1. The game will ask for inputs in this pattern:

                        >>>|X: 2
                           |
                           |
                           |    | X |
                           | -----------
                           |    |   |
                           | -----------
                           |    |   |
                           |
                        >>>|O: 5
                           |
                           |    | X |
                           | -----------
                           |    | O |
                           | -----------
                           |    |   |

                    2. Every box in the grid has a number as per this grid:

                        1 | 2 | 3
                       -----------
                        4 | 5 | 6
                       -----------
                        7 | 8 | 9

                    3. To place your sign in a box you'll enter the number in the prompt

                        Say you wanna add your x to box 2
                        This would look something like this-

                        >>>|X: 2
                           |
                           |    | X |
                           | -----------
                           |    |   |
                           | -----------
                           |    |   |
        ----------------------------------------------------------
        |              PRESS AMY KEY TO GO BACK                  |
        ----------------------------------------------------------
            """)
            ext=input()
            if ext==ext:
                pass
        if menu==3:
            print("""
        ----------------------------------------------------------
        |                       CREDITS                          |
        ----------------------------------------------------------
        |                                                        |
        |   1. Anmol Sharma                                      |
        |   2. Aryaman Sharma                                    |
        |                                                        |
        |   XI - A                                               |
        |   Source code available at:                            |
        |   https://github.com/AnmolPlayzz/Python-Tic-Tac-Toe    |
        |                                                        |
        |   LICENSED UNDER THE MIT LICENSE                       |
        |                                                        |
        ----------------------------------------------------------
        |              PRESS AMY KEY TO GO BACK                  |
        ----------------------------------------------------------
    """)
            ext1=input()
            if ext1==ext1:
                pass
    else:
        print("""
INVALID INPUT!
        """)
        pass
