"""
user.py

created by dromakin as 03.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210503'

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Statistic(Base):
    id = Column(Integer, primary_key=True, index=True)
    target = Column(String, index=True)
    value = Column(String)
    tid = Column(String, index=True)
    date = Column(String)
    # time = Column(DateTime, default=datetime.datetime.utcnow())
    time = Column(String)
    cookie = Column(String, index=True)
    hashid = Column(String)
    ip = Column(String, index=True)
    platform = Column(String)
    customer = relationship("User", back_populates="statistics")
    customer_id = Column(Integer, ForeignKey("user.id"))
    webGL = Column(String)
    canvas = Column(String)
    deviceId = Column(String)
