import datetime

from src.gamma.challenge.domain.challenge import Challenge, ChallengeRepository


class ChallengeList:

    def __init__(self, repository: ChallengeRepository) -> None:
        self.repository = repository

    def excecute(self):
        challenges = self.repository.find_all()

        data = []
        for challenge in challenges:  # type: Challenge
            data.append(self._process(challenge))

        return data

    @classmethod
    def _process(cls, challenge: Challenge):
        return {
            'id': challenge.id,
            'title': challenge.title
        }
