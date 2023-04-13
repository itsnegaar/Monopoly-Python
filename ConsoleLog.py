from typing import Dict

from Enums import PropertyTypeEnum


class ConsoleLog:
    @staticmethod
    def print_line():
        print("\t \t ********************************** \t \t\n")

    @staticmethod
    def get_player_name():
        player_name = input("Please Enter Your Name: ")
        return player_name

    @staticmethod
    def print_rolling_dice(rolled_dice):
        print("Rolled The Dice: Dices=({},{})".format(rolled_dice[0], rolled_dice[1]))

    @staticmethod
    def print_moved_on_go():
        print("Congrats! Got $200 for moving on the GO property.")

    @staticmethod
    def print_in_prison():
        print("Sorry! You're still in prison...")


    @staticmethod
    def print_go():
        input("Click <ENTER> to begin your go... ")

    @staticmethod
    def print_chest_found(chest: Dict):
        print("You Landed on a Chest:\n",
              chest['message'])

    @staticmethod
    def print_tax_applied(tax_type: PropertyTypeEnum, tax_money):
        print("Landed on {}. ${} was paid for tax.", tax_type, tax_money)

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
    def print_landed_on_jail(player):
        print("Sorry! You're landed on jail...\n"
              "Enter your choice:\n"
              "1.Get out of jail for $50.\n"
              "2.Stay in jail for 3 rounds.\n")

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
