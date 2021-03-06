﻿from flask import Flask, request, render_template

# just serve all the static files under root
app = Flask(__name__)
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


@app.route("/hello")
def helloworld():
    return 'hello world'
	
@app.route("/on")
def root():
    GPIO.output(8, GPIO.HIGH)
    print('on')
    return 'on'
    

@app.route("/off")
def off():
  GPIO.output(8, GPIO.LOW)
  print('off')
  return 'off'




# start listening
if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')

    
