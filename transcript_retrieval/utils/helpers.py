import pandas as pd
from .constants import KEYWORD_COL_PREFIX, QUESTION_COL_PREFIX

def extract_question_query(columns_name):
    return [value[len(QUESTION_COL_PREFIX):] for value in columns_name if value.startswith(QUESTION_COL_PREFIX)]


def extract_keyword_query(columns_name):
    return [value[len(KEYWORD_COL_PREFIX):] for value in columns_name if value.startswith(KEYWORD_COL_PREFIX)]

def extract_query_from_df(df):
    columns_name = df.columns
    query_dict = {
        "keyword": extract_keyword_query(columns_name),
        "question": extract_question_query(columns_name),
    }
    
    return query_dict