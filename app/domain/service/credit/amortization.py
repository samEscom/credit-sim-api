from typing import List
from app.domain.entities.credit import AmortizationRow


class AmortizationService:
    @staticmethod
    def simulate(
        amount: float,
        annual_rate: float,
        months: int,
    ) -> List[AmortizationRow]:

        monthly_rate = annual_rate / 12 / 100

        # French System Formula: P = (A * i) / (1 - (1 + i)^-n)
        if monthly_rate > 0:
            payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
        else:
            payment = amount / months

        balance = amount
        total_principal_rounded = 0.0
        schedule = []

        for month in range(1, months + 1):
            interest = balance * monthly_rate
            principal = payment - interest

            # Rounding and accumulation
            rounded_interest = round(interest, 2)
            if month < months:
                rounded_principal = round(principal, 2)
                total_principal_rounded += rounded_principal
                balance -= rounded_principal
            else:
                # Last month: adjust principal to match exact total amount
                rounded_principal = round(amount - total_principal_rounded, 2)
                balance = 0.0

            rounded_payment = round(rounded_principal + rounded_interest, 2)

            schedule.append(
                AmortizationRow(
                    month=month,
                    payment=rounded_payment,
                    principal=rounded_principal,
                    interest=rounded_interest,
                    remaining_balance=max(0.0, round(balance, 2)),
                )
            )

        return schedule
