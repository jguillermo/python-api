import unittest
from unittest import mock

from src.gamma.challenge.application.challenge_list import ChallengeList
from src.gamma.challenge.domain.challenge import ChallengeRepository, Challenge, ChallengeId, ChallengeTitle


class ChallengeMockRepository:

    @staticmethod
    def ok() -> ChallengeRepository:
        repository = mock.create_autospec(ChallengeRepository)
        repository.find_all.return_value = [
            Challenge(ChallengeId('1'), ChallengeTitle('a')),
            Challenge(ChallengeId('2'), ChallengeTitle('b'))
        ]
        return repository


class TestGammaApplicationChallengeList(unittest.TestCase):

    def test_exception_app_empty(self):
        service = ChallengeList(ChallengeMockRepository.ok())
        data = service.excecute()

        self.assertEqual([{'id': '1', 'title': 'a'}, {'id': '2', 'title': 'b'}], data)
