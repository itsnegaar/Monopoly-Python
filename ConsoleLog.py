from typing import Dict
import time
from Enums import PropertyTypeEnum


class ConsoleLog:
    @staticmethod
    def print_line():
        time.sleep(1)
        print("\t \t ********************************** \t \t\n")
        time.sleep(1)

    @staticmethod
    def print_rolling_dice(rolled_dice):
        print("Rolled The Dice: Dices=({},{})".format(rolled_dice[0], rolled_dice[1]))


    @staticmethod
    def print_in_prison():
        print("Sorry! You're still in prison...")


    @staticmethod
    def print_chest_found(chest: Dict):
        print("You Landed on a Chest:\n",
              chest['message'])


    @staticmethod
    def print_negative_balance(player):
        player.print_owned_properties(player)

    @staticmethod
    def print_invalid_input():
        print("Invalid input. Please try again.")

    @staticmethod
    def print_property_not_found(property_name):
        print("Sorry! The property", property_name, "was not found.")



    @staticmethod
    def print_bot_turn():
        print("It's Bots turn...\n")

    @staticmethod
    def show_board(self):
        pass

    @staticmethod
    def print_start_menu():
        pass

    def print_options_menu_empty_property(self, property_cost):
        print("\nwhat would you like to do?"
              "\n(1)Buy for $", property_cost,
              "\n(2)Mortgage(CURRENTLY UNAVAILABLE)"
              "\n(3)Check properties"
              "\n(4)End turn")

    # @staticmethod
    # def print_menu_for_bought_properties(self):
