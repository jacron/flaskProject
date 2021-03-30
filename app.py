import os

from flask import Flask, render_template, request
from read_exchange import read_exchange
from settings import sampledir
from write_exchange import write_exchange

app = Flask(__name__)


@app.route('/')
def index_page():
    names = []
    files = os.listdir(sampledir)
    for file in files:
        if file.endswith('.bl8'):
            names.append(file)
    return render_template('index.html', names=names)


@app.route('/exchange/<filename>', methods=['POST', 'GET'])
def read(filename):
    data = read_exchange(filename)
    if request.method == 'POST':
        write_exchange(request.form, filename)
        data = read_exchange(filename)
    return render_template('form.html', title=filename, data=data)


if __name__ == '__main__':
    app.run()
