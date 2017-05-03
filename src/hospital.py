class Hospital():

    def __init__(self, name):
        self.__name = name
        self.__id = None

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def save(self):
        self.__id = 1
