from fastapi import APIRouter, BackgroundTasks, Depends

from app.application.use_case.credit.simulate import SimulateCreditUseCase
from app.infrastructure.clients.audit import RiskAuditClient
from app.api.schemas.response import SimulateCreditResponse, SimulateResponse
from app.api.schemas.request import SimulateCreditRequest
from app.api.mappers.credit import map_amortization_rows, map_simulation_rows
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
    use_case = SimulateCreditUseCase(repository, risk_audit)

    result = use_case.execute(
        amount=request.amount,
        annual_rate=request.annual_rate,
        months=request.months,
    )

    response = map_amortization_rows(result)

    return SimulateCreditResponse(schedule=response)


@router.get("/simulate/{id}", response_model=SimulateResponse)
def simulate_credit_by_id(id: str, db: Session = Depends(get_db)):
    repository = SimulationRepository(db)
    use_case = SimulateCreditUseCase(repository)
    result = use_case.find_by_id(id)
    return result


@router.get("/simulate/history", response_model=list[SimulateResponse])
def simulate_credit_history(db: Session = Depends(get_db)):
    repository = SimulationRepository(db)

    use_case = SimulateCreditUseCase(repository)

    result = use_case.find_all()

    return map_simulation_rows(result)
