#Tara Prole
#October 29, 2021
#A4_TaraProle.py
#To create a password generator using a specific set of guidelines.

'''
Student Name: Tara
Be a length of 7 characters long.
Must include special characters of % and $.
Not use any form of the word Havergal.
'''

#IMPORTING MODULES
from random import randint
import time
import tkinter as tk

#DEFINING FUNCTIONS
'''This function prints the statement then waits two seconds before moving onto the next action.
Useful for introduction as it gives people time to read one sentence before moving on to the other, encouraging them to read everything instead of skimming.
This will reduce frustration as they will read the instructions about how to avoid errors and get their passwords in correctly.'''

def printSleep(argument):
    print(argument)
    time.sleep(2)

'''This function is a function for getting input keywords.'''
def addKeyword(category):
    global keywords
    while True: #repeats the process as long as the keyword is invalid
        keyword = input(category) #category is basically the output before the input; the question being asked
        keyword = keyword.replace(' ', '') #removing spaces to avoid errors / spaces in the password
        keyword = keyword.lower() #making the word lowercase
        if 'havergal' in keyword: #CRITERIA- if the word Havergal is in the password it is not added
            print('No use of the word "Havergal!"')
        elif keyword == "n/a": #n/a skips the question
            break
        elif keyword in keywords:
            print("Duplicate keyword. Try again.")
        elif len(keyword) < 3:
            print("This keyword is too short. Please type in keywords that are 3 letters or longer.")
        elif keyword.isalpha() == True: #making sure the keyword is a word and there are no numbers, etc.
            keywords.append(keyword)
            break
        else: #otherwise the input is invalid, so you have to input the keyword again
            print("Invalid input!")


passwordList = [] #to store passwords. I'm defining this outside the function so I can use it later on

def generatePassword():
    global passwordList

    passwordGenerated = False #making a while loop so that duplicate passwords can be OBLITERATED
    '''Making a list of password options'''
    while passwordGenerated == False:
        #a variable just in case we get duplicate passwords, this stores how many extra should be generated
        '''Choosing a keyword'''
        if i <= len(keywords)-1: #using the given keywords in order
            chosen_keyword = keywords[i]
        else: #once the list has been cycled through once, use random keywords from the list to fill the rest of the 10
            chosen_keyword = keywords[randint(0, len(keywords)-1)]

        '''Replacing any letter S's within the password index area with the dollar sign'''
        if 's' in chosen_keyword[0:6]:
            chosen_keyword = chosen_keyword.replace('s', '$')
            
        '''Chopping longer keywords into 6-letter chunks'''
        if len(chosen_keyword) >= 6:
            if "$" not in chosen_keyword: #the $ needs to be added later so a smaller chunk of the word should be taken
                chosen_keyword = chosen_keyword[0:5]
            else: #the $ is already in it so we just need a %
                chosen_keyword = chosen_keyword[0:6]

        '''Choosing a random place to insert the percent sign'''
        sliceyPlace = randint(0, 5)

        '''Inserting the percent sign at the slicey place'''
        firstSection = chosen_keyword[:sliceyPlace] #storing the part of the word before the %
        secondSection = chosen_keyword[sliceyPlace:] #part of the word after the %
        password = firstSection + '%' + secondSection #smooshing them all together- first section, % and second section

        '''If not seven characters, insert dollar sign until it is.'''
        while len(password) < 7: #adding $ until the length of the password is 7
            password = password + '$'
        if password not in passwordList: #if there is a duplicate, you'll need to add an extra password at the end because it shouldn't be added
            return(password)
            passwordGenerated = True
        else:
            continue

'''WELCOME MESSAGE- explaining the password generator, title, instructions etc.'''

print("TARA'S PASSWORD GENERATOR")

printSleep("Welcome to this password generator!")

printSleep("\nIn this generator, you will be asked to enter a specific set of keywords.")

printSleep("These keywords will be used to generate a set of ten different passwords according to a set of criteria.")

printSleep("Please note that keywords with numbers are not accepted, therefore if your answer contains a number you may wish to reconsider.")

printSleep("If you ever don't want to answer a question or it's not applicable to you, type n/a to move on to the next question.")

