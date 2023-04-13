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
        chosen_chest = random.randint(1, 6)
        ConsoleLog.print_chest_found(self.chest_list[chosen_chest])
        self.player_1.add_balance(money=self.chest_list[chosen_chest]['money'])

    def start_game(self):
        player_name = ConsoleLog.get_player_name()
        self.player_1 = Player(name=player_name)
        ConsoleLog.print_go()
        player_turn = 1

        while True:
            ConsoleLog.print_line()
            if player_turn % 2:
                # Are you in Prison?!
                if self.player_1.prison_time > 0:
                    ConsoleLog.print_in_prison()

                    rolled_dice = self.roll_dice()
                    ConsoleLog.print_rolling_dice(rolled_dice)

                    if Utils.check_double_dice(dice=rolled_dice):
                        self.player_1.prison_time = 0
                        self.player_1.move_player(steps=rolled_dice[0] + rolled_dice[1])
                    else:
                        if self.player_1.prison_time >= 3:
                            self.player_1.get_out_of_jail()
                        else:
                            self.player_1.prison_time += 1
                # Guess not in prison
                else:
                    self.player_1.prison_time = 0
                    rolled_dice = self.roll_dice()
                    ConsoleLog.print_rolling_dice(rolled_dice)

                    self.player_1.move_player(rolled_dice[0] + rolled_dice[1])

                    current_position = self.player_1.position
                    # todo: do the logic
                    if self.board[self.player_1.position].property_type == PropertyTypeEnum.CHEST:
                        self.choose_a_random_chest()
                    elif self.board[self.player_1.position].property_type == PropertyTypeEnum.INCOME_TAX:
                        self.player_1.apply_tax(tax_type=PropertyTypeEnum.INCOME_TAX)
                    elif self.board[self.player_1.position].property_type == PropertyTypeEnum.SUPER_TAX:
                        self.player_1.apply_tax(tax_type=PropertyTypeEnum.SUPER_TAX)
                    elif self.board[self.player_1.position].property_type == PropertyTypeEnum.JAIL:
                        self.player_1.handle_jail()
                    elif self.board[self.player_1.position].property_type == PropertyTypeEnum.LANDMARK:
                        self.player_1.land_on_property(self.board[self.player_1.position])
                    elif self.board[self.player_1.position].property_type == PropertyTypeEnum.PARKING:
                        pass

                    if Utils.check_double_dice(rolled_dice):
                        self.player_1.set_doubled_dice_times(self.player_1.doubled_dice_times + 1)
                        self.player_1.check_doubled_dice_times()
                        continue
                    self.player_1.work_with_properties()
                    self.player_1.check_positive_balance()
            else:
                ConsoleLog.print_bot_turn()
                rolled_dice = self.roll_dice()
                ConsoleLog.print_rolling_dice(rolled_dice)
                # todo: bot
                pass
            player_turn = (player_turn + 1) % 2
