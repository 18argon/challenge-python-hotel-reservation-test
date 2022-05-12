import re

DAYS_OF_WEEK = ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun']
CUSTOMER_TYPES = ['Regular', 'Rewards']


class Hotel:
    '''
    A class used to represent an Hotel

    Attributes
    ----------
    name: str
        The name of the hotel
    level: int
        The classification of the hotel
    regular_weekday: float
        The price for regular customers on weekdays
    regular_weekend: float
        The price for regular customers on weekends
    rewards_weekday: float
        The price for rewards customers on weekdays
    rewards_weekend: float
        The price for rewards customers on weekends
    '''

    def __init__(self, name, level, regular_weekday, regular_weekend, rewards_weekday, rewards_weekend):
        self.name = name
        self.level = level
        self.regular_weekday = regular_weekday
        self.regular_weekend = regular_weekend
        self.rewards_weekday = rewards_weekday
        self.rewards_weekend = rewards_weekend

    def get_cost(self, type, days):
        """
        Returns the cost for a customer of type ``type`` to stay in the hotel
        in the ``days`` indicated.

        Raise ``ValueError`` if receives an invalid customer type or day of the week
        """
        if not type in CUSTOMER_TYPES:
            raise ValueError(f'{type} - Invalid customer type.')

        if not all([day in DAYS_OF_WEEK for day in days]):
            raise ValueError('Invalid day of the week.')

        cost = 0
        if type == 'Regular':
            price_weekday, price_weekend = self.regular_weekday, self.regular_weekend
        else:
            price_weekday, price_weekend = self.rewards_weekday, self.rewards_weekend

        cost = sum([price_weekend if day == 'sun' or day == 'sat'
                    else price_weekday
                    for day in days])
        return cost


def get_hotels():
    """Returns a list of available hotels"""
    return [
        Hotel('Lakewood', 3, 110, 90, 80, 80),
        Hotel('Bridgewood', 4, 160, 60, 110, 50),
        Hotel('Ridgewood', 5, 220, 150, 100, 40),
    ]


def get_cheapest_hotel(entry):
    """Returns the cheapest hotel for the given entry"""
    # Extract the customer type and days of the week
    customer_type, days = entry.split(':')
    days = re.findall(r'\((\w+)\)', days)

    if len(days) == 0:
        return None

    # Find the price for each hotel
    prices = [(hotel.get_cost(customer_type, days), hotel.level, hotel.name)
              for hotel in get_hotels()]

    # Find the cheapest hotel with the highest classification
    cheapest_hotel = min(prices, key=lambda h: (h[0], -h[1]))
    return cheapest_hotel[2]


def main():
    entries = [
        'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)',
        'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)',
        'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)',
    ]
    for entry in entries:
        print(entry)
        print(get_cheapest_hotel(entry))


if __name__ == '__main__':
    main()
