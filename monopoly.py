import random
import time
from Player import *
import Utils
from Enums import PropertyTypeEnum
from Board import Board
from ConsoleLog import ConsoleLog
from Player import Player
from copy import deepcopy
from math import ceil

class Monopoly:
    def __init__(self):
        self.board = Board.return_board()
        self.player_1: Player = None
        self.player_2 = "AI"
        self.players = [self.player_1, self.player_2]
        self.curr_player = None
        self.chest_list = [
            {'money': 100, 'message': "Your friend owed you money, now he pays you back!"},
            {'money': -100, 'message': "Your sister wants a new ipad, she needs a $100!"},
            {'money': 50, 'message': "Your grandma gave you money. She tells you to buy candy for yourself!"},
            {'money': 200, 'message': "You received $200 for your birthday! Don't spend it on drugs!"},
            {'money': -200, 'message': "Oops! You lost $200. It maybe fell off your pocket."},
            {'money': 500,
             'message': "You won the national hot dog eating contest and won $500! Hope that'll cover your toilet repairs..."},
            {'money': -50, 'message': "Your phone died. pay $50 to repair it!"},
            {'money': -50, 'message': "Doctor's fee. Pay $50"},
            {'money': 100, 'message': "Holiday fund matures. Receive $100"},
            {'money': 100, 'message': "Life insurance matures. Collect $100"},
            {'money':  25, 'message': "Receive $25 consultancy fee"},
            {'money': 100, 'message': "You inherit $100."},
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
                self.curr_player = 0
            else:
                player_now = self.player_2
                self.curr_player = 1

            print("It's {} Turn.\n".format(player_now.name))
            time.sleep(0.5)
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
    
    def take_action(self, action: int):
        # Updating the game state based on the action taken by the current player
        new_players = deepcopy(self.players)
        new_board = deepcopy(self.board)
        curr_player = new_players[self.curr_player]
        curr_position = curr_player.position 
        curr_prop = new_board[curr_position]
        # Do the appropriate changes for the action
        if action == 0:
            pass
        elif action == 1:
            curr_player.pay(curr_prop.price)
            curr_player.properties.append(curr_position)
            curr_prop.owner = self.current_player    
        elif action == 2:
            curr_player.pay(curr_prop.rent)
            new_players[curr_prop.owner].receive(curr_prop.rent)
        elif action == 3:
            curr_prop.rent *= 1.5
            curr_prop.rent = ceil(curr_prop.rent)
            curr_prop.level += 1
        elif action == 4:
            curr_player.position = 10
            curr_player.in_jail = True
            curr_player.turns_in_jail += 1
        elif action == 5:
            curr_player.turns_in_jail += 1
        elif action == 6:
            curr_player.pay(50)
            curr_player.in_jail = False
            curr_player.turns_in_jail = 0
        elif action == 7:
            curr_player.in_jail = False
            curr_player.turns_in_jail = 0       
        return Monopoly(new_board, new_players, self.current_player, self.game_over)
    
    def get_possible_actions(self) -> list:
        # Get the possible actions available to the current player
        curr_player = self.players
        curr_position = curr_player.position
        curr_prop = self.board[curr_position]
        if curr_player.in_jail:
            if curr_player.rolled_doubles:
                return [7]
            if curr_player.turns_in_jail >= 3:
                return [6]
            return [5, 6]
        if curr_prop.ownable:
            if curr_prop.owner == self.current_player:
                if curr_prop.level < 5:
                    return [3, 0]
                return [0]
            elif curr_prop.owner == None:
                if curr_player.money > curr_prop.price:
                    return [1, 0]
                return [0]
            else:
                return [2]
        if curr_prop.space == "GoToJail":
                return [4]
        return [0]
