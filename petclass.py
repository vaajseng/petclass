


class pet:
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animaltype):
        self.__animal_type =animaltype

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    pets = pet()

    pets.set_name(input('Enter pet name'))
    pets.set_animal_type(input('Enter animal type'))
    pets.set_age(int(input('Enter the animal\'s age')))

    print('The pet\'s name is', pets.get_name())
    print('The animal is a', pets.get_animal_type())
    print(pets.get_name()+'\'s age is', pets.get_age(),'Years old.')

main()


