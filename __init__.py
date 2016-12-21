from sopel import module
from ks_scrape import *
from time import sleep
from threading import Thread
from re import match

def setup(bot):
	def monitor(bot):
		sleep(5)
		while True:
			sleep(300)
	targs = (bot,)
	t = Thread(target=monitor, args=targs)
	t.start()

def add_ks(address):
	blah = match('(https?://www.kickstarter.com/projects/\d+/.+?)(/.+|\?.+)?$', text)
	if blah == None:
		return None
	address = blah.group(1)
	data = scrape_data(address)
	data = process_data(data)
	f = open('ks_list', 'a', encoding='utf-8')
	f.write(data['name'] + '\t' + address + '\n')
	f.close()
	return data
	
@module.commands('ksstatus')
def ksstatus(bot, trigger):
	return
	
@module.commands('addks')
def addks(bot, trigger):
	ks_data = add_ks(address)
	if ks_data == None:
		return bot.say("Please provide a valid Kickstarter address.")		
	return