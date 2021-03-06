"""
statistic.py

created by dromakin as 12.05.2021
Project app
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__status__ = 'Development'
__version__ = '20210512'

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Statistic])
def read_statistics(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve statistics.
    """
    if crud.user.is_superuser(current_user):
        statistics = crud.statistic.get_multi_statistics(db, skip=skip, limit=limit)
    else:
        statistics = crud.statistic.get_multi_by_customer(
            db=db, customer_id=current_user.id, skip=skip, limit=limit
        )
    return statistics


@router.post("/", response_model=schemas.Statistic)
def create_statistic(
    *,
    db: Session = Depends(deps.get_db),
    statistic_in: schemas.StatisticCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new statistic.
    """
    item = crud.statistic.create_with_customer(
        db=db, obj_in=statistic_in, customer_id=current_user.id
    )
    return item


@router.put("/{id}", response_model=schemas.Statistic)
def update_statistic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    statistic_in: schemas.StatisticUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an statistic.
    """
    statistic = crud.statistic.get(db=db, id=id)
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.customer_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    statistic = crud.statistic.update(db=db, db_obj=statistic, obj_in=statistic_in)
    return statistic


@router.get("/{id}", response_model=schemas.Statistic)
def read_statistic_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get statistic by ID.
    """
    statistic = crud.statistic.get(db=db, id=id)
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.customer_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return statistic


@router.post("/get_statistic_by_tid", response_model=List[schemas.Statistic])
def read_statistic_by_tid(
    *,
    db: Session = Depends(deps.get_db),
    statistic_model: schemas.statistic.StatisticAPI,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get statistic by tid.
    """
    tid = str(statistic_model.tid)
    skip = int(statistic_model.skip)
    limit = int(statistic_model.limit)

    if crud.user.is_superuser(current_user):
        statistic = crud.statistic.get_multi_by_tid(
            db=db, tid=tid, skip=skip, limit=limit
        )
    else:
        statistic = crud.statistic.get_multi_by_customer_tid(
            db=db, customer_id=current_user.id, tid=tid, skip=skip, limit=limit
        )
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.customer_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return statistic


@router.post("/get_statistic_by_target", response_model=List[schemas.Statistic])
def read_statistic_by_target(
    *,
    db: Session = Depends(deps.get_db),
    statistic_model: schemas.statistic.StatisticAPI,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get statistic by target.
    """
    target = str(statistic_model.target)
    skip = int(statistic_model.skip)
    limit = int(statistic_model.limit)

    if crud.user.is_superuser(current_user):
        statistic = crud.statistic.get_multi_by_target(
            db=db, target=target, skip=skip, limit=limit,
        )
    else:
        statistic = crud.statistic.get_multi_by_customer_target(
            db=db, customer_id=current_user.id, target=target, skip=skip, limit=limit,
        )
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.customer_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return statistic


@router.post("/get_statistic_by_cookie", response_model=List[schemas.Statistic])
def read_statistic_by_cookie(
    *,
    db: Session = Depends(deps.get_db),
    statistic_model: schemas.statistic.StatisticAPI,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get statistic by cookie.
    """
    cookie = str(statistic_model.cookie)
    skip = int(statistic_model.skip)
    limit = int(statistic_model.limit)

    if crud.user.is_superuser(current_user):
        statistic = crud.statistic.get_multi_by_cookie(
            db=db, cookie=cookie, skip=skip, limit=limit,
        )
    else:
        statistic = crud.statistic.get_multi_by_customer_cookie(
            db=db, customer_id=current_user.id, cookie=cookie, skip=skip, limit=limit,
        )
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.customer_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return statistic


@router.post("/get_statistic_by_platform", response_model=List[schemas.Statistic])
def read_statistic_by_platform(
    *,
    db: Session = Depends(deps.get_db),
    statistic_model: schemas.statistic.StatisticAPI,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get statistic by platform.
    """
    platform = str(statistic_model.platform)
    skip = int(statistic_model.skip)
    limit = int(statistic_model.limit)

    if crud.user.is_superuser(current_user):
        statistic = crud.statistic.get_multi_by_platform(
            db=db, customer_id=current_user.id, platform=platform, skip=skip, limit=limit,
        )
    else:
        statistic = crud.statistic.get_multi_by_customer_platform(
            db=db, customer_id=current_user.id, platform=platform, skip=skip, limit=limit,
        )
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.customer_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return statistic


@router.delete("/{id}", response_model=schemas.Statistic)
def delete_statistic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    statistic = crud.statistic.get(db=db, id=id)
    if not statistic:
        raise HTTPException(status_code=404, detail="Statistic not found")
    if not crud.user.is_superuser(current_user) and (statistic.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    statistic = crud.statistic.remove(db=db, id=id)
    return statistic

