from flask import render_template, request, redirect, url_for
from app import app
from app.request import get_news, get_news_item, search_news

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

    title = "Welcome to Wire Online News Service"

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', keyword = search_news))
    else:
        return render_template('index.html', title = title, general= general_online_news, business = business_online_news, technology = technology_online_news)


@app.route('/news/<news_id>')
def news(news_id):
    '''
    Views news function that returns news from a particular source
    '''
    news_item = get_news_item(id)
    title = f'{news_item.id}'

    return render_template('news.html', title=title, news_item=news_item)
    
@app.route('/search/<keyword>')
def search(keyword):
    '''
    View function to display news search results given a keyword
    '''
    news_keyword = keyword.split(" ")
    keyword_name_format = "+".join(news_keyword)
    searched_news = search_news(keyword_name_format)
    
    title = f'search results for {keyword}'

    return render_template('search.html', keyword = keyword, news = searched_news)
    
