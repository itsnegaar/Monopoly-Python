from Enums import PropertyTypeEnum
from Property import Property


class Board:
    @staticmethod
    def return_board():
        board = [
            Property(cell_number=1, name="GO", property_type=PropertyTypeEnum.GO),
            Property(cell_number=2, name="Old Kent Road", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=3, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, rent=8),
            Property(cell_number=4, name="Whitechapel Road", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),

            Property(cell_number=5, name="Income Tax", property_type=PropertyTypeEnum.INCOME_TAX),
            Property(cell_number=6, name="Kings Cross Station", property_type=PropertyTypeEnum.STATION, price=200, rent=8),

            Property(cell_number=7, name="The Angel Islington", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=8, name="Community Chest", property_type=PropertyTypeEnum.CHEST, price=200, rent=8),
            Property(cell_number=9, name="Euston Road", property_type=PropertyTypeEnum.LANDMARK),
            Property(cell_number=10, name="Pentonville Road", property_type=PropertyTypeEnum.LANDMARK),
            Property(cell_number=11, name="Jail / Just Visiting", property_type=PropertyTypeEnum.JAIL),
            Property(cell_number=12, name="Pall Mall", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=13, name="Electric Company", property_type=PropertyTypeEnum.COMPANY, price=200, rent=8),
            Property(cell_number=14, name="Whitehall", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=15, name="Northumberland Avenue", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
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
            Property(cell_number=26, name="Fenchurch St.Station", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=27, name="Leicester Square", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=28, name="Coventry Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=29, name="Water Works", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=30, name="Piccadilly", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=31, name="Go To Jail", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=32, name="Regent Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=33, name="Oxford Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=34, name="Community Chest", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=35, name="Bond Street", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=36, name="Liverpool St. Station", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=37, name="Community Chest", property_type=None, price=200, rent=8),
            Property(cell_number=38, name="Park Lane", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=39, name="Super Tax", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
            Property(cell_number=40, name="Mayfair", property_type=PropertyTypeEnum.LANDMARK, price=200, rent=8),
        ]

        return board
