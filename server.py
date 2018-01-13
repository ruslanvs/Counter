from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "adfj;als;dkfa34534ijo345i@#$$%$^uireu"

@app.route( "/" )
def front_page():
    
    if "counter" not in session:
        session["counter"] = 0
    session["counter"] += 2

    counter = session["counter"]

    return render_template( "index.html", counter = counter )

@app.route( "/result", methods = ["POST"])
def result():
    return redirect( "/" )


# @app.route( "/result", methods = ["post"])
# def result():
#     iname = request.form["fname"]
#     location = request.form["location"]
#     language = request.form["language"]
#     comment = request.form["comment"]

#     return render_template( "result.html", iname = iname, language = language, location = location, comment = comment )
#     return redirect( "/" )

# @app.route( "/process", methods = ["post"])
# def process():
#     print "Data from form:"
#     print request.form
#     name = request.form["name"]
#     print name
#     return redirect( "/" )

app.run( debug = True )