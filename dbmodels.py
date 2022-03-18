'''
    @script-author: Amandeep Singh Khanna and Theepan Chakravarthy. S
    @script-description: This script contains the schema of all the db tables 
    that need to be created for this project to be functional.
    @script-version: 1
    @script-last-updated: 19-03-2022, Saturday
'''


# Import Statements:
from sqlalchemy import *


# TableName: userquestions
class UserQuestions:
    '''
        Schema for the table: userquestions
    '''
    __table_name__ = 'userquestions'
    question_id = Column(Integer, primary_key=True)
    interaction_timestamp = Column(DateTime)
    user_question = Column(String(1000))
    social_media_handle = Column(String(500))
    user_location = Column(String(200))
    classifier_used = Column(Boolean)
    classifier_response = Column(Integer)
    is_correct_response = Column(Boolean)
    daily_verse_subscriber = Column(Boolean)
    saw_menucard = Column(Boolean)
    menucard_selection = Column(Integer)

