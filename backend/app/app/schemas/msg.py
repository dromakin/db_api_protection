"""
msg.py

created by dromakin as 03.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210503'

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
