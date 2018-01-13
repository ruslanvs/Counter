from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "adfj;als;dkfa34534ijo345i@#$$%$^uireu"

@app.route( "/" )
def front_page():
    
    if "counter" not in session:
        session["counter"] = 0

    session["counter"] += 1
    counter = session["counter"]
    return render_template( "index.html", counter = counter )

@app.route( "/result", methods = ["POST"] )
def result():
    session["counter"] += 1
    
    return redirect( "/" )

@app.route( "/reset", methods = ["POST"] )
def reset():
    print "adas;lkj"
    session["counter"] = 0
    # session.clear() // also works
    return redirect( "/" )

app.run( debug = True )