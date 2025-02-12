from abc import ABCMeta, abstractmethod


class BaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def insert(self, id: int):
        raise NotImplementedError
