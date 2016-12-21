from sopel import module
from ks_scrape import *
from time import sleep
from threading import Thread
from re import match, split

def setup(bot):
	def monitor(bot):
		sleep(5)
		while True:
			f = open('ks_list', 'r', encoding='utf-8')
			for ks in f:
				[name, address] = split('\t', ks)
				name = name.strip()
				address = address.strip()
				ks_data = get_data(ks)
				if ks_data['updates'] != None:
					for update in ks_data['updates']:
						bot.say("New update for " + name + ": " + update, '#ggn-degenerates')
			for 
			sleep(300)
	targs = (bot,)
	t = Thread(target=monitor, args=targs)
	t.start()
	
@module.commands('ksstatus')
def ksstatus(bot, trigger):
	f = open('ks_list', 'r', encoding='utf-8')
	tks = None
	for ks in f:
		[name, address] = split('\t', ks)
		name = name.strip()
		address = address.strip()
		if trigger.group(1).lower() in name.lower():
			tks = ks
			break
	f.close()
	if tks == None:
		return bot.say("Kickstarter project '" + trigger.group(1) + "' not found."
	ks_data = get_data(tks)
	response = name + ": " + ks_data['pledged'] + " of " + ks_data['goal'] + " goal by " + ks_data['backer_count'] + " backers. Project is " + ks_data['percent'] + " funded. " + address
	return bot.say(response)
	
@module.commands('addks')
def addks(bot, trigger):
	ks_data = add_ks(address)
	if ks_data == None:
		return bot.say("Please provide a valid Kickstarter address.")		
	return bot.say("The kickstarter '" + ks_data['name'] + "' has been added.")
	
@module.commands('remks')
def remks(bot, trigger):
	response = rem_ks(trigger.group(1))
	if response == None:
		return bot.say(trigger.group(1) + " not found. You must enter the EXACT name in order to delete.")
	return bot.say(response + "  successfully removed.")