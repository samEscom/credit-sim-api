import uuid

from app.domain.service.credit.amortization import AmortizationService
from app.application.ports.risk_audit import RiskAuditPort


class SimulateCreditUseCase:
    def __init__(self, risk_audit_port: RiskAuditPort):
        self.risk_audit = risk_audit_port

    def execute(
        self,
        amount: float,
        annual_rate: float,
        months: int,
    ):
        simulation_id = str(uuid.uuid4())

        self.risk_audit.execute(simulation_id)

        schedule = AmortizationService.simulate(
            amount=amount,
            annual_rate=annual_rate,
            months=months,
        )

        # 2. TODO: persistencia

        return schedule
