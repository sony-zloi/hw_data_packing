import pickle
import json
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Stadium:
    """
    Задание 3
    Реализуйте класс «Стадион». Необходимо хранить в полях класса:
    - название стадиона,
    - дату открытия,
    - страну,
    - город,
    - вместимость.
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    name: str
    year: int
    country: str
    city: str
    capacity: int

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

    def getCountry(self):
        return self.country

    def setCountry(self, value):
        if not value:
            raise ValueError
        self.country = value

    def getCity(self):
        return self.city

    def setCity(self, value):
        if not value:
            raise ValueError
        self.city = value

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, value):
        if not value:
            raise ValueError
        self.capacity = value

    def as_dict(self):
        return {'name': self.name, 'year': self.year, 'country': self.country, 'city': self.city,
                'capacity': self.capacity}

    def json_serialize(self) -> str:
        return json.dumps(self.as_dict())

    @staticmethod
    def json_deserialize(value: str) -> Dict[str, Any]:
        return json.loads(value)

    def pickle_serialize(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def pickle_deserialize(value: bytes) -> "Stadium":
        return pickle.loads(value)