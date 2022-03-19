"""
    @script-author: Amandeep Singh Khanna and Theepan Chakravarthy. S
    @script-description: This script contains the module to ingest user-data 
    into their respective RDBMS tables.
    @script-version: 1
    @script-last-updated: 19-03-2022, Saturday
"""


# Import Statements:
import pandas as pd
from sqlalchemy import *
from datetime import datetime


class IngestUserData:
    def __init__(self, db_url, input_data, table_name):
        self.CURRENT_TIMESTAMP = datetime.now().strftime(format="%Y%m%d%H%M%S")
        self.DB_URL = db_url
        assert (
            isinstance(input_data) == pd.core.DataFrame
        ), "input_data must be a pandas DataFrame object."
        # TODO - Add the unit check to see if data for all columns exists.
        self.input_data = input_data
        self.TABLE_NAME = table_name

    def create_db_engine(self):
        try:
            self.db_engine = create_engine(url=self.DB_URL, echo=True)
        except Exception as e:
            self.db_engine = None

    def ingest_data(self):
        self.create_db_engine()
        if self.db_engine != None:
            self.input_data["INGESTION_TIMESTAMP"] = self.CURRENT_TIMESTAMP
            try:
                self.input_data.to_sql(
                    name=self.TABLE_NAME,
                    con=self.db_engine,
                    if_exists="append",
                    index=False,
                    chunksize=1000,
                )
            except Exception as e:
                return f"DB table write operation failed with the error - {e} at {self.CURRENT_TIMESTAMP}"
        else:
            return f"DB Ingestion Failed at {self.CURRENT_TIMESTAMP}"
