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
        statistics = crud.statistic.get_multi(db, skip=skip, limit=limit)
    else:
        statistics = crud.statistic.get_multi_by_customer(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return statistics


@router.post("/", response_model=schemas.Statistic)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.StatisticCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new statistic.
    """
    item = crud.statistic.create_with_customer(db=db, obj_in=item_in, customer_id=current_user.id)
    return item


@router.put("/{id}", response_model=schemas.Statistic)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.StatisticUpdate,
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
    statistic = crud.statistic.update(db=db, db_obj=statistic, obj_in=item_in)
    return statistic


@router.get("/{id}", response_model=schemas.Statistic)
def read_item(
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


@router.delete("/{id}", response_model=schemas.Statistic)
def delete_item(
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
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (statistic.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    statistic = crud.statistic.remove(db=db, id=id)
    return statistic

