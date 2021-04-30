from datetime import datetime

#Get the index according to datetime.now()
def t2idx(time):
	print(time)
	hr = time.hour
	m = time.minute
	return int((hr*60+m)/10)

#Get the input from user
def get_inp(text):
	print(text)
	resp = input(">> ")
	return resp

#Print intro on startup
def intro(done,d=0,sl=0,dt=0):
	if not done:
		t_diff = datetime.now()-dt
		##CHECK AND DEBUG
		print("Hey. There's a gap of "+ str(t_diff) +" time in your tracking, amounting to "+ str(t2idx(datetime.now())-sl)+((datetime.now().Date-dt.Date).TotalDays)*24*6) +" slots. Do fill it up retard!")
	else:
		print("You're up-to-date! Nice!")