from flask import Flask, render_template, request, make_response

from get_files import get_exchange_files
from read_exchange import read_exchange
from settings import sampledir, cookie_path_name
from write_exchange import write_exchange

app = Flask(__name__)


@app.route('/setpath', methods=['POST', 'GET'])
def path_page():
    if request.method == 'POST':
        path = request.form['exchange_path']
        resp = make_response(render_template('setpath.html', path=path))
        resp.set_cookie(cookie_path_name, path)
        return resp


@app.route('/')
def index_page():
    names = get_exchange_files(request)
    path = request.cookies.get(cookie_path_name) or sampledir
    return render_template('index.html', names=names, path=path)


@app.route('/exchange/<filename>', methods=['POST', 'GET'])
def read(filename):
    data = read_exchange(filename)
    if request.method == 'POST':
        write_exchange(request.form, filename)
        data = read_exchange(filename)
    return render_template('form/form.html', title=filename, data=data)


if __name__ == '__main__':
    app.run()
