from pydantic import BaseModel, Field


class SimulateCreditRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Credit amount")
    annual_rate: float = Field(..., gt=0, description="Annual interest rate (%)")
    months: int = Field(..., gt=0, description="Credit term in months")
