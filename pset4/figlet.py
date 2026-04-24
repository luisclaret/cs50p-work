from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    exe_prompt = sys.argv
    available_fonts = figlet.getFonts()
    if len(exe_prompt) == 1 or (
        len(exe_prompt) == 3
        and (exe_prompt[1] == "-f" or exe_prompt[1] == "--font")
        and (exe_prompt[2] in available_fonts)
    ):
        user_input = input("Input: ").strip()
        user_font = check_argv(exe_prompt=exe_prompt, available_fonts=available_fonts)
        convert_figlet(figlet, user_input=user_input, user_font=user_font)
    else:
        sys.exit("Error Message")


def convert_figlet(figlet, user_input: str, user_font: str):
    figlet.setFont(font=user_font)
    print(figlet.renderText(user_input))


def check_argv(exe_prompt: list, available_fonts: list):
    match len(exe_prompt):
        case 1:
            choose_font = random.choice(available_fonts)
            return choose_font
        case 3:
            return exe_prompt[2]
        case _:
            sys.exit("Error Message")


if __name__ == "__main__":
    main()
