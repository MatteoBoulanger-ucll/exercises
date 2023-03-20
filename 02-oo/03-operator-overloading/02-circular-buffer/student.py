class CircularBuffer:
    def __init__(self, maximum_size):
        self.__maximum_size = maximum_size
        self.__item_lijst = []

    def add(self, item):
        self.__item_lijst.append(item)
        if len(self.__item_lijst) > self.__maximum_size:
            self.__item_lijst.pop(0)

    def __getitem__(self, index):
        return self.__item_lijst[index]

    def __len__(self):
        return len(self.__item_lijst)
