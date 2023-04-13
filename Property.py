from Enums import PropertyTypeEnum, PropertyColorEnum
from Player import Player


class Property:
    def __init__(self, cell_number: int, name: str, property_type: PropertyTypeEnum, price: int = None,
                 rent: int = None, property_color: PropertyColorEnum = None):
        self.name = name
        self.cell_number = cell_number
        self.property_type = property_type
        self.price = price
        self.rent = rent
        self.buildings_count = 0
        self.house_price = 0
        self.owner: (Player, None) = None
        self.country: CountryTypeEnum

    def is_owned(self):
        if self.owner:
            return True
        else:
            return False

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

    def destroy_building(self):
        if self.buildings_count > 0:
            self.buildings_count -= 1
            return self.house_price / 2
        else:
            return -1

    def __str__(self):
        output = str(self.cell_number) + self.name + " ** number of buildings:" + str(
            self.buildings_count) + " ** " + str(self.house_price)
