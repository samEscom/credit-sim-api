from dataclasses import dataclass
from typing import List


@dataclass
class AmortizationRow:
    month: int
    payment: float
    principal: float
    interest: float
    remaining_balance: float


class AmortizationService:
    @staticmethod
    def simulate(
        amount: float,
        annual_rate: float,
        months: int,
    ) -> List[AmortizationRow]:

        monthly_rate = annual_rate / 12 / 100
        payment = amount / months
        balance = amount
        schedule = []

        for month in range(1, months + 1):
            interest = balance * monthly_rate
            principal = payment - interest
            balance -= principal

            schedule.append(
                AmortizationRow(
                    month=month,
                    payment=round(payment, 2),
                    principal=round(principal, 2),
                    interest=round(interest, 2),
                    remaining_balance=round(balance, 2),
                )
            )

        return schedule
