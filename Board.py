from Enums import PropertyTypeEnum, CountryTypeEnum
from Property import Property


class Board:
    jail_address = 11

    board = [
        Property(cell_number=1, name="GO", property_type=PropertyTypeEnum.GO),
        Property(cell_number=2, name="Rio", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.BRAZIL,
                 price=60, mortgage=30, rent=2),
        Property(cell_number=3, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=60, mortgage=30, rent=4),
        Property(cell_number=4, name="Salvador", property_type=PropertyTypeEnum.LANDMARK,
                 country=CountryTypeEnum.BRAZIL, price=40, mortgage=20, rent=6),

        Property(cell_number=5, name="Income Tax", property_type=PropertyTypeEnum.INCOME_TAX),
        Property(cell_number=6, name="Rio Airport", property_type=PropertyTypeEnum.AIRPORT, country=CountryTypeEnum.BRAZIL, price=200, mortgage=100 ,rent=25),

        Property(cell_number=7, name="Amol", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.IRAN,
                 price=100, mortgage=50, rent=6),
        Property(cell_number=8, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, rent=8),
        Property(cell_number=9, name="Tehran", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.IRAN,
                 price=100, mortgage=50, rent=6),
        Property(cell_number=10, name="Qazvin", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.IRAN,
                 price=120, mortgage=60, rent=8),
        Property(cell_number=11, name="Jail / Just Visiting", property_type=PropertyTypeEnum.JAIL),

        Property(cell_number=12, name="Pall Mall", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.ITALY, price=140, mortgage=70, rent=10),
        Property(cell_number=13, name="Whitehall", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.ITALY, price=140, rent=10),
        Property(cell_number=14, name="Northumberland Avenue", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.ITALY, price=160, mortgage=80,
                 rent=14),
        Property(cell_number=15, name="Marylebone Airport", property_type=PropertyTypeEnum.AIRPORT,country=CountryTypeEnum.ITALY, price=200,mortgage=100, rent=25),
        Property(cell_number=16, name="Bow Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.GERMANY, price=180, mortgage=90, rent=14),
        Property(cell_number=17, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, mortgage=8),
        Property(cell_number=18, name="Marlborough Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.GERMANY, price=180, mortgage=90, rent=14),
        Property(cell_number=19, name="Vine Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.GERMANY, price=200, mortgage=100, rent=16),

        Property(cell_number=20, name="The Strand", property_type=PropertyTypeEnum.LANDMARK, price=220, mortgage=110, rent=18),
        Property(cell_number=21, name="Chance", property_type=PropertyTypeEnum.LANDMARK, price=200, mortgage=8),

        Property(cell_number=22, name="Fleet Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.GERMANY, price=220, mortgage=110, rent=18),
        Property(cell_number=23, name="Trafalgar Square", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.RUSSIA, price=240, mortgage=120, rent=20),
        Property(cell_number=24, name="Fenchurch St.Airport", property_type=PropertyTypeEnum.AIRPORT,country=CountryTypeEnum.RUSSIA, price=20,
                 mortgage=100, rent=25),
        Property(cell_number=25, name="Leicester Square", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.RUSSIA, price=260, mortgage=130, rent=22),
        Property(cell_number=26, name="Coventry Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.FRANCE, price=260, mortgage=130, rent=22),
        Property(cell_number=27, name="Water Works", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.FRANCE, price=150, mortgage=75, rent=4*dice),
        Property(cell_number=28, name="Piccadilly", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.FRANCE, price=280, mortgage=140, rent=22),
        Property(cell_number=29, name="Go To Jail", property_type=PropertyTypeEnum.GO_TO_JAIL),
        Property(cell_number=30, name="Regent Street", property_type=PropertyTypeEnum.LANDMARK, country=CountryTypeEnum.ENGLAND, price=300, mortgage=150, rent=26),
        Property(cell_number=31, name="Oxford Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.ENGLAND, price=300, mortgage=150, rent=26),
        Property(cell_number=32, name="Community Chest", property_type=PropertyTypeEnum.CHEST),
        Property(cell_number=33, name="Bond Street", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.ENGLAND, price=320, mortgage=160, rent=28),
        Property(cell_number=34, name="Liverpool St. Airport", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.ENGLAND, price=200,
                 mortgage=100 , rent=25),
        Property(cell_number=35, name="Community Chest", property_type=None, price=200, mortgage=8),
        Property(cell_number=36, name="Park Lane", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.AMERICA, price=350, mortgage=175 , rent=35),
        Property(cell_number=37, name="Super Tax", property_type=PropertyTypeEnum.SUPER_TAX ),
        Property(cell_number=38, name="Mayfair", property_type=PropertyTypeEnum.LANDMARK,country=CountryTypeEnum.AMERICA, price=400, mortgage=50 , rent=50),
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

    @classmethod
    def change_cities_to_not_upgradable(cls, given_country):
        for _property in cls.board:
            if _property.country == given_country:
                _property.is_upgradable = False


