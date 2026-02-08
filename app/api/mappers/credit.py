from typing import List

from app.domain.service.credit.amortization import AmortizationRow
from app.api.schemas.response import AmortizationRowResponse, SimulateResponse
from app.domain.models.credit import SimulationModel


def map_amortization_rows(
    rows: List[AmortizationRow],
) -> List[AmortizationRowResponse]:
    return [
        AmortizationRowResponse(
            month=row.month,
            payment=row.payment,
            principal=row.principal,
            interest=row.interest,
            remaining_balance=row.remaining_balance,
        )
        for row in rows
    ]


def map_simulation_rows(rows: List[SimulationModel]) -> List[SimulateResponse]:
    return [
        SimulateResponse(
            id=row.id,
            amount=row.amount,
            annual_rate=row.annual_rate,
            months=row.months,
            risk_score=row.risk_score,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )
        for row in rows
    ]
