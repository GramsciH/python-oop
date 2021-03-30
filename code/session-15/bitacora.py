from person import Person

class Bitacora(object):
    _instance = None
    def __init__(self):
        print("INIT")
        self.__people_sick = []
        self.__people_recovered = []
        self.__people_helthy = []

    def __new__(cls):
        if cls._instance is None:
            print("NEW")
            cls._instance = super(Bitacora, cls).__new__(cls)
        return cls._instance



    def add_sick_person(self, person):
        self.__people_sick.append(person)

    def add_recovered_person(self, person):
        self.__people_recovered.append(person)

    def add_helthy_person(self, person):
        self.__people_helthy.append(person)

    def remove_sick_person(self, person):
        self.__people_sick.remove(person)

    @property
    def people_sick(self):
        return self.__people_sick

    @property
    def people_recovered(self):
        return self.__people_recovered

    @property
    def people_helthy(self):
        return self.__people_helthy


# b1 = Bitacora()
# b2 = Bitacora()

# print(b1 == b2)
