'''
    @script-author: Amandeep Singh Khanna and Theepan Chakravarthy. S
    @script-description: This script contains the module to ingest user-data 
    into their respective RDBMS tables.
    @script-version: 1
    @script-last-updated: 19-03-2022, Saturday
'''


# Import Statements:
from  datetime import datetime
from sqlalchemy import *
from dbmodels import UserQuestions


class IngestUserData:

    def __init__(self):
        self.current_timestamp = datetime.now().strftime(format="%Y%m%d%H%M%S")
