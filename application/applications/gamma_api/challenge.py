from flask_restful import Resource

from applications.container import GammaServiceFactory
from src.gamma.challenge.application.challenge_create import ChallengeCreateInput


class ChallengeResource(Resource):

    def get(self):
        return GammaServiceFactory.challenge_list().excecute(), 200

    def post(self):
        input = ChallengeCreateInput('sdf', 'tidsf')
        return GammaServiceFactory.challenge_create().excecute(input)
