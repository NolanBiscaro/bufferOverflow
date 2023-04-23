from game_engine.level_manager import LevelManager
from game_engine.exploit_executor import ExploitExecutor
from game_engine.exploit_validator import ExploitValidator

from prompt_toolkit import PromptSession

class UserInterface:
    def __init__(self):
        self.session = PromptSession()
        self.level_manager = LevelManager()
        self.exploit_executor = ExploitExecutor()
        self.exploit_validator = ExploitValidator()

    def display_level_instructions(self, level):
        # Display level-specific instructions and vulnerable code to the player
        pass

    def get_exploit_input(self):
        # Get the player's exploit code input using the session.prompt() function
        pass

    def handle_menu(self):
        # Handle user input for menu options (e.g., save progress, exit game)
        pass

    def start_game(self):
        print("Welcome to the Buffer Overflow Game!")

        while True:
            current_level = self.level_manager.get_current_level()
            self.display_level_instructions(current_level)

            user_input = self.session.prompt("> ")

            if user_input.startswith("exploit"):
                exploit_code = self.get_exploit_input()
                exploit_result = self.exploit_executor.execute_exploit(exploit_code)

                if self.exploit_validator.validate_exploit(exploit_result):
                    print("Success! You have completed this level.")
                    self.level_manager.advance_to_next_level()
                else:
                    print("Exploit failed. Try again.")
            elif user_input.startswith("menu"):
                self.handle_menu()
            elif user_input.startswith("exit"):
                print("Goodbye!")
                break
            else:
                print("Invalid command.")