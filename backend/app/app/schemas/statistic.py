"""
statistic.py

created by dromakin as 13.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210513'

from typing import Optional

from pydantic import BaseModel


# Shared properties
class StatisticBase(BaseModel):
    target: str
    value: str
    tid: str
    date: str
    cookie: str
    hashid: str
    ip: str
    platform: str
    webGL: str
    canvas: str
    deviceId: str


# Properties to receive on item creation
class StatisticCreate(StatisticBase):
    pass


# Properties to receive on item update
class StatisticUpdate(StatisticBase):
    pass


# Properties shared by models stored in DB
class StatisticInDBBase(StatisticBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Statistic(StatisticInDBBase):
    pass


# Properties properties stored in DB
class StatisticInDB(StatisticInDBBase):
    pass


