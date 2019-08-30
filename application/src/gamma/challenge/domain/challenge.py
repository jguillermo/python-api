from abc import abstractmethod, ABC


class Challenge:
    def __init__(self, id, title) -> None:
        self.id = id
        self.title = title


class ChallengeRepository(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass
