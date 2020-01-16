from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Class SilverServiceTaxi that inherits from Taxi"""
    flagfall = 4.50

    def __init__(self, name, fanciness):
        """initialise a SilverServiceTaxi from Taxi"""
        super().__init__(self, name)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string"""
        return "{}, plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get the current fare"""
        return super().get_fare() + self.flagfall
