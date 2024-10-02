import emoji #EMOJI
import random #RANDOM
import time #WAIT
from colorama import Fore, Back, Style #COLOR

#decisionKey:
#drop
#south
#yes (noImmediateEffect)
#straight
#yes
#no
#ignore
#yes

#FISHY ERROR
bird = "placeheld"
gameNumber = 0
infoWait = 2
inputWait = 1.75

def loopGame():
 global gameNumber
 while 1 == 1:
   
   if int(gameNumber) < 1:
     x = 1
   else:
     time.sleep(inputWait)
     clue = input("\nWould you like to play a little guessing game to get a hint for your next attempt?" + Fore.BLUE + ' (yes or no)' + Style.RESET_ALL + '\n')
     if clue == "yes":
       randomGame()
     elif clue == "no":
       print("\nOkay then!")
     else:
       print("\nWhat is " + clue + "?")
    
   gameNumber = gameNumber + 1
  
   game = input("\nShould Pin the cat go to the fish market?" + Fore.BLUE + ' (yes or no)' + Style.RESET_ALL + '\n')
 
   if game == "yes":
     print(emoji.emojize("\nAttempt #" + str(gameNumber) + " :fish:"))
     exposition()
     zeroStreet()
     halfStreet()
     oneStreet()
     twoStreet()
     threeStreet()
     fourStreet()
     fiveStreet()
     sixStreet()
  
   elif game == "no":
     print("\nNo, not today")
     exit()
   elif game == "hawthorne":
     global bird
     bird = "true"
     sixStreet()
   else:
     print("\nPin can't " + game + "!")
    
def randomGame():
 value = random.randint(1,10)
 #print(value)
 
 print("\nYou have 3 guesses... Go!")
 guessNumber = 1
 
 while int(guessNumber) < 4:
   guess = input("\nGuess #" + str(guessNumber) + ": the random number between 1 and 10 \n")
 
   if int(guessNumber) < 5:
     if int(guess) == value:
       print("\nYay!")
       print("You want to go south on St. Milo Way the entire time to reach the fish market")
       loopGame()
     elif int(guess) < value:
       guessNumber = guessNumber + 1
       print("\nToo low!")
       if int(guessNumber) == 5:
        print("Better luck next time!")
        loopGame()
       else:
        x = 1
     else:
       guessNumber = guessNumber + 1
       print("\nToo high!")
       if int(guessNumber) == 5:
        print("Better luck next time!")
        loopGame()
       else:
        x = 1
   else:
     print("\nToo many guesses...")
     loopGame()
 
#Exposition
def exposition():
 print("\nPin lived on the second story of the apartment complex on St. Milo Way with his pet human. Today the human was not home and Pin had places to be. The fish market on 6th Street opened at dawn and the first rays of sunlight were visible out the balcony as they brightened the eastern horizon. He sniffed deeply at the crisp morning air. There was something salty and fishy that Pin detected. He could smell the sea to his right.")
 
#0 Street
def zeroStreet():
 time.sleep(infoWait)
 print("\nPin knew the fire escape exited into a gated area that had no exits without the proper key. This was far from up to code but Pin couldn’t fix everything. But, the 1st level of apartments was slightly below street level which meant the drop from the Pin’s balcony was only 7 ft and he had a tree that he could climb back up on the return journey.")
 time.sleep(inputWait)
 zero = input("\nHow should Pin leave the apartment?" + Fore.BLUE + ' (fire escape or drop)' + Style.RESET_ALL + '\n')
 
 if zero == "fire escape":
   print("\nWrong way")
   loopGame()
 elif zero == "drop":
   print("\nThe drop is clearly the most logical choice so Pin leaps. He safely lands on his feet!")
 else:
   print("\nPin can't " + zero + "!")
   loopGame()
 
#0.5 Street
def halfStreet():
 time.sleep(infoWait)
 print("\nPin reaches the street! He looks up and down the street considering which was to go. He must decide which direction to travel in if he wants to reach the fish market.")
 time.sleep(inputWait)
 half = input("\nWhich direction should Pin go?" + Fore.BLUE + ' (north or south)' + Style.RESET_ALL + '\n')
 
 if half == "north":
   print("\nWrong way")
   loopGame()
 elif half == "south":
   print("\nThe fish wind was coming from the right as Pin faced the eastern sunrise, south he goes!")
 else:
   print("\nPin can't go " + half + "!")
   loopGame()
 
#1 Street
def oneStreet():
 time.sleep(infoWait)
 print("\nWhen he reaches 1st Street, he spies a bird. It’s a sparrow and the wind is directed north. And its back is turned too, such luck!")
 time.sleep(inputWait)
 one = input("\nShould Pin try to catch the bird?" + Fore.BLUE + ' (yes or no)' + Style.RESET_ALL + '\n')
 
 if one == "no":
   global bird
   bird = "false"
   print("\nKeep going! Pin needs to get there quickly if he wants to get good fish!")
 elif one == "yes":
   bird = "true"
   print("\nThe bird will make excellent payment for the a fish at the market and he knows the good ones are quickly snapped up by other customers and time is ticking.")
 else:
   print("\nPin can't " + one + "!")
   loopGame()
 
