
import processing_module as mod
from flask import Flask, render_template, request
app = Flask(__name__)


# startpage(index)
@app.route('/')
def startpage():
    return render_template('index.html')

# menu
@app.route('/menu')
def menu():
    return render_template('menu.html')

# quiz
@app.route('/quiz')
def quiz():
    return render_template('quizA.html')

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
