from sources.application import create_application
from sources.utils.setting import setting

application = create_application(setting.FLASK_ENV)

if __name__ == '__main__':
    application.run(debug=setting.FLASK_DEBUG, host=setting.FLASK_HOST, port=setting.FLASK_PORT)
