from abc import abstractmethod, ABC

from src.shared.domain.types import TypeString, TypeId


class ChallengeId(TypeId):
    pass


class ChallengeTitle(TypeString):
    pass


class Challenge:
    def __init__(self, id: ChallengeId, title: ChallengeTitle) -> None:
        self.id = id
        self.title = title

    @classmethod
    def create(cls, id: ChallengeId, title: ChallengeTitle):
        return cls(id, title)


class ChallengeRepository(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id: ChallengeId):
        pass
