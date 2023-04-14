from Enums import PropertyTypeEnum, CountryTypeEnum
from Property import Property


class Board:
    jail_address = 11

    board = [
        Property(cell_number=1, name="GO", property_type=PropertyTypeEnum.GO),
        Property(cell_number=2, name="Rio", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.BRAZIL,
                 price=200, rent=8),
        Property(cell_number=3, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, rent=8),
        Property(cell_number=4, name="Salvador", property_type=PropertyTypeEnum.LANDMARK,
                 country=CountryTypeEnum.BRAZIL, price=200, rent=8),

        Property(cell_number=5, name="Income Tax", property_type=PropertyTypeEnum.INCOME_TAX),
        Property(cell_number=6, name="Kings Cross Station", property_type=PropertyTypeEnum.STATION, price=200, rent=8),

        Property(cell_number=7, name="Amol", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.IRAN,
                 price=200, rent=8),
        Property(cell_number=8, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, rent=8),
        Property(cell_number=9, name="Tehran", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.IRAN,
                 price=100, rent=6),
        Property(cell_number=10, name="Qazvin", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.IRAN,
                 price=120, rent=7),
        Property(cell_number=11, name="Jail / Just Visiting", property_type=PropertyTypeEnum.JAIL),
        Property(cell_number=12, name="Pall Mall", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=13, name="Electric Company", property_type=PropertyTypeEnum.COMPANY, price=200, rent=8),
        Property(cell_number=14, name="Whitehall", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=15, name="Northumberland Avenue", property_type=PropertyTypeEnum.LANDMARK, price=200,
                 rent=8),
        Property(cell_number=16, name="Marylebone Station", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=17, name="Bow Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=18, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, rent=8),
        Property(cell_number=19, name="Marlborough Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=20, name="Vine Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=21, name="Free Parking", property_type=PropertyTypeEnum.PARKING, price=200, rent=8),

        Property(cell_number=22, name="Strand", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=23, name="Chance", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),

        Property(cell_number=24, name="Fleet Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=25, name="Trafalgar Square", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=26, name="Fenchurch St.Station", property_type=PropertyTypeEnum.LANDMARK, price=200,
                 rent=8),
        Property(cell_number=27, name="Leicester Square", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=28, name="Coventry Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=29, name="Water Works", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=30, name="Piccadilly", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=31, name="Go To Jail", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=32, name="Regent Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=33, name="Oxford Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=34, name="Community Chest", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=35, name="Bond Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=36, name="Liverpool St. Station", property_type=PropertyTypeEnum.LANDMARK, price=200,
                 rent=8),
        Property(cell_number=37, name="Community Chest", property_type=None, price=200, rent=8),
        Property(cell_number=38, name="Park Lane", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=39, name="Super Tax", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        Property(cell_number=40, name="Mayfair", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
    ]

    @classmethod
    def return_board(cls):
        return cls.board

    @classmethod
    def number_of_cities_in_a_country(cls, given_country: CountryTypeEnum):
        count = 0
        for _property in cls.board:
            if _property.country == given_country:
                count += 1
        return count

    @classmethod
    def upgrade_cities_to_upgradable(cls, given_country: CountryTypeEnum):
        for _property in cls.board:
            if _property.country == given_country:
                _property.is_upgradable = True


