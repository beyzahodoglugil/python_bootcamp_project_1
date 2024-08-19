import random
def tas_kagit_makas_NACİYE_BEYZA_HODOĞLUGİL():
    print("Welcome to Rock-Paper-Scissors Game\n")
    print("Game Rules:Rock beats scissors, scissors beats paper, and paper beats rock.\n")
    print("If you want to exit game you should press 'q'\n")
    game_actions=["rock","paper","scissors"]
    game_number=0
    round_number=0
    
    while True:
        player_score=0
        computer_score=0  
        while player_score<2 and computer_score<2:
            player_choice=input("Please make your choice btw :Rock paper or scissors").lower()
            
            if player_choice=='q':
                print("Quitting the game.\n")
                return
            
            if player_choice not in game_actions:
                print("Your choice is invalid! Please try again\n")
                continue

            computer_choice=random.choice(game_actions)
            print(f"Computer's choice: {computer_choice}")

            if player_choice==computer_choice:
                print("Tie")
            elif (player_choice=="rock" and computer_choice=="scissors") or (player_choice=="paper" and computer_choice=="rock") or (player_choice=="scissors" and computer_choice=="paper"):
                print("You won this round!")
                player_score+=1
            else :
                print("Computer won this round!")
                computer_score+=1

                print(f"--Scores--\nPlayer:{player_score}\nComputer:{computer_score}")
            
        if player_score==2:
            print("Congraculations! You won this game.")
        else:
            print("Computer won this game.")

        new_game=input("Do you want to play new game?(y/n):").lower()
        if new_game!='y':
            print("Game is completed!")
            break

        computer_new_game=random.choice(['y','n'])
        if computer_new_game=='n':
            print("Game is completed!") 
            break          