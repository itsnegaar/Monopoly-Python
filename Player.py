from Enums import PropertyTypeEnum
from ConsoleLog import ConsoleLog
from Property import Property


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.balance = 1500
        self.owned_property_list = []
        self.prison_time = 0
        self.doubled_dice_times = 0

    def move_player(self, steps: int):
        self.position = (self.position + steps)
        if self.position >= 40:
            self.balance += 200
            self.position %= 40
            ConsoleLog.print_moved_on_go()

    def pay_rent(self, rent, owner):
        if self.balance >= rent:
            self.balance -= rent
            owner.balance += rent
            return True
        else:
            return False

    def apply_tax(self, tax_type):
        if tax_type == PropertyTypeEnum.INCOME_TAX:
            self.balance -= 200
            ConsoleLog.print_tax_applied(tax_type=tax_type, tax_money=200)
        elif tax_type == PropertyTypeEnum.SUPER_TAX:
            self.balance -= 100
            ConsoleLog.print_tax_applied(tax_type=tax_type, tax_money=100)

    def is_defeated(self):
        for owned_property in self.owned_property_list:
            pass

    def handle_jail(self):
        if self.prison_time == 0:
            ConsoleLog.print_landed_on_jail(self)
            while True:
                input_choice = input()
                if input_choice == '1' or input_choice == '2':
                    break
                else:
                    print("Wrong Input. Try Again:")
                    continue
            if input_choice == '1':
                self.get_out_of_jail_for_money()
        elif self.prison_time <= 2:
            print("Sorry! You're still in jail for more {} rounds.\n", 3 - self.prison_time)
            self.prison_time += 1
        else:
            self.get_out_of_jail()

    def get_out_of_jail_for_money(self):
        self.balance -= 50
        self.prison_time = 0
        print("Got out of jail for $50...\n")

    def get_out_of_jail(self):
        print("Congrats! You got out of prison after three failed attempts. Just visiting...")
        self.prison_time = 0

    def buy_property(self, owned_property: Property):
        if self.balance >= owned_property.price:
            property.owner = self
            self.balance -= owned_property.price
            return True
        else:
            print("Your balance is lower than the expected balance for this action!")
            return False

    def add_balance(self, money: int):
        self.balance += money

    def check_positive_balance(self):
        if self.balance >= 0:
            return
        else:
            print("Your balance is less that zero; Sell properties to avoid bankruptcy.")
            self.handle_negative_balance()

    def work_with_properties(self):
        print("You're Balance is {}.\n", self.balance)
        while True:
            input_choice = input("Enter 1 to check properties or 0 to pass: ")
            if input_choice == '0':
                break
            elif input_choice == '1':
                self.print_owned_properties()
            else:
                print("Wrong input. Try Again...")
        # while True:
        #     property_choice = input("Choose a property number to downgrade, sell, or mortgage: ")
        #     # todo: more
        #     print("Ch")

    def print_owned_properties(self):
        for owned_property in self.owned_property_list:
            print(owned_property)

    def handle_negative_balance(self):
        while self.balance < 0:
            print("Select a property to sell, downgrade or mortgage")
            i = 0
            for owned_property in self.owned_property_list:
                print('property{} = ' + owned_property, i)
                i += 1
            while i > len(self.owned_property_list) or i < 0:
                input_property = int(input(""))
                if input_property < 0 or input_property >= len(self.owned_property_list):
                    ConsoleLog.print_invalid_input()

    def set_doubled_dice_times(self, times: int) -> None:
        self.doubled_dice_times = times

    def check_doubled_dice_times(self):
        if self.doubled_dice_times >= 3:
            print("You have doubled the dice for {} rounds.\n Now you go to Jail!", self.doubled_dice_times)
            self.position = 11  # position of jail
            self.doubled_dice_times = 0
            self.prison_time = 1

    def land_on_property(self, landed_property: Property):
        print("You landed on {}.".format(landed_property.name))
        if landed_property.owner:
            print("Sorry, this property is owned by Agent. Paying rent...")
            self.pay_rent(landed_property.rent)
        else:
            print("This property doesn't belong to anybody. Choose action:\n"
                  "1. Buy the property...\n"
                  "2. Go to next action...")
            while True:
                input_choice = input()
                if input_choice == '1':
                    self.buy_property(landed_property)
                    # todo : buy
                elif input_choice == '2':
                    break
                else:
                    print("Wrong output. Try Again: \n"
                          "1. Buy the property..."
                          "2. Go to next action...")

