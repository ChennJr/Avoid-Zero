#imports
import pygame 
import random
import time
import sys


wins = 0 # variables
see_score = ""
save_score = ""
rnumber = ""
remaining = ""
play_again = ""

def remove(string):
          return string.replace(" ", "")

#introduction
print("Hi, welcome to Avoid Zero")
time.sleep(1)
name = str(input("May I have your first name?\n"))
time.sleep(1)
print("\nHi", name)
time.sleep(2)
print("You will recieve a starting number between 20 and 30")
time.sleep(3)
print("The aim of Avoid Zero is to, well avoid landing on zero or a number below zero")
time.sleep(3)
print("You have to remove an amount between 1-3 from the given number each turn")
time.sleep(2)
print("You will go against a computer and take turns removing an amount from the number")
time.sleep(2)

#scoreboard
text_file = open("score.txt", "r")

while see_score != "Y" and see_score != "N": 
    see_score = remove(input("Would you like to see the scoreboard? Y or N\n")).upper()

if see_score == "Y":
    score_read = text_file.read()
    print (score_read)
    text_file.close()
elif see_score == "N":
    text_file.close()
    

#continue loop start + user ready check
while True:
  print("\nYou have", wins, "wins\n")
  
  rnumber = random.randint(20,30) 
  remaining = rnumber
  user_ready = ""
  while user_ready != "Y" and user_ready != "N": 
    user_ready = input("Are you ready? Y or N\n")
    user_ready = user_ready.upper()
    user_ready = remove(user_ready)

  while user_ready == "Y":
    print("\nOk good luck!")
    time.sleep(1)
    print("\n\n\nStarting number:",rnumber)
    break

  while user_ready == "N":
    time.sleep(3)
    user_ready = str(input("Ok, are you ready now?\n"))
    user_ready = user_ready.upper()
    time.sleep(3)
    user_ready = str(input("Ok, are you ready now?\n"))
    user_ready = user_ready.upper()
    time.sleep(3)
    print("Ok you have had enough time, the game is starting big boi")
    user_ready = "Y"
    time.sleep(2)
    print("\nOk good luck!")
    time.sleep(1)

    print("\n\n\nStarting number:",rnumber)
    break
  
  

  while rnumber != 0:
#user input
      print("\nYour turn:")
      user_remove = str(input("How many do you want to remove? 1-3\n"))
      user_remove = remove(user_remove)
        
            
#user conditions
      while user_remove == 1 or user_remove == 2 or user_remove == 3:
          user_remove = int(user_remove)
            
      while user_remove != "1" and user_remove != "2" and user_remove != "3" or len(user_remove) == 0:
          user_remove = str(input("That was not a number between 1-3. Please enter a correct value to subtract.\n"))
          user_remove = remove(user_remove)

      while user_remove == "1" or user_remove == "2" or user_remove == "3":
          user_remove = remove(user_remove)
          user_remove = int(user_remove)

#user removal
      remaining = rnumber
      remaining = remaining - user_remove
      remaining1 = remaining

      rnumber = remaining1
      print("\nYou removed",user_remove)
      time.sleep(0.5)
      print(rnumber, "left\n\n")

#user loss
      if rnumber == 0 or rnumber <= 0:
          time.sleep(1)
          print("Unlucky, you reached a number below or equal to zero")
          time.sleep(2)
          print("The computer won")
          print("You have", wins, "wins")
         
         
          #play again?
          while play_again != "Y" and play_again != "N":
            play_again = input("Would you like to play again? Y or N\n")
            play_again = play_again.upper()
            play_again = remove(play_again)
        
          if play_again == "Y":
            continue

          if play_again == "N":
            while save_score != "Y" and save_score != "Y":
                save_score = input("Would you like to save your score? Y or N\n")
                save_score = save_score.upper()
                save_score = remove(save_score)
            

            if save_score == "Y":
              text_file = open("score.txt", "a")
              wins = str(wins)
              text_file.write("\n" + name + ' has a score of ' + wins + ' wins')
              text_file.close()

#easter egg for connor
            if "connor" in name or "conn" in name or "oneill" in name or "oneill_jr" in name or "oneilljr" in name:
                time.sleep(2)
                print("xD uR TraSH Connor")
            

          print ("\nEXITING GAME")
          sys.exit()
          break
          quit()
          
        

      
#computer conditions       
      elif rnumber != 0:
          computer = random.randint(1,3)

          if rnumber == 2 or rnumber == 6 or rnumber == 10 or rnumber == 13 or rnumber == 14 or rnumber == 17:
              computer = 1

          if rnumber == 4 or rnumber == 8 or rnumber == 12 or rnumber == 16 or rnumber == 19:
              computer = 3

          if rnumber == 3 or rnumber == 7 or rnumber == 11 or rnumber == 15:
              computer = 2

          elif rnumber == 1:
              computer = 1

#computer removal          
          cremaining = computer
          cremaining = rnumber - cremaining
          rnumber = cremaining
          time.sleep(0.5)
          print("Computer turn:")
          time.sleep(2)
          print("Computer_1 removed",computer)
          time.sleep(0.5)
          print(cremaining, "left\n")
        
#computer loss      
          if rnumber == 0:
              time.sleep(1)
              print("Congrats! You won!")
              wins = wins +1
              wins = str(wins)
              print("You have", wins, "wins")
              
              while play_again != "Y" and play_again != "N":
                play_again = input("Would you like to play again? Y or N\n")
                play_again = play_again.upper()
                play_again = remove(play_again)
              
              if play_again == "Y":
                continue

              if play_again == "N":
                while save_score != "Y" and save_score != "Y":
                    save_score = input("Would you like to save your score? Y or N\n")
                    save_score = save_score.upper()
                    save_score = remove(save_score)
                
                if save_score == "Y":
                  text_file = open("score.txt", "a")
                  wins = str(wins)
                  text_file.write("\n" + name + ' has a score of ' + wins + ' wins')
                  text_file.close()

#easter egg for Connor
              if "connor" in name or "conn" in name or "oneill" in name or "oneill_jr" in name or "oneilljr" in name:
                time.sleep(2)
                print("xD uR TraSH Connor")
              
              print("EXITING GAME")
              sys.exit()
              break
              quit()



            
              
    

    


    

