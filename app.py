from flask import Flask
from flask import render_template, url_for
from flask import request, redirect
from flask import session
from heuristic import get_queen_position
import time

app = Flask(__name__)
app.secret_key = '12134eafhajsdhjasvdasds'


@app.route('/')
@app.route('/solve', methods=['GET', 'POST'])
def queen_sort():
    n = request.args.get('n', 4, type=int)
    if not n or n < 4:
        n = 4

    i = request.args.get('i', 1, type=int)
    if not i or i < 0:
        i = 1

    if type(i) != type(1):
        i = 1
    if type(n) != type(1):
        n = 4

    start = time.time()
    pos = get_queen_position(n)
    end = time.time()

    result_number = len(pos)
    session['i'] = i
    session['n'] = n
    session['result_number'] = result_number

    return render_template('chessboard.html', queens = pos[i-1],
                            N = n, result_number=result_number,
                            num=i, time =(end-start))


@app.route('/queens', methods=['POST', 'GET'])
def get_queens():
    n = request.args.get('n', 4, type=int)
    i = request.args.get('i', 1, type=int)

    return redirect(f'/solve?n={n}&i={i}')


@app.route('/next', methods=['GET', 'POST'])
def get_next():
    if request.method == 'POST':
        n = session.get('n')
        i = session.get('i')
        i = int(i) + 1
        result_number = session.get('result_number')
        if n is None or i is None or result_number is None:
            return redirect('/')
        if i > result_number:
            i = 1

        return redirect(f'/solve?n={n}&i={i}')


@app.route('/prev', methods=['GET', 'POST'])
def get_prev():
    if request.method == 'POST':
        n = session.get('n')
        i = session.get('i')
        i = int(i) - 1
        result_number = session.get('result_number')
        if n is None or i is None or result_number is None:
            return redirect('/')

        if i < 1:
            i = result_number

        return redirect(f'/solve?n={n}&i={i}')


@app.route('/find', methods=['GET', 'POST'])
def get_result():
    n = session.get('n')
    i = request.args.get('i', 1, type=int)
    result_number = session.get('result_number')
    if n is None or not i or result_number is None or type(i) is not type(1):
        return redirect('/')

    if int(i) < 1 or int(i) > result_number:
        i = 1

    return redirect(f'/solve?n={n}&i={i}')


if __name__ == '__main__':
    app.run(debug=True)