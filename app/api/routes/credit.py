from fastapi import APIRouter, BackgroundTasks
from app.application.use_case.credit.simulate import SimulateCreditUseCase
from app.infrastructure.clients.audit import RiskAuditClient
from app.api.schemas.response import SimulateCreditResponse
from app.api.schemas.request import SimulateCreditRequest
from app.api.mappers.credit import map_amortization_rows

router = APIRouter(prefix="/credit", tags=["Credit"])


@router.post("/simulate", response_model=SimulateCreditResponse)
def simulate_credit(request: SimulateCreditRequest, background_tasks: BackgroundTasks):

    risk_audit = RiskAuditClient(background_tasks)
    use_case = SimulateCreditUseCase(risk_audit)

    result = use_case.execute(
        amount=request.amount,
        annual_rate=request.annual_rate,
        months=request.months,
    )

    response = map_amortization_rows(result)

    return SimulateCreditResponse(schedule=response)
