import translate
import time
import re


def port_to_eng(to, fr):
    traduzir = translate.Translator(to, fr)

    while True:
        try:
            word = input("\nPlease type a word to translate to portugues: ")
            word = int(word)

            print("\n *** It's an integer, please type a text. *** \n")
            continue
        except ValueError:
            try:
                word = float(word)
                print("\n *** It's a float, please type a text. ***\n")
                continue
            except ValueError:
                print(f"\nLet's translate {word} for you...\n")
                time.sleep(2)
                # with open("translate.txt", mode="a+") as my_file:
                #     my_file.write(f"{word} is {traduzir.translate(word)} \n")

                print(f"{word} is {traduzir.translate(word)} \n")


                answer = input("Do you need to translate another word? \"Yes/No\" ")

                pattern_yes = re.compile(r"[yY][eE]?[Ss]?")
                pattern_no = re.compile(r"[nN][oO]?")

                if pattern_yes.match(answer):

                    continue 

                elif pattern_no.match(answer):
                    print("\nThank you!!! \n")
                    break

                else:
                    print("\nYou typed something different from yes and no. Closing the program...\n")
                    time.sleep(2)
                    break

port_to_eng("pt", "en")

