from dataclasses import dataclass
from datetime import datetime


@dataclass
class Simulation:
    id: str
    amount: float
    annual_rate: float
    months: int
    created_at: datetime
