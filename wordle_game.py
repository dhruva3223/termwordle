from colorama import init, Style, Back, Fore
import pandas as pd
from datetime import datetime

NEW_WORD = 0
wordle_word = pd.read_csv('wordle_words.csv')
valid_words = pd.read_csv("valid_words.csv")
loop = True

while loop:
    print(Back.LIGHTRED_EX + Fore.BLACK +
          "               Start (y)               " + Style.RESET_ALL)
    print(Back.LIGHTRED_EX + Fore.BLACK +
          "              Settings (s)             " + Style.RESET_ALL)
    print(Back.LIGHTRED_EX + Fore.BLACK +
          "                Quit (q)               " + Style.RESET_ALL)
    command = input()
    if command == "q":
        loop = False
    elif command == "s":
        print(Back.LIGHTYELLOW_EX + Fore.BLACK +
              "  change wordle to today's wordle (t)  " + Style.RESET_ALL)
        print(Back.LIGHTCYAN_EX + Fore.BLACK +
              "       change puzzle number (s)        " + Style.RESET_ALL)
        print(Back.LIGHTWHITE_EX + Fore.BLACK +
              "              continue (c)             " + Style.RESET_ALL)
        settings = input()
        if settings == "t":
            dt_string = datetime.now().strftime("%m %d %Y")
            df = pd.DataFrame(wordle_word)
            reset_puzzle_number = int(
                df.loc[df['date'] == dt_string]['puzzle-number']+2)
            with open('progress.txt', 'w+') as data:
                data.write(str(reset_puzzle_number))
        elif settings == "s":
            puzzle_number = input("Enter puzzle_number number: ")
            with open('progress.txt', 'w+') as data:
                data.write(str(puzzle_number))
        elif settings == "c":
            continue
    elif command == "y":
        count = 0
        try:
            with open("progress.txt", "r+") as data:
                NEW_WORD = int(data.read())
        except:
            with open("progress.txt", "w+") as data:
                data.write("0")
        print(Back.LIGHTCYAN_EX+Fore.BLACK +
              f"puzzle-number: #{NEW_WORD}"+Style.RESET_ALL)
        word = wordle_word.iloc[NEW_WORD]['word']
        word = word.lower()
        print("Enter a word")

        while count < 6:
            word_exists = False
            while not word_exists:
                attempt = input()
                df = pd.DataFrame(valid_words)
                word_exists = (df['words'] == attempt).any()
                if not word_exists:
                    print("Please enter a valid 5 letter word")

            user_input = ""
            for i in range(len(word)):
                if attempt[i] == word[i]:
                    user_input = user_input + Back.RED + \
                        attempt[i] + Back.RESET
                elif attempt[i] in word:
                    user_input = user_input + Back.BLUE + \
                        attempt[i] + Back.RESET
                else:
                    user_input = user_input + attempt[i] + Back.RESET
            print(user_input)
            if word == attempt:
                print(Back.GREEN+"You Win!"+Back.RESET+"\n")
                count = count + 7

            count = count + 1
        if count == 6:
            print("You Lose: The Wordle was "+Back.WHITE +
                  Fore.BLACK+f"{word}"+Back.RESET+Fore.RESET)
            print("\n")

        with open('progress.txt', 'w+') as data:
            NEW_WORD += 1
            data.write(str(NEW_WORD))