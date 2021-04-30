from datetime import datetime
from utils import *
import pickle

#A day is divided into 10 minute intervals
day = 24*6

class TimeTracer:
	def __init__(self):
		#A matrix can store data for an entire year, create a new file if overlap is starting to occur
		#ALL of these need to be imported from pkl files!

		### TBD ###
		
		self.matr = [[None]*day]*365
		self.act_file = "str1.pkl"
		self.file_names = [self.act_file]
		
		#need to import this from a pkl as well!
		self.pt_d = 0
		self.pt_sl = 0
		self.pt_datetime = 0

		#Print intro on start-up
		diff = self.pt_datetime-datetime.now() 
		if diff.total_seconds() > 5*60 or t2idx(self.pt_datetime)!=t2idx(datetime.now()):
			intro(False, self.pt_d, self.pt_sl, self.pt_datetime)
		else:
			intro(True)

	def run(self):
