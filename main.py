import random
import string
import colorama
import time
from colorama import Fore, Style

colorama.init(autoreset=True)

def generate_promo_code():
    prefix = "https://discord.com/billing/partner-promotions/1180231712274387115/eyJhbGciOiJkaXIiLCJ"
    suffix = ".iBAdZbFxNmUCR-6eRNIXtQ"
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=150))
    return f"{prefix}{random_part}{suffix}"

def print_drex_tools():
    for _ in range(3):
        print(Fore.RED + "Drex Tools - zandev97")

def main():
    print_drex_tools()

    print(Fore.YELLOW + "How many promo codes for Discord Nitro do you want to generate?")
    num_codes = int(input())

    generated_codes = []
    for _ in range(num_codes):
        code = generate_promo_code()
        generated_codes.append(code)

    with open("codes.txt", "w") as file:
        for code in generated_codes:
            file.write(code + '\n')

    print(Fore.BLUE + f"Generated {num_codes} promo codes. Codes are saved in codes.txt")

    print(Fore.GREEN + "Close? [Y/N]")
    close_choice = input().strip().lower()
    if close_choice == "y":
        print_drex_tools()
        print(Fore.GREEN + "Closing the console.")
        time.sleep(1)

if __name__ == "__main__":
    main()