#2 Street
def twoStreet():
 time.sleep(infoWait)
 print("\nOn 2nd Street a street sign has been knocked off its pole and has swung 90 degrees clockwise. It indicates that the fish market is to his right, St. Milo Way is to his left, and 2nd Street is straight.")
 time.sleep(inputWait)
 two = input("\nWhich direction should Pin turn?" + Fore.BLUE + ' (right, left, back, or straight)' + Style.RESET_ALL + '\n')
 
 if two == "left":
   print("\nWrong way")
   loopGame()
 elif two == "right":
   print("\nWrong way")
   loopGame()
 elif two == "back":
   print("\nWrong way")
   loopGame()
 elif two == "straight":
   print("\nPin continues on St. Milo Way towards the fish market!")
 else:
   print("Pin can't go " + two + "!")
   loopGame()
 
#3 Street
def threeStreet():
 time.sleep(infoWait)
 print("\nOn 3rd Street the light up sign across the street shows a red hand and there are cars zooming fast. But time is of the essence and Pin really has to get to the fish market!")
 time.sleep(inputWait)
 three = input("\nShould Pin wait for the light to change before stepping onto the crosswalk?" + Fore.BLUE + ' (yes or no)' + Style.RESET_ALL + '\n')
 
 if three == "no":
   print("\nWow how fast the scary cars go. How frightening! Pin decides to turn around and go home.")
   loopGame()
 elif three == "yes":
   print("\nHe waits for the stoplight before crossing the street.")
 else:
   print("\nPin can't " + three + "!")
   loopGame()
 
 
#4 Street
def fourStreet():
 time.sleep(infoWait)
 print("\nOn 4th Street Pin encounters some of his friends. They greet him cheerfully:")
 
 #if then regarder le bird
 if bird == "true":
   print("Why hello Pin! How are you this fine morning? Oh I see you cannot reply, what a wonderful catch you have there, such a perfect sparrow! À bientôt!")
 elif bird == "false":
   print("Why hello Pin! How are you this fine morning? We are just on our way to the fish market! Would you like to join us on our westward quest for the finest fish?")
 else:
   print("\nFISHY ERROR")
 
 time.sleep(inputWait)
 four = input("\nShould Pin follow his friends?" + Fore.BLUE + ' (yes or no)' + Style.RESET_ALL + '\n')
 
 if four == "yes":
   print("\nWrong way, Pin wants to go south not west")
   loopGame()
 elif four == "no":
   print("\nYup, friends have no clue where the fish market is, Pin is southbound")
 else:
   print("\nPin can't " + four + "!")
   loopGame()
 
#5 Street
def fiveStreet():
 time.sleep(infoWait)
 print("\nOn 5th Street a truck that is heading back the way Pin came is driving by. Its side bears large images that advertises fresh and high quality fish.")
 time.sleep(inputWait)
 five = input("\nWhat should Pin do about the truck?" + Fore.BLUE + ' (follow or ignore)' + Style.RESET_ALL + '\n')
 
 if five == "follow":
   print("\nA fruitless chase that Pin gives up on when he realizes the truck has driven up St. Milo Way and he is back where he started in front of his apartment.")
   loopGame()
 elif five == "ignore":
   print("\nThe truck must have just come from the fish market. Onwards!\n")
 else:
   print("\nPin can't " + five + "!")
   loopGame()
 
#6 Street
def sixStreet():
 time.sleep(infoWait)
 print("\nSuccess! Pin arrives just as the morning’s catch is being laid out. Delectable aromas sweep towards him. There is one in particular that catches Pin’s attention.")
 #if then regarder le fish
 
 if bird == "false":
   print("The vendor looks up just in time to see Pin lunge for the finest tuna of the day’s catch! Cat, not my fish! Shoo! Pin heads home with no sparrow and without his tuna.")
 elif bird == "true":
 
   time.sleep(inputWait)
   six = input("\nShould Pin use the sparrow to pay for the fish?" + Fore.BLUE + ' (yes or no)' + Style.RESET_ALL + '\n')
 
   if six == "no":
     print("\nNo! My sparrow! The vendor looks up just in time to see Pin lunge for the finest tuna of the day’s catch! Cat, not my fish! Shoo! Pin heads home with his sparrow but without his tuna.")
   elif six == "yes":
     print(emoji.emojize("\nYes! Pin should pay. Since the human guarding this specific tuna does not see a dead bird as a suitable payment for the marvelous fish, Pin darts up and snatches it off the table! Pin enjoys his yummy tuna. :fish::fish::fish:"))
     exit()
   else:
     print("\nPin can't " + six + "!")
     loopGame()
 
 else:
   print("\nFISHY ERROR")
 
loopGame()
 