from sopel import module
from ks_scrape import *
from time import sleep
from threading import Thread

def setup(bot):
	def monitor(bot):
		sleep(5)
			while True:
				sleep(300)
	targs = (bot,)
	t = Thread(target=monitor, args=targs)
	t.start()

@module.commands('ksstatus')
def ksstatus(bot, trigger):
	return
	
@module.commands('addks')
def addks(bot, trigger):
	return