import pickle
import json
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Car:
    """
    Задание 1
    Реализуйте класс «Автомобиль». Необходимо хранить
    в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
    методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    name: str
    year: int
    vendor: str
    power: int
    color: str
    cost: float

    def getName(self):
        return self.name

    def setName(self, value):
        if not value:
            raise ValueError
        self.name = value

    def getYear(self):
        return self.year

    def setYear(self, value):
        if not value:
            raise ValueError
        self.year = value

    def getVendor(self):
        return self.vendor

    def setVendor(self, value):
        if not value:
            raise ValueError
        self.vendor = value

    def getPower(self):
        return self.power

    def setPower(self, value):
        if not value:
            raise ValueError
        self.power = value

    def getColor(self):
        return self.color

    def setColor(self, value):
        if not value:
            raise ValueError
        self.color = value

    def getCost(self):
        return self.cost

    def setCost(self, value):
        if not value:
            raise ValueError
        self.cost = value

    def as_dict(self):
        return {'name': self.name, 'year': self.year, 'vendor': self.vendor, 'power': self.power,
                'color': self.color, 'cost': self.cost}

    def json_serialize(self) -> str:
        return json.dumps(self.as_dict())

    @staticmethod
    def json_deserialize(value: str) -> Dict[str, str]:
        return json.loads(value)

    def pickle_serialize(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def pickle_deserialize(value: bytes) -> "Car":
        return pickle.loads(value)


car1 = Car("Audi", 2001, "VAG", 230, "white", 25000)
print(car1.pickle_serialize())
print(car1.pickle_deserialize(car1.pickle_serialize()))
