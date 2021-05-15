"""
__init__.py

created by dromakin as 14.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210514'

import os
import pandas
import numpy as np
from typing import List

STATISTIC_DIR = "statistics_data_migration"
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_TO_FILE = os.path.join(APP_DIR, STATISTIC_DIR)


def get_users_by_name_files():
    files = {os.path.splitext(f)[0]: f for f in os.listdir(PATH_TO_FILE)
             if os.path.isfile(os.path.join(PATH_TO_FILE, f)) and f != "__init__.py"}

    return files


def get_db_data_by_file_name(filename: str) -> List[dict]:
    df = pandas.read_csv(os.path.join(PATH_TO_FILE, filename), delimiter=",")
    df = df.replace(r'^\s*$', '-', regex=True)
    df = df.replace(np.nan, '-', regex=True)
    df = df.astype(str)
    if 'time' in list(df.columns) and 'customer' in list(df.columns):
        df = df.drop(columns=['time', 'customer'])

    data = list()

    for i in range(df.shape[0]):
        data.append(dict(df.loc[0]))

    return data


# TESTING by dromakin
# def get_name_files():
#     files = [f for f in os.listdir(PATH_TO_FILE)
#              if os.path.isfile(os.path.join(PATH_TO_FILE, f)) and f != "__init__.py"]
#
#     for file in files:
#         df = pandas.read_csv(os.path.join(PATH_TO_FILE, file), delimiter=",")
#         df = df.replace(r'^\s*$', '-', regex=True)
#         df = df.replace(np.nan, '-', regex=True)
#         if 'time' in list(df.columns) and 'customer' in list(df.columns):
#             df = df.drop(columns=['time', 'customer'])
#
#         print(**dict(df.loc[0]))
#         print(list(df.loc[0].values))
#         break
#
# if __name__ == "__main__":
#     print(get_users_by_name_files())
#     print(get_db_data_by_file_name(os.path.join(PATH_TO_FILE, "test.csv")))
