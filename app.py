from flask import Flask
from flask import render_template, url_for
from flask import request, redirect
from flask import session
from heuristic import get_queen_position
import time

app = Flask(__name__)
app.secret_key = '12134eafhajsdhjasvdasds'


@app.route('/')
@app.route('/solve/n=<int:N>/i=<int:num>', methods=['GET', 'POST'])
def queen_sort(N=4, num=1):
    error = False
    if N < 4:
        N = 4
        error = True
    if type(num) is not int:
        num = 1
    if type(N) is not int:
        N = 4

    start = time.time()
    pos = get_queen_position(N)
    end = time.time()

    session['num'] = num
    session['N'] = N
    result_number = len(pos)
    session['result_number'] = result_number

    return render_template('chessboard.html', queens = pos[num-1],
                            N = N, result_number=result_number,
                            error=error, num=num, time =(end-start))


@app.route('/queens', methods=['POST', 'GET'])
def get_queens():
    if request.method == 'POST':
        N = request.form.get('N')
        print(N)
        if not N:
            N = 4
        return redirect(f'/solve/n={N}/i=1')


@app.route('/next', methods=['GET', 'POST'])
def get_next():
    if request.method == 'POST':
        N = session.get('N')
        num = session.get('num')
        num = int(num) + 1
        result_number = session.get('result_number')
        if N is None or num is None or result_number is None:
            return redirect('/')
        if num > result_number:
            num = 1

        return redirect(f'/solve/n={N}/i={num}')


@app.route('/prev', methods=['GET', 'POST'])
def get_prev():
    if request.method == 'POST':
        N = session.get('N')
        num = session.get('num')
        num = int(num) - 1
        result_number = session.get('result_number')
        if N is None or num is None or result_number is None:
            return redirect('/')

        if num < 1:
            num = result_number

        return redirect(f'/solve/n={N}/i={num}')


@app.route('/find', methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
        N = session.get('N')
        num = request.form['index']
        result_number = session.get('result_number')
        if N is None or not num or result_number is None or type(num) is not int:
            return redirect('/')

        if int(num) < 1 or int(num) > result_number:
            num = 1

        return redirect(f'/solve/n={N}/i={num}')


if __name__ == '__main__':
    app.run(debug=True)