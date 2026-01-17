
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

# review
@app.route('/<rue>')
def review(rue):
    return render_template('RnE.html', mode=rue)

# edit
@app.route('/<rue>', methods=['GET', 'POST'])
def edit(rue):
    if type(request.form['inputdata'])==str:       # add
        print(mod.dictionerizer(mod.dictreturn(), request.form['datain']))
    return render_template('RnE.html', mode=rue, data=mod.dictreturn())

# settings
@app.route('/settings')
def settings():
    return render_template('settings.html')







app.run(debug=True)