# -*- coding: utf-8 -*-
from src.gamma.challenge.application.challenge_list import ChallengeList
from src.gamma.challenge.infrastructure.persistence import ChallengeRepositoryMysql


class GammaRepositoryFactory:
    @staticmethod
    def challenge_repository():
        return ChallengeRepositoryMysql()


class GammaServiceFactory:
    @staticmethod
    def list_challenge():
        return ChallengeList(repository=GammaRepositoryFactory.challenge_repository())
