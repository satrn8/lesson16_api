from utils.requests_helper import BaseSession


def reqres() -> BaseSession:
        reqres_api = 'https://reqres.in'
        return BaseSession(base_url=reqres_api)