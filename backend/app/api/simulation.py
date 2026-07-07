from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user,
)

from app.models.user import User

from app.schemas.simulation import SimulationRequest

from app.services.simulation_service import SimulationService


router = APIRouter(

    prefix="/simulation",

    tags=["Simulation"],

)

service = SimulationService()


@router.post("/")
def simulate(

    request: SimulationRequest,

    current_user: User = Depends(get_current_user),

    db: Session = Depends(get_db),

):

    return service.simulate(

        db=db,

        user_id=current_user.id,

        scenario=request.scenario,

    )