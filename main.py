class SpaceObject:
    def __init__(self, name: str, acceleration_of_free_fall: float):
        self.name = name
        self.acceleration_of_free_fall = acceleration_of_free_fall

    def weight(self: float):
        list_space_object = [moon, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto,
                             moon_jupiter_io, moon_jupiter_europa, moon_jupiter_ganymede, moon_jupiter_callisto, sun]
        if self > 0:
            for i in list_space_object:
                print(f'{i.name}: {(i.acceleration_of_free_fall * self):.1f}кг')
        elif self == 0:
            print("\033[31m{}".format(f'Ваш вес не может быть равен нулю!'))
            return
        elif self < 0:
            print("\033[31m{}".format(f'Ваш вес не может быть отрицательный!'))
            return
        else:
            print("\033[31m{}".format(f'Вы ничего не ввели!'))
        print('🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣')


try:
    moon = SpaceObject('Луна', 0.165)
    mercury = SpaceObject('Меркурий', 0.38)
    venus = SpaceObject('Венера', 0.906)
    earth = SpaceObject('Земля', 1.0)
    mars = SpaceObject('Марс', 0.378)
    jupiter = SpaceObject('Юпитер', 2.442)
    saturn = SpaceObject('Сатурн', 1.065)
    uranus = SpaceObject('Уран', 0.903)
    neptune = SpaceObject('Нептун', 1.131)
    pluto = SpaceObject('Плутон', 0.063)
    moon_jupiter_io = SpaceObject('Ио (спутник Юпитера)', 0.183)
    moon_jupiter_europa = SpaceObject('Европа (спутник Юпитера)', 0.134)
    moon_jupiter_ganymede = SpaceObject('Ганимед (спутник Юпитера)', 0.146)
    moon_jupiter_callisto = SpaceObject('Каллисто (спутник Юпитера)', 0.126)
    sun = SpaceObject('Солнце', 27.85)
    str_weight = input('Тебе интересно какой будет твой вес\nна других объектах солнечной системы?'
                       '\n😎 Тогда введи свой вес в кг: ')
    print('-------------------------------')
    SpaceObject.weight(float(str_weight.replace(',', '.')))
except ValueError:
    print("\033[31m{}".format(f'Введены некорректные данные Вашего веса!'))
