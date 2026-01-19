
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
@app.route('/review')
def review():
    return render_template('review.html', data=mod.dictreturn())

# edit
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method=='POST':
        if request.form['inputdata']:       # add
            mod.dictionerizer(mod.dictreturn(), request.form['inputdata'])
    return render_template('edit.html', data=mod.dictreturn())

# settings
@app.route('/settings')
def settings():
    return render_template('settings.html')







app.run(debug=True)
