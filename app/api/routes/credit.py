from fastapi import APIRouter, BackgroundTasks, Depends

from app.application.use_case.credit.simulate import SimulateCreditUseCase
from app.infrastructure.clients.audit import RiskAuditClient
from app.api.schemas.response import SimulateCreditResponse
from app.api.schemas.request import SimulateCreditRequest
from app.api.mappers.credit import map_amortization_rows
from sqlalchemy.orm import Session
from app.infrastructure.database.session import get_db
from app.domain.repository.credit.simulation import SimulationRepository


router = APIRouter(prefix="/credit", tags=["Credit"])


@router.post("/simulate", response_model=SimulateCreditResponse)
def simulate_credit(
    request: SimulateCreditRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):

    risk_audit = RiskAuditClient(background_tasks)
    repository = SimulationRepository(db)
    use_case = SimulateCreditUseCase(risk_audit, repository)

    result = use_case.execute(
        amount=request.amount,
        annual_rate=request.annual_rate,
        months=request.months,
    )

    response = map_amortization_rows(result)

    return SimulateCreditResponse(schedule=response)
