class Configuration(object):

    pass


class DevelopmentConfiguration(Configuration):

    DEBUG = True
    TESTING = False


class ProductionConfiguration(Configuration):

    DEBUG = False
    TESTING = False


class TestingConfiguration(Configuration):

    DEBUG = False
    TESTING = True


configuration = {
    'development': DevelopmentConfiguration,
    'production': ProductionConfiguration,
    'testing': TestingConfiguration
}
