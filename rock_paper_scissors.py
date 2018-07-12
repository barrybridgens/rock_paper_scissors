# Rock Paper Scissors game

from random import randint

# Outcome of each round willbe determained by a lookup table
# Inputs "R", "P", "S"
# Outputs "W", "L", "D" (player win, lose, draw)
rock = {"R" : "D", "P" : "L", "S" : "W"}
paper = {"R" : "W", "P" : "D", "S" : "L"}
scissors = {"R" : "L", "P" : "W", "S" : "D"}

table = {"R" : rock, "P" : paper, "S" : scissors}

def random_play():
    num = randint(1, 9)
    if (num <= 3):
        play = "R"
    elif (num <=6):
        play = "P"
    else:
        play = "S"
    return(play)

def Outcome(player_play, computer_play):
    return(table[player_play][computer_play])

def game():
    player_score = 0
    computer_score = 0
    rounds = input("How many rounds do you want to play? ")
    rounds = int(rounds)
    for round in range(rounds):
        print("Round : ", (round + 1))
        play_ok = False
        while (play_ok == False):
            play = input("What do you play (R, P or S)? ")
            if ((play == "R") or (play == "P") or (play == "S")):
                play_ok = True
            else:
                print("Invalid play: try again")
        computer_play = random_play()
        print("Computer plays: ", computer_play)
        outcome = Outcome(play, computer_play)
        if (outcome == "W"):
            print("You Win!")
            player_score = player_score + 1
        elif (outcome == "L"):
            print ("You Lose")
            computer_score = computer_score + 1
        else:
            print("Draw")

    print()
    print("Final Scores")
    print("  You      : ", player_score)
    print("  Computer : ", computer_score)
    
game()
