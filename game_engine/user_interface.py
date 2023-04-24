from game_engine.level_manager import LevelManager
from game_engine.exploit_executor import ExploitExecutor
from game_engine.exploit_validator import ExploitValidator
from utils.exploit_editor import ExploitEditor

from prompt_toolkit import PromptSession

import os
import time

class UserInterface:
    def __init__(self):
        self.session = PromptSession()
        self.level_manager = LevelManager()
        self.exploit_executor = ExploitExecutor()
        self.exploit_validator = ExploitValidator()
        self.exploit_editor = ExploitEditor()

    def print_slowly(self, text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def print_border(self):
        os.system('clear')
        border = "#" * 80
        print(border)
        print("#" + " " * 78 + "#")

    def display_level_instructions(self, level):
        # Display level-specific instructions and vulnerable code to the player
        self.print_border()
        self.print_slowly(f"Level {level['number']}:")
        self.print_slowly("Instructions:")
        self.print_slowly(level['instructions'])
        self.print_slowly("\nVulnerable Code:")

        with open(level['path'], 'r') as f:
            vulnerable_code = f.read()
            self.exploit_editor.show_code(vulnerable_code)
 
    def get_exploit_input(self):
        # Get the player's exploit code input using the session.prompt() function
        return self.exploit_editor.get_code()

    def handle_menu(self):
            self.print_slowly("\nMenu options:")
            self.print_slowly("1. Save progress")
            self.print_slowly("2. Exit game")
            choice = self.session.prompt("Select an option: ")
            if choice == '1':
                self.level_manager.save_progress()
                self.print_slowly("Progress saved.")
            elif choice == '2':
                self.print_slowly("Goodbye!")
                exit(0)
            else:
                self.print_slowly("Invalid choice.")

    def start_game(self):
        self.print_slowly("Welcome to the Buffer Overflow Game!", 0.03)

        while True:
            current_level = self.level_manager.get_current_level()
            self.display_level_instructions(current_level)

            user_input = self.session.prompt("> ")

            if user_input.startswith("exploit"):
                exploit_code = self.get_exploit_input()
                exploit_result = self.exploit_executor.execute_exploit(exploit_code)

                if self.exploit_validator.validate_exploit(exploit_result):
                    self.print_slowly("Success! You have completed this level.")
                    self.level_manager.advance_to_next_level()
                else:
                    self.print_slowly("Exploit failed. Try again.")
            elif user_input.startswith("menu"):
                self.handle_menu()
            elif user_input.startswith("exit"):
                self.print_slowly("Goodbye!")
                break
            else:
                self.print_slowly("Invalid command.")