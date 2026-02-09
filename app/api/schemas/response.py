from pydantic import BaseModel
from typing import List
from datetime import datetime


class HealthResponse(BaseModel):
    status: str


class AmortizationRowResponse(BaseModel):
    month: int
    payment: float
    principal: float
    interest: float
    remaining_balance: float


class SimulateCreditResponse(BaseModel):
    simulation_id: str
    schedule: List[AmortizationRowResponse]


class SimulateResponse(BaseModel):
    id: str
    amount: float
    annual_rate: float
    months: int
    risk_score: str
    created_at: datetime
    updated_at: datetime
