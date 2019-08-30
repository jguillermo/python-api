from abc import abstractmethod, ABC


class ApplicationService(ABC):
    @abstractmethod
    def execute(self, **kwargs):
        pass
