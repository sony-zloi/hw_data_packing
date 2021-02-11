import pickle
import json
from dataclasses import dataclass, field
from typing import *


@dataclass
class Book:
    """
    Задание 2
    Реализуйте класс «Книга». Необходимо хранить в полях класса:
    - название книги
    - год выпуска
    - издателя,
    - жанр
    - автора,
    - цену
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    name: str
    year: int
    publisher: str
    genre: str
    author: str
    cost: int

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

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, value):
        if not value:
            raise ValueError
        self.publisher = value

    def getGenre(self):
        return self.genre

    def setGenre(self, value):
        if not value:
            raise ValueError
        self.genre = value

    def getAuthor(self):
        return self.author

    def setAuthor(self, value):
        if not value:
            raise ValueError
        self.author = value

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
    def pickle_deserialize(value: bytes) -> "Book":
        return pickle.loads(value)