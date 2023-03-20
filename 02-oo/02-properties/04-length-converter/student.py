class LengthConverter:

    def __init__(self):
        self.__length_in_meter = 0

    @property
    def meter(self):
        return self.__length_in_meter

    @meter.setter
    def meter(self, value):
        self.__length_in_meter = value

    @property
    def feet(self):
        return self.__length_in_meter * 3.28084

    @feet.setter
    def feet(self, value):
        self.__length_in_meter = value/3.28084

    @property
    def inch(self):
        return self.__length_in_meter*39.3701

    @inch.setter
    def feet(self, value):
        self.__length_in_meter = value/39.3701
