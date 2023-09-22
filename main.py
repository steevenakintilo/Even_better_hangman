from random import randint

def openfile(path):
  try:
    with open(path, encoding="utf-8") as file:
      f = file.read()
      file.close()
      return(f)
  except Exception as e:
    print("file don't exist")
    quit()

def replace_letter(string,letter):
  guess_word = ""
  for i in range(len(string)):
    if string[i] in letter:guess_word+=string[i]
    else:guess_word+="-"
  return(guess_word)

random_word = openfile("FR_words").split("\n")[randint(0,len(openfile("FR_words").split("\n")) - 1)]
nb_of_guess = 5
wrong_letter = ""
guess_word = "-"*len(random_word)
letter_done = []

while True:
  try:
    
    print(guess_word+"\n")
    guess = input("Put a letter big bro: ").lower()
    if len(guess) > 1 and guess != random_word:
      quit(print(f"Wrong word game over word was {random_word} "))
    elif len(guess) == 1 and guess.isalpha() == False:
      print("You can only put letters")
    elif nb_of_guess == 0:
      quit(print(f"You lost the word was: {random_word} "))
    elif guess not in random_word:
      wrong_letter += " " + guess
      print(f"the letter is not in the word\nNumber of guess left {nb_of_guess}")
      nb_of_guess=nb_of_guess-1
    elif guess in random_word:
      print("Good letter")
      letter_done.append(guess)
      guess_word = replace_letter(random_word,letter_done)
    if guess == random_word or "-" not in guess_word:
      quit(print("You won"))
    print("\nletter already done: " , wrong_letter)
  
  except:
    quit()