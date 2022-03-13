# menu function
def procMenu():
    print('''welcome to the number converter
what would you like to do
    
    1: convert binary to denary
    
    2: convert denary to binary
    
    3: quit program''')
    valid = False # input validation
    while valid == False:
        menuChoice = input(">")
        if menuChoice == '1': # binary to denary
            valid == True
            procBinDen()
            break
        elif menuChoice == '2': # denary to binary
            valid == True
            procDenBin()
            break
        elif menuChoice == '3': # quit
            valid == True
            print("thank you for using this program, have a cool day")
            quit()
        else:
            print("invalid input, please enter either 1, 2 or 3")
        
# binary to denary conversion function
def procBinDen():
    print("binary to denary converter")
    binary = input("enter binary number for conversion - maximum 8 bits: ")
    valid = False
    while valid == False:
        try:
            if len(binary) > 8:
                print("error: inputted value exceeds 8 bits")
                procEnd()
                break
            else:
                valid == True
                denary = 0
                for digit in binary:
                    denary = denary * 2 + int(digit)
                print(str(binary) + " in denary is " + str(denary))
                procEnd()
                break
        except:
            print("invalid value, please enter a binary number")
            procEnd()
            
# denary to binary conversion function - LACKS PROPER VALIDATION
def procDenBin():
    print("denary to binary converter")
    denaryInput = int(input("enter denary number for conversion: "))
    try:
        denary = denaryInput
        binary = ""
        while denary > 0:
            binary = str(denary%2) + binary
            denary = denary // 2
        print(str(denaryInput) + " in binary is " + str(binary))
        procEnd()
    except:
        print("invalid input")

# 'end screen' - either the conversion has finished or an invalid value was entered
def procEnd():
    print('''
what would you like to do

    1. return to menu
    
    2. quit program''')
    valid = False
    while valid == False:
        endChoice = input(">")
        if endChoice == '1': # back to menu
            valid == True
            procMenu()
            break
        elif endChoice == '2': # quit
            valid == True
            print("thank you for using this program, have a cool day")
            quit()
        else:
            print("invalid input, please enter either 1 or 2")

#actual program
procMenu()

# i really wish python had a GOTO command
# BASIC has made me lazy
