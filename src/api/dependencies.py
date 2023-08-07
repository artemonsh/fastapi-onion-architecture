from typing import Annotated

from fastapi import Depends

from utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
