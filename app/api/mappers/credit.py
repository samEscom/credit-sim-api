from typing import List

from app.domain.service.credit.amortization import AmortizationRow
from app.api.schemas.response import AmortizationRowResponse


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
