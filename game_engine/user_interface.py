from game_engine.level_manager import LevelManager
from game_engine.exploit_executor import ExploitExecutor
from game_engine.exploit_validator import ExploitValidator
from utils.exploit_editor import ExploitEditor

from prompt_toolkit import PromptSession

import os
import time
import shutil
import tempfile

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
        self.print_slowly(f"Level {level['number']}:")
        self.print_slowly(level['instructions'])
        self.print_border()
        self.print_slowly("\nVulnerable Code:")
        with open(level['path'], 'r') as f:
            vulnerable_code = f.read()
            self.exploit_editor.show_code(vulnerable_code)
 
    def get_exploit_input(self):
        # Get the player's exploit code input using the session.prompt() function
        return self.exploit_editor.get_code()

    def handle_main_menu(self):
            self.print_slowly("\nMain Menu options:")
            self.print_slowly("1. Smash the Stack")
            self.print_slowly("2. Save progress")
            self.print_slowly("3. Exit game")
            choice = self.session.prompt("Select an option: ")
            if choice == '1':
                return True
            elif choice == '2':
                self.level_manager.save_progress()
                self.print_slowly("Progress saved.")
                return False
            elif choice == '3':
                self.print_slowly("Goodbye!")
                exit(0)
            else:
                self.print_slowly("Invalid choice.")
    
    def handle_exploit_menu(self):
        self.print_slowly("\nExploit Menu Options:")
        self.print_slowly("1. Write Exploit")
        self.print_slowly("2. Get Hint")
        self.print_slowly("3. Skip Level")
        self.print_slowly("4. Return to Main Menu")
        choice = self.session.prompt("Select an option: ")
        if choice == '1':
            return True
        elif choice == '2':
            current_level = self.level_manager.get_current_level()
            self.print_slowly(current_level['hints'])
            return True
        elif choice == '3':
            current_level = self.level_manager.get_current_level()
            self.print_slowly("Success! You have completed this level.")
            self.level_manager.advance_to_next_level()
            return True
        elif choice == '4':
            return False
        else:
            self.print_slowly("Invalid choice.")


    def start_game(self):
        self.print_slowly("Welcome to Stack Smash!", 0.03)
        while True:  # Main game loop
            if self.handle_main_menu():  # If main menu returns True, enter exploit menu
                show_level_instructions = True
                while True:  # Exploit menu loop
                    if not self.handle_exploit_menu():  # If exploit menu returns False, break the loop and go back to the main menu
                        break
                    else:
                        if show_level_instructions:
                            current_level = self.level_manager.get_current_level()
                            self.display_level_instructions(current_level)
                            show_level_instructions = False
                        with tempfile.TemporaryDirectory() as tempdir:
                            with open(current_level['path'], 'r') as f:
                                vulnerable_code = f.read()
                                self.exploit_executor.enter_shell(vulnerable_code, tempdir)
                                exploit_result = self.exploit_executor.execute_exploit(tempdir)

                        print("EXPLOIT OUTPUT: exploit_result")
                        success_condition = (exploit_result == current_level['success'])
                        if success_condition:
                            self.print_slowly("Success! You have completed this level.")
                            self.level_manager.advance_to_next_level()
                            # clean up the dir in sandbox for this level
                            shutil(tempdir)
                        else:
                            self.print_slowly("Exploit failed. Try again.")