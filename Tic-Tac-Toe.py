

def main():
    x = ["1","2"]
    while True:
        intro()
        y = input("Choose number: ")
        print()
        if y not in x:
            print("Choose only a given number")
            continue
        elif y == "1":
            game()
        elif y == "2":
            exit()
        

def intro():
    print("""
Tic-Tac-Toe

[1] - Play game
[2] - Exit

""")


def game():
    p1 = "ONE"
    p2 = "TWO"
    if marker():
        p2 = "ONE"
        p1 = "TWO"
    p = first()
    o = 2
    if p:
        o = 1
        print ("\n'x' is First \n")
    else:
        print("\n'O' is First \n")
    loc = {1:[],2:[]}
    while True and len(loc[1] + loc[2]) < 9:
        print_tic(loc,o)
        if p:
            z = input("Please Player {} 'X' enter number between 1 and 9: ".format(p1))
            print()
            if z.isdigit():
                if z not in loc[1] and z not in loc[2] and 1 <= int(z) <= 9:
                    p = False
                    loc[1].append(z)
                else:
                    print("Try again Player {} 'x' and pick a new number not chosen before and between 1 and 9 \n".format(p1))
                if check(loc[1]):
                    print_tic(loc,o)
                    print("Player {} 'X' WON\n\nTo play again press '1'".format(p1))
                    return
            else:
                print("Try again Player {} 'X' and enter a number only \n".format(p1))
                
        else:
            z = input("Please Player {} 'O' enter number between 1 and 9: ".format(p2))
            print()
            if z.isdigit():
                if z not in loc[1] and z not in loc[2] and  1 <= int(z) <= 9:
                    p = True
                    loc[2].append(z)
                else:
                    print("Try again Player {} 'O' and pick a new number not chosen before and between 1 and 9 \n".format(p2))
                if check(loc[2]):
                    print_tic(loc,o)
                    print("Player {}'O' WON\n\nTo play again press '1'".format(p2))
                    return
            else:
                print("Try again Player {} 'O' and enter a number only \n".format(p2))
    print("NO ONE WON\n\nTo play again press '1'")

def check(x = [], y = {1:["1","2","3"],2:["4","5","6"],3:["7","8","9"],4:["1","4","7"],5:["2","5","8"],6:["3","6","9"],7:["1","5","9"],8:["3","5","7"]}):
    t = 0
    for s in y:
        t = 0
        for i in y[s]:
            if i in x:
                t += 1
            if t == 3:
                return True
    return False

    
def print_tic(x = {1:[],2:[]},o = 1):
    xo = {"1":" 1 ","2":" | 2 | ","3":" 3 ","4":" 4 ","5":" | 5 | ","6":" 6 ","7":" 7 ","8":" | 8 | ","9":" 9 ",
          "10":"--------------",
          "11":" X ","12":" | X | ","13":" O ","14":" | O | "}
    y = x[1] + x[2]
    r = ["1","2","3","4","5","6","7","8","9"]
    t = 0
    f = 1
    g = 0
    st = ""
    if o == 1:
        while len(y) > t:
            if f == 1:
                if x[1][g] == "2" or x[1][g] == "5" or x[1][g] == "8":
                    r[int(x[1][g]) - 1] = "12"
                else:
                    r[int(x[1][g])-1] = "11"
                f = 0
            else:
                if x[2][g] == "2" or x[2][g] == "5" or x[2][g] == "8":
                    r[int(x[2][g]) - 1] = "14"
                else:
                    r[int(x[2][g])-1] = "13"
                f = 1
                g += 1
            t += 1
    else:
        while len(y) > t:
            if f == 1:
                if x[2][g] == "2" or x[2][g] == "5" or x[2][g] == "8":
                    r[int(x[2][g]) - 1] = "14"
                else:
                    r[int(x[2][g]) - 1] = "13"
                f = 0
            else:
                if x[1][g] == "2" or x[1][g] == "5" or x[1][g] == "8":
                    r[int(x[1][g]) - 1] = "12"
                else:
                    r[int(x[1][g]) - 1] = "11"
                f = 1
                g += 1
            t += 1
    t = 0
    for s in r:
        if t == 3:
            st +=  "\n" + xo["10"] + "\n"
            t = 0
        st += xo[s]
        t += 1
    print(st + "\n")

def marker():
    z = input("Player ONE pick 'x' or 'o': ")
    if z.lower() == "x":
        return False
    if z.lower() == "o":
        return True
    print("\nPick only either 'x' or 'o'")
    marker()

def first():
    import random as r
    x = r.randint(0,1)
    return x == 0

main()
        
        
            
            





