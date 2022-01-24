from typing import List


class Response:

    def __init__(self, code: int):
        self.code = code

    def fail(self, errors: List[str] = None, message: str = None):
        response = {
            'code': self.code
        }
        if errors:
            response['errors'] = errors
        if message:
            response['message'] = message
        return response

    def success(self, data: dict = None):
        response = {
            'code': self.code
        }
        if data:
            response['data'] = data
        return response
