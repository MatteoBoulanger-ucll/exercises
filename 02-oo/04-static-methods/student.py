class Duration:
    def __init__(self, *, in_seconds):
        self.__in_seconds = in_seconds

    @property
    def seconds(self):
        return self.__in_seconds

    @property
    def minutes(self):
        return self.__in_seconds/60

    @property
    def hours(self):
        return self.__in_seconds/3600

    @staticmethod
    def from_seconds(value):
        return Duration(in_seconds=value)

    @staticmethod
    def from_minutes(value):
        return Duration(in_seconds=value*60)

    @staticmethod
    def from_hours(value):
        return Duration(in_seconds=value*3600)
