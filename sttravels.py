from flask import request
from flask import Flask
from flask import render_template

app = Flask("MyApp") #define the app

@app.route("/")
def hello():
	return render_template("hello.html")

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())


@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form_data
	print form_data['name']
	print form_data['email']
	return "All OK"



app.run()

#BELOW THIS WAS MY ORGINAL VERSION THAT I MADE ^ THE ABOVE VERSION WAS GIVEN TO ME BY SASHA 

#from flask import request
#from flask import Flask 
#from Flask import render_template 

#app = Flask ("My app") # Define the app


# @app.route ("/signup"), methods=['POST']
  #def sign_up ():
  #from_data = request.form
 # print form_data ['name']
 # print form_data ['email']
#  return "All OK"