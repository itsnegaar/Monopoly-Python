import random

import Utils
from Enums import PropertyTypeEnum
from Board import Board
from ConsoleLog import ConsoleLog
from Player import Player


class Monopoly:
    def __init__(self):
        self.board = Board.return_board()
        self.player_1: Player = None
        self.player_2 = "AI"

        self.chest_list = [
            {'money': 100, 'message': "Your friend owed you money, now he pays you back!"},
            {'money': -100, 'message': "Your sister wants a new ipad, she needs a $100!"},
            {'money': 50, 'message': "Your grandma gave you money. She tells you to buy candy for yourself!"},
            {'money': 200, 'message': "You received $200 for your birthday! Don't spend it on drugs!"},
            {'money': -200, 'message': "Oops! You lost $200. It maybe fell off your pocket."},
            {'money': 500,
             'message': "You won the national hot dog eating contest and won $500! Hope that'll cover your toilet repairs..."},
        ]

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def choose_a_random_chest(self):
        chosen_chest = random.randint(0, 5)
        ConsoleLog.print_chest_found(self.chest_list[chosen_chest])
        self.player_1.add_balance(money=self.chest_list[chosen_chest]['money'])

    def start_game(self):
        player_name = input("Player 1: Please Enter Your Name: ")
        self.player_1 = Player(name=player_name)
        player_name = input("Player 2: Please Enter Your Name: ")
        self.player_2 = Player(name=player_name)

        input("{}, Click <ENTER> to begin your go... ".format(self.player_1.name))
        player_turn = 1

        while True:
            ConsoleLog.print_line()
            if player_turn % 2:
                player_now = self.player_1
            else:
                player_now = self.player_2

            print("It's {} Turn.\n".format(player_now.name))
            # Are you in Prison?!
            if self.player_1.prison_time > 0:
                ConsoleLog.print_in_prison()

                rolled_dice = self.roll_dice()
                ConsoleLog.print_rolling_dice(rolled_dice)

                if Utils.check_double_dice(dice=rolled_dice):
                    player_now.prison_time = 0
                    player_now.move_player(steps=rolled_dice[0] + rolled_dice[1])
                else:
                    if player_now.prison_time >= 3:
                        player_now.get_out_of_jail()
                    else:
                        player_now.prison_time += 1
            # Guess not in prison
            # todo: make doubles zero when gone to jail
            else:
                if not player_now.is_visiting:
                    player_now.prison_time = 0
                    rolled_dice = self.roll_dice()
                    ConsoleLog.print_rolling_dice(rolled_dice)

                    player_now.move_player(rolled_dice[0] + rolled_dice[1])

                    current_position = player_now.position
                    # todo: do the logic
                    if self.board[player_now.position].property_type == PropertyTypeEnum.CHEST:
                        self.choose_a_random_chest()
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.INCOME_TAX:
                        player_now.apply_tax(tax_type=PropertyTypeEnum.INCOME_TAX)
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.SUPER_TAX:
                        player_now.apply_tax(tax_type=PropertyTypeEnum.SUPER_TAX)
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.JAIL:
                        player_now.handle_jail()
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.GO_TO_JAIL:
                        player_now.go_to_jail()
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.JUST_VISITING:
                        player_now.just_visiting()
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.LANDMARK:
                        player_now.land_on_property(self.board[player_now.position])
                    elif self.board[player_now.position].property_type == PropertyTypeEnum.AIRPORT:
                        player_now.land_on_airport(self.board[player_now.position])

                    if Utils.check_double_dice(rolled_dice):
                        player_now.set_doubled_dice_times(player_now.doubled_dice_times + 1)
                        player_now.check_doubled_dice_times()
                        print("You diced a double. Your turn again!")
                        player_now.work_with_properties()
                        player_now.check_positive_balance()
                        continue
                    else:
                        player_now.set_doubled_dice_times(0)
                else:
                    player_now.set_doubled_dice_times(0)
                    player_now.is_visiting = False
                player_now.work_with_properties()
                player_now.check_positive_balance()

            player_turn = (player_turn + 1) % 2
