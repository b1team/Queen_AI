from flask import Flask
from flask import render_template, url_for
from flask import request, redirect
from flask import session
from heuristic import get_queen_position
import time

app = Flask(__name__)
app.secret_key = '12134eafhajsdhjasvdasds'


@app.route('/')
@app.route('/sort/<int:N>/<int:num>', methods=['GET', 'POST'])
def queen_sort(N=8, num=1):
    error = False
    if N < 4:
        N = 4
        error = True

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
        return redirect(f'/sort/{N}/1')


@app.route('/next', methods=['GET', 'POST'])
def get_next():
    if request.method == 'POST':
        N = session.get('N')
        num = session.get('num')
        num = int(num) + 1
        result_number = session.get('result_number')
        if num > result_number:
            num = 1

        return redirect(f'/sort/{N}/{num}')


@app.route('/prev', methods=['GET', 'POST'])
def get_prev():
    if request.method == 'POST':
        N = session.get('N')
        num = session.get('num')
        num = int(num) - 1
        result_number = session.get('result_number')
        if num < 1:
            num = result_number

        return redirect(f'/sort/{N}/{num}')
    pass


@app.route('/find', methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
        N = session.get('N')
        num = request.form['index']
        result_number = session.get('result_number')
        if int(num) < 1 or int(num) > result_number:
            num = 1

        return redirect(f'/sort/{N}/{num}')


if __name__ == '__main__':
    app.run(debug=True)