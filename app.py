from flask import Flask, render_template, request
from read_exchange import read_exchange
from write_exchange import write_exchange

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/exchange/<filename>', methods=['POST', 'GET'])
def read(filename):
    data = read_exchange(filename)
    if request.method == 'POST':
        write_exchange(request.form, filename)
    return render_template('form.html', title=filename, data=data)


if __name__ == '__main__':
    app.run()
