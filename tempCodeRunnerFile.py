@app.route('/show')
def showregistrations():
    alldetails=students.query.all()
    print (alldetails)
    return render_template('show.html',alldetails=alldetails)
