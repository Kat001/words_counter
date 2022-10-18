from flask import render_template, url_for, redirect
from words_scrapper import app
from words_scrapper import queue
from words_scrapper.tasks import count_words
from time import strftime
import json
from flask import request

from words_scrapper.models import PageWordsCount


@app.route("/", methods=['GET', 'POST'])
def index():
    print("request.method", request.method)
    if request.method == 'POST':
        page_url = request.form['page_url']
        print("calledd post", page_url)
        count_words(page_url)
        job = queue.enqueue(count_words, page_url)
        redirect('/')
    return render_template('index.html')

# @app.route("/")
# def home():
#     text = "This is a very long text from your ex"
#     job = queue.enqueue(count_words, text)
    
#     task = job.get_id()
#     result = {
#            "Task":job.get_id(),
#            "Time":strftime('%a, %d %b %Y %H:%M:%S')
#     }
#     return json.dumps({"result":result})

@app.route("/results", methods=['GET'])
def results():
    results = PageWordsCount.query.all()
    return render_template('results.html', results=results)

@app.route("/result/<result_id>", methods=['GET'])
def result(result_id):
    result = PageWordsCount.query.filter_by(id=result_id).first()
    return render_template('result.html', result=result)