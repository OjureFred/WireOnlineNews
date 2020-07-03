from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/news/<news_id>')
def news(news_id):
    '''
    Views news function that returns news from a particular source
    '''
    return render_template('news.html',id = news_id)