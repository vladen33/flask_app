from flask import jsonify

from . import app


class InvalidRequestError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


# Создайте тут функцию — обработчик исключения InvalidRequestError.
@app.errorhandler(InvalidRequestError)
def invalid_request(error):
    return jsonify(error.to_dict()), 400
