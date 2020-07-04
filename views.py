from flask import render_template
from app import app
from app.request import get_news

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting news item
    general_online_news = get_news("general")
    business_online_news = get_news("business")
    technology_online_news = get_news("technology")

    print(general_online_news)
    title = "Welcome to Wire Online News Service"
    return render_template('index.html', title = title, general= general_online_news, business = business_online_news, technology = technology_online_news)


@app.route('/news/<news_id>')
def news(news_id):
    '''
    Views news function that returns news from a particular source
    '''
    return render_template('news.html',id = news_id)