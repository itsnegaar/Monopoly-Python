from Enums import PropertyTypeEnum, CountryTypeEnum


class Property:
    def __init__(self, cell_number: int, name: str, property_type: PropertyTypeEnum, price: int = None,
                 rent: int = None, country: CountryTypeEnum = None):
        self.name = name
        self.cell_number = cell_number
        self.property_type = property_type
        self.price: int = price
        self.rent: int = rent
        self.buildings_count: int = 0
        self.house_price: int = 0
        self.owner = None
        self.country: CountryTypeEnum = country
        self.is_upgradable: bool = False
        self.is_mortgaged: bool = False

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
            self.rent /= 2
            return self.house_price / 2
        else:
            return -1

    def upgrade_buildings(self):
        pass

    def mortgage_building(self):
        pass

    def __repr__(self):
        output = str(self.cell_number) + " | " + self.name + " | number of buildings:" + str(
            self.buildings_count) + " | price: $" + str(self.price) + " | rent: $" + str(
            self.rent) + " | country:" + str(self.country)
        return output
