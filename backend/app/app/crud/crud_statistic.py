"""
crud_statistic.py

created by dromakin as 12.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210512'

from typing import Any, Dict, Optional, Union, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.statistic import Statistic
from app.schemas.statistic import StatisticCreate, StatisticUpdate


class CRUDStatistic(CRUDBase[Statistic, StatisticCreate, StatisticUpdate]):
    def get_multi_statistics(
            self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[List]:
        return (
            db.query(self.model)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def create_with_customer(
            self, db: Session, *, obj_in: StatisticCreate, customer_id: int
    ) -> Statistic:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, customer_id=customer_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_customer(
            self, db: Session, *, customer_id: int, skip: int = 0, limit: int = 100
    ) -> List[List]:
        return (
            db.query(self.model)
                .filter(Statistic.customer_id == customer_id)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def get_multi_by_tid(
            self, db: Session, *, tid: str, skip: int = 0, limit: int = 100
    ) -> List[List]:
        return (
            db.query(self.model)
                .filter(Statistic.tid == tid)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def get_multi_by_target(
            self, db: Session, *, target: str, skip: int = 0, limit: int = 100
    ) -> List[List]:
        return (
            db.query(self.model)
                .filter(Statistic.target == target)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def get_multi_by_cookie(
            self, db: Session, *, cookie: str, skip: int = 0, limit: int = 100
    ) -> List[List]:
        return (
            db.query(self.model)
                .filter(Statistic.cookie == cookie)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def get_multi_by_platform(
            self, db: Session, *, platform: str, skip: int = 0, limit: int = 100
    ) -> List[List]:
        return (
            db.query(self.model)
                .filter(Statistic.platform == platform)
                .offset(skip)
                .limit(limit)
                .all()
        )


statistic = CRUDStatistic(Statistic)
