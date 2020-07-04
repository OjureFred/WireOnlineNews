from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
#api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
#base_url = app.config["MOVIE_API_BASE_URL"]
base_url = 'https://newsapi.org/v2/sources?apiKey=0f91a1188bde4ec2a617cbda88fc63d1'

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description =news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        news_object = News(id,name,description,url,category,language, country)
        news_results.append(news_object)

    return news_results