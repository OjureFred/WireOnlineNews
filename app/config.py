class Config:
    '''
    General configuration parent class
    '''
    pass
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=0f91a1188bde4ec2a617cbda88fc63d1'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
