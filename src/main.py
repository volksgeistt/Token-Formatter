import colorama
from colorama import Fore
import time
import os

def get_all_tokens(filename: str):
    all_tokens = []
    try:
        with open(filename, "r") as file:
            for gc in file.read().splitlines():
                if ":" in gc:
                    token = gc.split(":")[2]
                    all_tokens.append(token)
                else:
                    all_tokens.append(gc)
    except FileNotFoundError:
        print(f"{Fore.RED}[ ERROR ] : File {filename} Not Found.")
    except Exception as e:
        print(f"{Fore.RED}[ ERROR ] : An Error Occured :- {e}")
    return all_tokens
def format_and_save_tokens(filename: str, tokens: list):
    try:
        with open(filename, "w") as file:
            for token in tokens:
                file.write(f"{token}\n")
    except Exception as e:
        print(f"{Fore.RED}[ ERROR ] : Failed While Saving Tokens :-  {e}")

def main():
    print(f"""

███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗████████╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░░░░██║░░░█████╗░░██████╔╝
██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗
██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░░░░██║░░░███████╗██║░░██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

                        - Volksgeist
    """)
    time.sleep(1)
    filename = input(f"{Fore.MAGENTA}Enter Filename Containing Tokens ( Ex: tokens.txt ) : ").strip()
    if not os.path.isfile(filename):
        print(f"{Fore.RED}[ ERROR ] : File {filename} Not Found")
        return
    print(f"{Fore.GREEN}[ PROGRESS ] Formatting Tokens, Please Wait.")
    time.sleep(1)
    all_tokens = get_all_tokens(filename)
    if all_tokens:
        format_and_save_tokens(filename, all_tokens)
        print(f"{Fore.GREEN}[ SUCCESS ] All Tokens Formatted And Saved Into {filename}")
    else:
        print(f"{Fore.RED}[ ERROR ] : There Are No Tokens In {filename}")

if __name__ == "__main__":
    main()
