from die import Die


class TestDie:

    def __init__(self):
        self.sides = ["John Snow", "Tyrion Lannister", "Brienne of Tarth"]

    def test_die_define(self):
        
        # we test our arg input validation
        try:
            Die(*self.sides[-1])
        except ValueError:
            pass
        self.new_die = Die(*self.sides)

    def test_die_roll(self):
        test_value = self.new_die.roll()
        if len(self.new_die.currentValue) and test_value == self.new_die.currentValue:
            print(self.new_die)
        else:
            print("die roll failed to set current_value")

    def run_tests(self):
        self.test_die_define()
        self.test_die_roll()


if __name__ == '__main__':
    new_test = TestDie()
    new_test.run_tests()
