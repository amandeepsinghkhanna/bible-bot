###################################PraiseBeToGod##############################################
The initial commit of the bot-engine made on 30-03-2022
Rasa open source is being used here to build the chatbot

The stories.yml needs more work.

Steps to setup Rasa-opensource
Visit https://rasa.com/docs/rasa/installation/ for more details

1. conda create -n "env_name" python=3.8
# Python 3.8 is being used as latest version had some bugs

2. conda activate env_name

3. Run pip3 install -U --user pip && pip3 install rasa

4. once rasa is installed

5. go to project directory and run rasa train to train the nlu

6. then run rasa shell to open a interactive session
