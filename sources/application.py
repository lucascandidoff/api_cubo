from flask import Flask, jsonify, Response, request
from http import HTTPStatus
from sources.configuration import configuration
from sources.utils.response import Response
from sources.utils.setting import setting
from typing import Any
from werkzeug.exceptions import HTTPException
from sources.resources.cubo import cubo_api


def create_application(environment: str):

    application = Flask(__name__)
    application.config.from_object(configuration[environment])


    application.register_blueprint(cubo_api, url_prefix='/api/cubo')


    @application.before_request
    def before_request():
        pass

    @application.errorhandler(HTTPException)
    def http_exception(exception: Any):
        try:
            return jsonify({'errors': exception.errors, 'message': exception.message}), exception.code
        except AttributeError:
            return jsonify({'errors': exception.name, 'message': exception.description}), exception.code

    @application.route('/', methods=['GET'], strict_slashes=False)
    def health_check():
        response = {
            'application_name': setting.APPLICATION_NAME,
            'application_version': setting.APPLICATION_VERSION
        }
        return jsonify(Response(HTTPStatus.OK).success(response)), HTTPStatus.OK

    return application
