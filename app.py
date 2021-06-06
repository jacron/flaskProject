from flask import Flask, render_template, request, make_response, redirect

from get_files import get_exchange_files
from read_exchange import read_exchange
from settings import SAMPLEDIR, COOKIE_PATH_NAME, DIRS, FONT_NAME, DEFAULT_FONT
from write_exchange import write_exchange

app = Flask(__name__)


@app.route('/setpath', methods=['POST', 'GET'])
def path_page():
    if request.method == 'POST':
        path = request.form['exchange_path']
        resp = make_response(render_template('setpath.html', path=path))
        resp.set_cookie(COOKIE_PATH_NAME, path)
        return resp


@app.route('/')
def index_page():
    path = request.cookies.get(COOKIE_PATH_NAME) or SAMPLEDIR
    names = get_exchange_files(path, '.bl8')
    return render_template('index.html', names=names, path=path)


def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1].lower() == 'bl8'


@app.route('/exchange', methods=['POST', 'GET'])
@app.route('/exchange/<filename>', methods=['POST', 'GET'])
@app.route('/exchange/<filename>/<code>', methods=['POST', 'GET'])
def read(filename=None, code=None):

    if request.method == 'POST':
        if 'content' in request.form:
            content = request.form['content']
            filename = request.form['filename']
            path = request.cookies.get(COOKIE_PATH_NAME) or SAMPLEDIR
            write_exchange(content, filename, path)
            return redirect('/exchange/' + filename)
        if 'exchangepath' in request.form:
            response = make_response()
            response.set_cookie(COOKIE_PATH_NAME, request.form['exchangepath'])
            response.headers['location'] = '/exchange'
            return response, 302
        if 'filename' in request.form:
            return redirect('/exchange/' + request.form['filename'])
        if 'font' in request.form:
            response = make_response()
            response.set_cookie(FONT_NAME, request.form['font'])
            response.headers['location'] = '/exchange/' + filename
            return response, 302
        if 'filter' in request.form:
            filter_ = request.form['filter']
            if filter_ != -1:
                return redirect('/exchange/' + filename + '/' + filter_)

    path = request.cookies.get(COOKIE_PATH_NAME) or SAMPLEDIR
    names = get_exchange_files(path, '.bl8')
    data = None
    content = None
    font = request.cookies.get(FONT_NAME) or DEFAULT_FONT
    if len(names) > 0 and filename:
        if code == '-1':
            code = None
        data = read_exchange(filename, path, code)
        if data.get('lines'):
            content = ''.join(data['lines'])
    return render_template('form/form.html',
                           title=filename,
                           content=content,
                           path=path,
                           paths=DIRS,
                           names=names,
                           font=font,
                           code=code,
                           data=data)


if __name__ == '__main__':
    app.run()
