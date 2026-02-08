from sqlalchemy.orm import Session
from app.domain.repository.credit.base import SimulationRepositoryBase
from app.domain.models.credit import SimulationModel
from app.domain.entities.credit import Simulation


class SimulationRepository(SimulationRepositoryBase):
    def __init__(self, db: Session):
        self.db = db

    def save(self, simulation: Simulation) -> None:
        model = SimulationModel(
            id=simulation.id,
            amount=simulation.amount,
            annual_rate=simulation.annual_rate,
            months=simulation.months,
            created_at=simulation.created_at,
        )
        self.db.add(model)
        self.db.commit()

    def find_all(self) -> list[SimulationModel]:
        return self.db.query(SimulationModel).all()

    def find_by_id(self, simulation_id: str) -> SimulationModel:
        return (
            self.db.query(SimulationModel)
            .filter(SimulationModel.id == simulation_id)
            .first()
        )

    def update(self, model: SimulationModel) -> None:
        self.db.merge(model)
        self.db.commit()
