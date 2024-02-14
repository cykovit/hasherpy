## hash it, here we go again...

import hashlib
from rich.console import Console
from rich.table import Table

console = Console()

title = '''
     _                  _                               
    | |                | |                              
    | |__    __ _  ___ | |__    ___  _ __  _ __   _   _ 
    | '_ \  / _` |/ __|| '_ \  / _ \| '__|| '_ \ | | | |
    | | | || (_| |\__ \| | | ||  __/| |   | |_) || |_| |
    |_| |_| \__,_||___/|_| |_| \___||_|   | .__/  \__, |
                                          | |      __/ |
                                          |_|     |___/ 
    
'''
print(title)

def get_hash_algorithms():
    return {
        1: hashlib.md5,
        2: hashlib.sha256,
        3: hashlib.sha384,
        4: hashlib.sha512,
    }

def get_user_input(message):
    return input(message)

def display_available_algorithms(algorithms):
    table = Table(title="Choose your hashing algorithm", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan")
    table.add_column("Algorithm", style="cyan")

    for key, algorithm in algorithms.items():
        table.add_row(str(key), algorithm.__name__)

    console.print(table)

def hash_password(password, algorithm):
    hash_object = algorithm(password.encode('utf-8'))
    return hash_object.hexdigest()

if __name__ == "__main__":
    algorithms = get_hash_algorithms()

    password = get_user_input("enter the string to hash : ")

    display_available_algorithms(algorithms)

    algorithm_choice = int(get_user_input("enter 1,2,3 or 4 to continue : "))

    while algorithm_choice not in algorithms:
        console.print("ERROR: invalid choice")
        display_available_algorithms(algorithms)
        algorithm_choice = int(get_user_input("enter 1,2,3 or 4 to continue : "))

    selected_algorithm = algorithms[algorithm_choice]

    result = hash_password(password, selected_algorithm)

    console.print("\n[bold]Results:[/bold]")
    console.print(f"[cyan]String:[/cyan] {password}")
    console.print(f"[cyan]Hash:[/cyan] {result}")

input('press ENTER to exit')