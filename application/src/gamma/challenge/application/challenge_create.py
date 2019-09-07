from src.gamma.challenge.domain.challenge import Challenge, ChallengeRepository, ChallengeId, ChallengeTitle
from src.shared.exception import BadRequest


class ChallengeCreateInput:
    def __init__(self, id, title) -> None:
        self.id = ChallengeId(id)
        self.title = ChallengeTitle(title)


class ChallengeCreate:

    def __init__(self, repository: ChallengeRepository) -> None:
        self.repository = repository

    def excecute(self, input: ChallengeCreateInput):
        challenge_exist = self.repository.find_by_id(input.id.value())
        if challenge_exist is not None:
            raise BadRequest(4096, "Ya existe este Id")

        challenge = Challenge.create(input.id.value(), input.title.value())
        self.repository.persist(challenge)
        return True
