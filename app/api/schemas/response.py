from pydantic import BaseModel
from typing import List


class HealthResponse(BaseModel):
    status: str


class AmortizationRowResponse(BaseModel):
    month: int
    payment: float
    principal: float
    interest: float
    remaining_balance: float


class SimulateCreditResponse(BaseModel):
    schedule: List[AmortizationRowResponse]
