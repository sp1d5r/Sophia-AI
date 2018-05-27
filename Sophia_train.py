from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import os 

bot = ChatBot('Sophia')
bot.set_trainer(ListTrainer)
file_location = os.path.dirname(os.path.realpath(__file__))

languageSet = False 
while languageSet == False :
	select_language = input('Sophia: Please Select Your Language.')
	if select_language.lower() == 'english':
		data_location = file_location + '/Sophia_training_Corpus/data/english/'
		print('Sophia: English Selected')
		languageSet = True

	if select_language.lower() == 'bangla':
		data_location = file_location + '/Sophia_training_Corpus/data/bangla/'
		print('Sophia: Bangla Selected')
		languageSet = True

	if select_language.lower() == 'chinese':
		data_location = file_location + '/Sophia_training_Corpus/data/chinese/'
		print('Sophia: Chinese Selected')
		languageSet = True

	if select_language.lower() == 'french':
		data_location = file_location + '/Sophia_training_Corpus/data/french/'
		print('Sophia: French Selected')
		languageSet = True

	if select_language.lower() == 'german':
		data_location = file_location + '/Sophia_training_Corpus/data/german/'
		print('Sophia: German Selected')
		languageSet = True

	if select_language.lower() == 'hebrew':
		data_location = file_location + '/Sophia_training_Corpus/data/hebrew/'
		print('Sophia: Hebrew Selected')
		languageSet = True

	if select_language.lower() == 'hindi':
		data_location = file_location + '/Sophia_training_Corpus/data/hindi/'
		print('Sophia: Hindi Selected')
		languageSet = True

	if select_language.lower() == 'indonesia':
		data_location = file_location + '/Sophia_training_Corpus/data/indonesia/'
		print('Sophia: Indonesian Selected')
		languageSet = True

	if select_language.lower() == 'italian':
		data_location = file_location + '/Sophia_training_Corpus/data/italian/'
		print('Sophia: italian Selected')
		languageSet = True

	if select_language.lower() == 'marathi':
		data_location = file_location + '/Sophia_training_Corpus/data/marathi/'
		print('Sophia: Marathi Selected')
		languageSet = True

	if select_language.lower() == 'odia':
		data_location = file_location + '/Sophia_training_Corpus/data/odia/'
		print('Sophia: Odia Selected')
		languageSet = True

	if select_language.lower() == 'portuguese':
		data_location = file_location + '/Sophia_training_Corpus/data/portuguese/'
		print('Sophia: portuguese Selected')
		languageSet = True

	if select_language.lower() == 'russian':
		data_location = file_location + '/Sophia_training_Corpus/data/Russian/'
		print('Sophia: Russian Selected')
		languageSet = True

	if select_language.lower() == 'spanish':
		data_location = file_location + '/Sophia_training_Corpus/data/spanish/'
		print('Sophia: Spanish Selected')
		languageSet = True

	if select_language.lower() == 'swedish':
		data_location = file_location + '/Sophia_training_Corpus/data/swedish/'
		print('Sophia: Swedish Selected')
		languageSet = True

	if select_language.lower() == 'traditional chinese':
		data_location = file_location + '/Sophia_training_Corpus/data/tchinese/'
		print('Sophia: Traditional Chinese Selected')
		languageSet = True

	if select_language.lower() == 'thai':
		data_location = file_location + '/Sophia_training_Corpus/data/thai/'
		print('Sophia: Thai Selected')
		languageSet = True




for files in os.listdir(data_location):
	data = open(data_location + files , 'r').readlines()
	bot.train(data)


while True:
	message = input('Sp1d5r: ')
	if message.strip().lower() != 'bye':
		reply = bot.get_response(message)
		print('Sophia: ', reply)
	if message.strip().lower() == 'bye':
		print('Sophia: Bye')
		break