repeat = True
while repeat == True: #allowing the user to repeat the program at the very end
    #KEYWORD INPUT
    keywords = [] #creating a list of the keywords inputted

    #using function defined earlier to get keyword input
    addKeyword("Let's begin! What is the name of your pet or child? ")
    addKeyword("What is the city of your birth? ")
    addKeyword("What is your favourite movie? ")
    addKeyword("What is your favourite animal? ")
    addKeyword("What is your first name? ")
    addKeyword("What is your favourite colour? ")
    addKeyword("What is your favourite season? ")

    #checking that there is at least one keyword to work with, so I don't get an error
    if len(keywords) >= 4:
        print("Keyword input complete.")
    else:
        print("You do not have enough keywords to continue. Four or more inputs are required.")
        while len(keywords) < 4:
            addKeyword("Please enter a word to be used in password generation. ")

    #GENERATING PASSWORDS FOR THE PASSWORD LIST
    
    for i in range(10):
        passwordList.append(generatePassword())

    print(passwordList)

    ##PRINTING PASSWORDS NICELY USING TKINTER

    root = tk.Tk()
    text = tk.Text(root, height=100, width=100) #configuring a window that should be big enough to hold all my text nicely
    text.tag_configure('big', #configuring a text style that is large
                        foreground='#A3C2E4',
                        font=('Verdana', 34, 'bold'))
    text.tag_configure('color', #configuring a normal sized text style
                        foreground='#A4A3E4',
                        font=('Tempus Sans ITC', 15, 'bold'))
    text.tag_configure('other', #configuring a text style to use at the bottom of the output window
                        foreground='#C2E4A3',
                        font=('Tempus Sans ITC', 15, 'bold'))
    text.insert(tk.END,'\nHere are your passwords!\n', 'big')
    j = 1 #used for password numbers in the output
    for i in passwordList:
        quote = str(j) + '. ' + i #what will be printed on each line
        if len(i) == 7: #makes sure that only passwords with a length of 7 characters are outputted
            text.insert(tk.END, quote, 'color') #printing the text with the right text style
            text.insert(tk.END, '\n', 'follow') #creating a new line
            j = j + 1
    text.pack()
    text.pack(side=tk.LEFT)
    text.clipboard_clear() #clears the clipboard before writing to it
    text.clipboard_append(passwordList) #copying the entire password list to the clipboard
    text.update()
    text.insert(tk.END, '\nA list of your password options has been copied to the clipboard.', 'other')
    text.insert(tk.END, '\nIf you would like a specific password copied to the clipboard instead, please return to the input window. Do not close this window!', 'other')


    #COPYING A DESIRED PASSWORD TO THE CLIPBOARD
    on = True
    while on == True:
        print("\nIf you don't want to copy a specific password, type 'END' without the quotes.")
        clipboardPassword = input("Which number password would you like copied to the clipboard? ")
        try:
            if clipboardPassword == "END": #END is the exit command, so when the user types END the loop is broken
                on = False
                break
            clipboardPassword = int(clipboardPassword) #if the command is not END, then it converts it to an integer. If it isn't an integer then the except command with the TypeError is used
            if clipboardPassword <= 10 and clipboardPassword >= 1: #making sure the number is within the right range
                text.clipboard_clear()
                text.clipboard_append(passwordList[clipboardPassword-1]) #copying the chosen password to the clipboard
                text.update()
                print("Password number", str(clipboardPassword), "has been copied to the clipboard.")
                print("Please keep this window open until you have pasted your desired password into its final locations.")
                on = False #exiting the while loop
        except TypeError: #if a non-number is inputted
            print("Invalid input. You must input the number of the password from the output window. Try again, or type 'END' to end the program.") 
        except tk.TclError: #if the user closed the tkinter window
            print("You closed the window! Oops!")
            break
    #EXIT MESSAGE
    printSleep("Thank you for using this password generator. I hope you enjoy your life with this secure password of yours.")
    repeat_input = input("Would you like to run this password generator again? If so, type y. If you would like to end the program, type n.")
    if repeat_input == "y":
        continue
    else:
        printSleep("Enjoy the rest of your day!") #making the user happy :)
        repeat = False
root.mainloop() #necessary to keep the password on the clipboard while the program runs
