import uuid

from app.domain.service.credit.amortization import AmortizationService
from app.application.ports.risk_audit import RiskAuditPort
from app.domain.repository.credit.simulation import SimulationRepositoryBase
from app.domain.entities.credit import Simulation
from datetime import datetime


class SimulateCreditUseCase:
    def __init__(
        self,
        simulation_repository: SimulationRepositoryBase,
        risk_audit_port: RiskAuditPort | None = None,
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

        if self.risk_audit:
            # Pass the callback to be executed after audit completes
            self.risk_audit.execute(simulation_id, on_complete=self.update_risk_score)

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

    def find_all(self):
        return self.simulation_repository.find_all()

    def update_risk_score(self, simulation_id: str, risk_score: str):
        simulation = self.simulation_repository.find_by_id(simulation_id)
        if simulation:
            simulation.risk_score = risk_score
            simulation.updated_at = datetime.now()
            self.simulation_repository.update(simulation)
