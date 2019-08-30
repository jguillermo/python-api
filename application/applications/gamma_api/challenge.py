from flask_restful import Resource

from applications.container import GammaServiceFactory


class ChallengeResource(Resource):

    def get(self):
        return GammaServiceFactory.list_challenge().excecute(), 200
