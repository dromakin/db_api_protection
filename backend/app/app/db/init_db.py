"""
init_db.py

created by dromakin as 03.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210503'

from sqlalchemy.orm import Session
from pydantic import EmailStr

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

from app.statistics_data_migration import get_users_by_name_files, get_db_data_by_file_name


# dromakin:
# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    if settings.STATISTIC is True:
        # Statistic create users
        users = get_users_by_name_files()
        for user in users.keys():
            new_user = schemas.UserCreate(
                email=EmailStr(str(user) + '@dev-api.com'),
                password=str(user),
                is_active=False,
                is_superuser=False,
            )
            user_ = crud.user.create(db, obj_in=new_user)  # noqa: F841

            filename = users.get(user)
            statistics_raws = get_db_data_by_file_name(filename)
            for raw in statistics_raws:
                new_statistic = schemas.StatisticCreate(**raw)
                statistic_ = crud.statistic.create_with_customer(  # noqa: F841
                    db, obj_in=new_statistic, customer_id=user_.id
                )
