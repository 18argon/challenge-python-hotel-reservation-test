from unittest import TestCase
import pytest
from context import src
from src.my_module import Hotel, CUSTOMER_TYPES, DAYS_OF_WEEK


class HotelTest(TestCase):
    dummy_hotel = Hotel('Bridgewood', 4, 160, 60, 110, 50)

    def test_hotel_is_properly_initialized(self):
        new_hotel = Hotel('Bridgewood', 1, 120, 70, 100, 50)
        self.assertEqual('Bridgewood', new_hotel.name)
        self.assertEqual(1, new_hotel.level)
        self.assertEqual(120, new_hotel.regular_weekday)
        self.assertEqual(70, new_hotel.regular_weekend)
        self.assertEqual(100, new_hotel.rewards_weekday)
        self.assertEqual(50, new_hotel.rewards_weekend)

    def test_exception_on_invalid_day(self):
        day = 'foo'
        with pytest.raises(ValueError) as _:
            self.dummy_hotel.get_cost('Rewards', [day])

    def test_no_exception_on_valid_day(self):
        for day in DAYS_OF_WEEK:
            self.dummy_hotel.get_cost('Rewards', [day])

    def test_exception_on_invalid_customer_type(self):
        customer_type = 'foo'
        with pytest.raises(ValueError) as _:
            self.dummy_hotel.get_cost(customer_type, ['mon'])

    def test_no_exception_on_valid_customer_type(self):
        for customer_type in CUSTOMER_TYPES:
            self.dummy_hotel.get_cost(customer_type, ['mon'])

    def test_allweek_rewards_cost(self):
        result = 650
        self.assertEqual(
            result, self.dummy_hotel.get_cost('Rewards', DAYS_OF_WEEK))

    def test_allweek_regular_cost(self):
        result = 920
        self.assertEqual(
            result, self.dummy_hotel.get_cost('Regular', DAYS_OF_WEEK))

    def test_weekend_regular_cost(self):
        result = 60
        weekend = ['sat', 'sun']
        for day in weekend:
            self.assertEqual(
                result, self.dummy_hotel.get_cost('Regular', [day]))

    def test_weekend_rewards_cost(self):
        result = 50
        weekend = ['sat', 'sun']
        for day in weekend:
            self.assertEqual(
                result, self.dummy_hotel.get_cost('Rewards', [day]))

    def test_weekday_regular_cost(self):
        result = 160
        weekend = ['mon', 'tues', 'wed', 'thur', 'fri']
        for day in weekend:
            self.assertEqual(
                result, self.dummy_hotel.get_cost('Regular', [day]))

    def test_weekday_rewards_cost(self):
        result = 110
        weekend = ['mon', 'tues', 'wed', 'thur', 'fri']
        for day in weekend:
            self.assertEqual(
                result, self.dummy_hotel.get_cost('Rewards', [day]))

    def test_repeated_days_cost(self):
        result = 100
        self.assertEqual(result, self.dummy_hotel.get_cost('Rewards', ['sat', 'sat']))
