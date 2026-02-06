import uuid

from app.domain.service.credit.amortization import AmortizationService
from app.application.ports.risk_audit import RiskAuditPort
from app.domain.repository.credit.simulation import SimulationRepositoryBase
from app.domain.entities.credit import Simulation
from datetime import datetime


class SimulateCreditUseCase:
    def __init__(
        self,
        risk_audit_port: RiskAuditPort,
        simulation_repository: SimulationRepositoryBase,
    ):
        self.risk_audit = risk_audit_port
        self.simulation_repository = simulation_repository

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

        simulation = Simulation(
            id=simulation_id,
            amount=amount,
            annual_rate=annual_rate,
            months=months,
            created_at=datetime.now(),
        )

        self.simulation_repository.save(simulation)

        return schedule
