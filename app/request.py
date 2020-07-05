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

def get_news_item(id):
    '''
    Funtion to retrieve a single news item
    '''
    get_news_details_url = base_url.format(id)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')

            news_object = News(id,name,description,url,category,language, country)

    return news_object
    
def search_news(keyword):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey=0f91a1188bde4ec2a617cbda88fc63d1'.format(keyword)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_movie_results = None

        if search_news_response['sources']:
            search_news_list = search_news_response['sources']
            search_news_results = process_results(search_news_list)


    return search_news_results

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


