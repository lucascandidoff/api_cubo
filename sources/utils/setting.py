import os


class Setting:

    API_V1: str = '/api/v1'

    APPLICATION_NAME: str = 'api-cubo'
    APPLICATION_VERSION: str = '0.0.0'

    FLASK_APP: str = os.environ.get('FLASK_APP', 'sources/main.py')
    FLASK_DEBUG: bool = os.environ.get('FLASK_DEBUG', True)
    FLASK_ENV: str = os.environ.get('FLASK_ENV', 'development')
    FLASK_HOST: str = os.environ.get('FLASK_HOST', '0.0.0.0')
    FLASK_PORT: int = os.environ.get('FLASK_PORT', 5000)


setting = Setting()
