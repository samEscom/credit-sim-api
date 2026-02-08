from abc import ABC, abstractmethod
from app.domain.entities.credit import Simulation
from app.domain.models.credit import SimulationModel


class SimulationRepositoryBase(ABC):
    @abstractmethod
    def save(self, simulation: Simulation) -> None:
        pass

    @abstractmethod
    def find_all(self) -> list[SimulationModel]:
        pass

    @abstractmethod
    def find_by_id(self, simulation_id: str) -> SimulationModel:
        pass

    @abstractmethod
    def update(self, model: SimulationModel) -> None:
        pass
