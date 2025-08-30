import random
#THIS IS A PACKAGE USED TO GENERATE RANDOM NUMBERS THAT WE USE IT GIVE THE SYSTEM THE ABILITY TO PLAY 
#make the system play by generating a random number 
#rock=0
#paper=1
#scissors=2

User_score = 0
#THIS IS THE SCORE THAT THE USER WILL HAVE AT THE START
System_score = 0
options = ['rock', 'paper', 'scissors']
#THIS IS THE SCORE THAT THE SYSTEM WILL HAVE AT THE START
while True:  #THIS STARTS AN INFINITE LOOP 
    User_input=input("Enter Rock, Paper, Scissors or Q to quit: ").lower()
    #WE ARE TAKING THE USER INPUT AND CONVERTING IT TO LOWERCASE
    if User_input == 'q': 
    #THIS MAKES IT SO THAT WHEN THE USER PRESSES Q IT QUITS THE PROGRAM 
       break
     #THIS BREAK THE LOOP RESULTING IN THE BREAKING OF THE LOOP AND EXITING THE PROGRAM
    if User_input not in options:
        print("Invalid input, please try again.")
        continue
        #THIS CHECKS IF THE USER INPUT IS VALID OR NOT
    #This generates a random number for the system's choice
    System_input=random.randint(0,2)
    #System input = to random from 0 - 2 
    #we are going use the from options list to give the system choice
    #0=rock 1=paper 2 = scissors
    System_choice=options[System_input]
    #System choice = to get the value from the list at the index of the random number
    print(f"System chose: {System_choice}")
    #THIS WILL SHOW WHAT THE SYSTEM CHOSE 
    if User_input == System_choice : # Check for tie
        print("It's a tie!")
    elif User_input == 'rock' and System_choice == 'scissors': # Check for rock vs scissors
        print("You win!")
        User_score += 1 #THIS ADDs THE USER SCORE 
    elif User_input == 'paper' and System_choice == 'rock': # Check for paper vs rock
        print("You win!")
        User_score += 1 #THIS ADDs THE USER SCORE
    elif User_input == 'scissors' and System_choice == 'paper': # Check for scissors vs paper
        print("You win!")
        User_score += 1 #THIS ADDs THE USER SCORE
    else:
        print("You lose!")#because we checked that all the user wins scenarios are true then 
     #we other will the win for the system so we didn't have to do the if statements 
        System_score += 1#THIS ADDs THE system score 
    print(f"User score: {User_score}, System score: {System_score}") #THIS SHOWS THE CURRENT SCORE b/w you and the system 
    print("THANK YOU FOR PLAYING") 
    quit=input("Do you want to quit or play ? (y/n): ").lower()
    #This ask the user if he wants to quit ? (y/n)
    if quit == 'y':
        break
    elif quit == 'n':
        continue
    else:
        print("Invalid input, please try again.")
        continue


#MADE BY @DEVIL_PIXEL.S RATE THIS HOW YOU LIKE TO