# Sophia - AI 
This is a chatbot made using the chatterbot module in python, it involves machine learning and is a basic artificial intellegence. It can easily be adjusted to include more data. 

-- Update --
This doesn't use machine learning or any fancy AI, it's a module installed when I was younger and I haven't updated it out of nostalgia. Instead consider this an out-of-date guide for the chatterbot module. 

## Content
* [Changing Sophia's Name](#change-the-name)
* [Custom Training data](#add-training-data)
* [Credit](#credit)
* [Social Media](#social-media)

## Change the Name
to change Sophia's name to something else just open up the `Sophia_Train.py` and then travel to the begining part where it says 
``` python
bot = ChatBot('Sophia')
bot.set_trainer(ListTrainer)
file_location = os.path.dirname(os.path.realpath(__file__))
```

and change the `bot = ChatBot('Sophia')` to `bot = ChatBot('YOURNAME')` 

## Add Training Data  
To add training data/change training data go into `Sophia-AI/Sophia_Training_Corpus/data/` and then:
1) to add a new language: 
```
- add a new directory and call it your language.
- Now go into `Sophia_Train.py` 
- under the set language declaration, inside the while loop you have to create a new if statement. 
- copy and paste the if statement below with the altered options
```
```python
if select_language.lower() == 'YOURLANGUAGE':  #<----- enter the name of your language
		data_location = file_location + '/Sophia_training_Corpus/data/YOURLANGUAGE/'  # <------ enter the name of your language dir
		print('Sophia: English Selected')
		languageSet = True
```
2) to add to an existing language: 
```
- you just go into the language you would like to change 
- and replace all of the " - - something" with " - - your input text" because this is the input sophia recieves 
- and replace all of the "  - Sophias response" with "  - whatever you want to respond with" save the file and then retrain the chatbot.
```



## Credit: 
All of the credit goes to [gunthercox](https://github.com/gunthercox) , without his python module none of this would be possible, read his chatterbot repository because that will go into detail about creating a custome language. 
Message me on social media if you are having difficulties: 

# Social Media
- [Linkden - Elijah Ahmad](https://www.linkedin.com/in/elijah-ahmad-658a2b199/)
- [FaceBook - Elijah Ahmad](https://www.facebook.com/elijah.ahmad.71)
- [Instagram - @ElijahAhmad__](https://www.instagram.com/ElijahAhmad__)
- [Snapchat - @Elijah.Ahmad](https://www.snapchat.com/add/elijah.ahmad)
