
import processing_module as mod
import random as r
import ast
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'iamthesonofpshs'


# startpage(index)
@app.route('/')
def startpage():
    return render_template('index.html')

# menu
@app.route('/menu')
def menu():
    session.clear()
    return render_template('menu.html')

# quiz
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # quizset 설정 안된 경우 설정
    if 'quizset' not in session:        # session은 페이지 바뀌어도 값 담을 수 있는 전역변수 딕셔너리 감성임
        quizset = mod.dictreturn()
        r.shuffle(quizset)
        session['quizset'] = quizset
        session['answerset'] = []
        session['cnt'] = 0
    # history 설정(이전 세트 불러오기용)
    if 'history' not in session:
        session['history'] = []
    
    quizset = session['quizset']
    answerset = session['answerset']
    cnt = session['cnt']

    if request.args.get('reset'):               # reset quiz(GET)
        session.clear()
        return redirect('/quiz')

    if request.method=='POST':                  # answer submitted
        if request.form['QAA']:
            answerset.append(request.form['QAA'])
            session['answerset'] = answerset
            session['cnt'] = cnt+1
    if session['cnt']>=len(quizset):            # quiz finished
        session['history'].append(quizset)
        session.clear()                         # reset quizset
        ox_list = mod.grading(quizset, answerset)
        mod.quizhistory(quizset, answerset, ox_list)    # save result

        return redirect('/score')
    else:
        return render_template('quizA.html', data=quizset[session['cnt']], cnt=session['cnt'])

# score
@app.route('/score')
def score():
    recentRes = ast.literal_eval(mod.readhistory(-1))        # history 중 마지막 기록 꺼내기
    return render_template('score.html', data=recentRes, score=recentRes[2].count('O'), qNum=len(recentRes[2]))

# review
@app.route('/review')
def review():
    if len(request.args)!=0:          # sort
        sortargslist = [
            request.args.get('O', 'off'),
            request.args.get('X', 'off'),
            request.args.get('N', 'off'),
            request.args.get('oNum'),
            request.args.get('xNum'),
            request.args.get('uT')
            ]
        hanjadict = mod.dictsort(sortargslist)
    else:
        hanjadict = mod.dictreturn()
            
    return render_template('review.html', data=hanjadict)

# edit
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method=='POST':
        if request.form['inputdata']:       # add
            mod.dictionerizer(mod.dictreturn(), request.form['inputdata'])
    if len(request.args)!=0:          # sort
        sortargslist = [
            request.args.get('O', 'off'),
            request.args.get('X', 'off'),
            request.args.get('N', 'off'),
            request.args.get('oNum'),
            request.args.get('xNum'),
            request.args.get('uT')
            ]
        hanjadict = mod.dictsort(sortargslist)
    else:
        hanjadict = mod.dictreturn()
            
    return render_template('edit.html', data=hanjadict)

# settings
@app.route('/settings')
def settings():
    return render_template('settings.html')






app.run(debug=True)
