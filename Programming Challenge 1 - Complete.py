import time, random, sys, os, re
from statistics import median, mode
from linecache import getline
from getpass import getpass
def passReset():
    def updatePass(passwd, lineNo):
        lines = open('users.CRED').read().splitlines()
        # line = lines[lineNo-1].rstrip("\n\r")
        lines[lineNo-1] = str(passwd)
        open('users.CRED', 'w').write('\n'.join(lines))
    def valPass(pwd):
        if len(pwd) > 8:
            if (any(c.isupper() for c in pwd)):
                if (any(c.islower() for c in pwd)):
                    return True
                else:
                    return "there are No small case Letters"
            else:
              return "there are No capital Letters"
        else:
            return "the Password Has to contain ore than 8 characters"
    def checkForLine(lookup):
        with open("users.CRED") as f:
            for num, line in enumerate(f, 1):
                if lookup in line:
                    return num
        return False
    os.system('cls')
    print("Enter your credentials and if they exist and are correct you will then have the choice to change your password!")
    userName = str(input("Enter your username"))
    userpass = getpass(prompt='Enter your password:')
    
    uLine = checkForLine(userName)
    if uLine == False:
        print("username not found")
        input("Press enter to exit to menu")
        return 0
    pLine = uLine + 1

    username = getline('users.CRED', uLine)
    passwd = getline('users.CRED', pLine)

    if passwd.rstrip("\n\r") != str(userpass):
        input("Password Incorrect. Press Enter to exit!")
        return 0
    
    print("Alright! I Have now got your Username and have made sure it is really you")
    choice = input("Now do you still want to change your password? (Y/n)")

    if choice == "n":
        return 0

    ready = False
    while ready == False:
        newPass = getpass(prompt='Please Enter the new password')
        newPass1 = getpass(prompt='Please Enter the new password again')

        if newPass != newPass1:
            print("The passwords don't match. Please try again")
        else:
            ready = True
    res = valPass(newPass)
    if res == True:
        updatePass(newPass, pLine)
        print("Password Is valid and has been updated!")
        input("Press Enter to return to main menu")
        return 0
    else:
        print("Password Is not Valid and not changed becuase", res)
        input("Press Enter to return to main menu")
        return 0

    input()
def masterMind():
    os.system('cls')
    def hard():
        try:
            num = []
            for i in range(5):
                num.append(random.randint(0, 9))
            print(num)
            print("You have to guess 5 numbers and you dont have any hints. Good Luck")
            print("Hit enter when you are ready for the challenge")
            input()
            playing = True
            tries = 0
            while playing:
                userGuess = []
                for i in range(5):
                    inp = int(input("Enter a number"))
                    userGuess.append(inp)
                print(userGuess)
                if userGuess == num:
                    print("Well Done you got the right number")
                    print("It took you", tries, "tries.")
                    print("Press Enter to return to menu")
                    input()
                    os.system('cls')
                    return 0
                else:
                    print("Sorry your guess isnt right. Please try again.")
                    tries +=1
        except KeyboardInterrupt:
            return 0
    def easy():
            num = []
            for i in range(4):
                    num.append(random.randint(0, 9))
            print("This is the easy level \n you will have to guess the number")
            print("if you get a number wrong you will be told what number it was and what position")
            print("Ready? Press enter to start")
            input()
            playing = True
            trys = 0
            while playing == True:
                    userGuess = []
                    print("Number of trys:", str(trys))
                    for i in range(4):
                            inp = int(input("Enter a number"))
                            userGuess.append(inp)
                    for i in range(4):
                            if userGuess[i] == num[i]:
                                    print(userGuess[i], "is the right numeber and is in position", i+1)
                            else:
                              print("your postion", i+1, "number", userGuess[i], "is not right and not in the correct place")      
                    if userGuess == num:
                            print("Your guess is right press enter to exit")
                            input()
                            playing = False
                            return 0
                    else:
                            trys += 1
                            print("Wrong try. Try again")
                   
                    
                            
    os.system('cls')
    print("What level do you want?")
    print("1. Easy")
    print("2. Hard")
    print("3. Exit")
    inp = int(input())
    if inp == 1:
            easy()
    if inp == 2:
            hard()
    if inp ==3:
            os.system('cls')
            return 0


def numAverage(lst):
        avg = float(sum(lst)) / len(lst)
        return avg
        
def email():
        os.system('cls')
        def valEmail(email):
                if (' ' in email) == True:
                        fault = "There is a space in the email"
                        return fault
                if not re.match("[^@]+@[^@]+\.[^@]+", email):
                        
                        if ('@' in email) == False:
                                fault = "Missing the @ symbol"
                                return fault
                        if ('.com' in email) != True:
                                fault = "Missing suffix after the adress EG .com or .co.uk"
                                return fault
                        if ('.co.uk' in email) != True:
                                fault = "Missing suffix after the adress EG .com or .co.uk"
                                return fault
                
                return "Email Correct"
        def manVal():

                userInp = input("Enter your email")
                print(userInp, ":", valEmail(userInp))
                input("Press Enter to continue")
                return 0
        def autoVal():
                print("Make sure that there is a file called emailList.txt in the current directory and press enter to start the validation")
                input()
                with open("emailList.txt", "r") as ins:
                        emails = []
                        for i in ins:
                                 e =''.join(i.split('\n'))
                                 emails.append(e)

                for i in range(len(emails)):
                    print(emails[i], valEmail(emails[i]))
                input("Press Enter to continue")
                return 0

        print("What do you want to do?")
        print("1. Manually check email")
        print("2. Read From File")
        print("3. Return to menu")
        inp = int(input())

        if inp == 1:
                manVal()
        if inp == 2:
                autoVal()
        if inp == 3:
                   return 0
        else:
                email()

        os.system('cls')
        return 0

def numMath():
        os.system('cls')
        numLength = int(input("How may numbers do you want to enter?"))
        data = []
        for i in range(numLength):
                num = int(input("Enter a number"))
                data.append(num)
        print("The average of your numbers is:", numAverage(data))
        print("The median is:", median(data))
        print("The mode is:", mode(data))
        inp = input("Do you want to output the results to a text file? Y/N")
        if inp == "Y" or inp == "yes":
                data1 = str(data).strip('[]')
                dat = "Your Data: %s" % data1 + "\n"
                avg = "The Average %s" % numAverage(data) + "\n"
                med = "The median: %s" % median(data) + "\n"
                mod = "The mode: %s" % mode(data) + "\n"
                numMathFile = open("Data Analysis.txt", "w")
                numMathFile.write(dat)
                numMathFile.write(avg)
                numMathFile.write(med)
                numMathFile.write(mod)
                numMathFile.close()
                os.system('cls')
                return 
        else:
                os.system('cls')
                return 


while True:
        os.system('cls')
        print("######################################")
        print("# 1. Number Average, median and mode #")
        print("# 2. Validate your email             #")
        print("# 3. Master Mind guessing game       #")
        print("# 4. Password Reset                  #")
        print("# 5. Exit                            #")
        print("######################################")

        userInp = int(input("What do you want to do?"))

        if userInp == 1:
                numMath()
        if userInp == 2:
                email()
        if userInp == 3:
                masterMind()
        if userInp == 4:
                passReset()
        if userInp == 5:
                os.system('cls')
                print("Exiting. Good Bye")
                time.sleep(1)
                sys.exit()
        else:
                os.system('cls')