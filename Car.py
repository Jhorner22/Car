
from flask import Flask
from gpiozero import AngularServo
from time import sleep

app = Flask(_name_)

s1 = AngularServo(17, min_angle=-90, max_angle=90)
s2 = AngularServo(27, min_angle=-90, max_angle=90)

def Right_Motor_Forward(lforward):
	if lforward == True:
		s1.angle = -90
		sleep(1)
def Right_Motor_Backward(lbackward):
	if lbackward == True:
		s1.angle = 90
		sleep(500)
def Left_Motor_Forward(rforward):
	if rforward == True:
		s2.angle = 90
		sleep(500)
def Left_Motor_Backward(rbackward):
	if rbackward == True:
		s2.angle = -90
		sleep(500)

@app.route("/lft")
	lforward = True
@app.route("/lbt")

@app.route("/rft")

@app.route("/rbt")

@app.route("/lff")

@app.route("/lbf")

@app.route("/rff")

@app.route("/tbf")


while True:
	lforward = False
	lbackward = False
	rforward = False
	rbackward = False
	Right_Motor_Forward(lforward)
	Right_Motor_Backward(lbackward)
	Left_Motor_Forward(rforward)
