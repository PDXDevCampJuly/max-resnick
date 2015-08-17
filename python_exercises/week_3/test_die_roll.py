__author__ = 'Maxwell J. Resnick'

import unittest
from die import Die


class DieRollTest(unittest.TestCase):
    """Test the roll functionality of the Die class' roll function."""

    def setUp(self):
        self.possible_values = ["John Snow", "Tyrion Lannister",
                                "Brienne of Tarth", 1, 2]
        self.new_die = Die(*self.possible_values)

        print(self.shortDescription())

    def test_roll_once(self):
        """roll the dice once and ensure the value is in possibleValues"""
        self.assertIn(self.new_die.roll(), self.possible_values,
                      "Asserted rolled value not in possible_values")

    def test_rolled_value_changes(self):
        """tests that the dice's returned value does actually change."""
        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
                print("Rolled Die value {} is different than Holding Value"
                    .format(
                    self.new_die.currentValue, holding_value
                ))
                self.assertTrue(True)
                return

        error_message = "Holding value was the same for 10 rolls."
        self.assertTrue(False, error_message)

    def test_currentValue_is_updated_to_rolled_value(self):
        """Make sure that the roll function does update self.currentValue"""
        # make sure new initialized die, has a currentValue of 0
        self.assertEqual('', self.new_die.currentValue)
        new_roll = self.new_die.roll()
        self.assertEqual(new_roll, self.new_die.currentValue,
                         "The rolled value doesn't equal currentValue")


if __name__ == '__main__':
    unittest.main()
