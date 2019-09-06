import unittest
from unittest import mock

from src.gamma.challenge.application.challenge_list import ChallengeList
from src.gamma.challenge.domain.challenge import ChallengeRepository, Challenge, ChallengeId, ChallengeTitle


class ChallengeMockRepository:

    @staticmethod
    def ok() -> ChallengeRepository:
        repository = mock.create_autospec(ChallengeRepository)
        repository.find_all.return_value = [
            Challenge(ChallengeId('dfb7a1a1-4d78-4575-b035-3ec2fa6097e9'), ChallengeTitle('a')),
            Challenge(ChallengeId('b4d51f9e-cc29-4e52-a351-4156149b3ef1'), ChallengeTitle('b'))
        ]
        return repository


class TestGammaApplicationChallengeList(unittest.TestCase):

    def test_exception_app_empty(self):
        service = ChallengeList(ChallengeMockRepository.ok())
        data = service.excecute()

        self.assertEqual([
            {'id': 'dfb7a1a1-4d78-4575-b035-3ec2fa6097e9', 'title': 'a'},
            {'id': 'b4d51f9e-cc29-4e52-a351-4156149b3ef1', 'title': 'b'}], data)
