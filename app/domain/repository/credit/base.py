from abc import ABC, abstractmethod
from app.domain.entities.credit import Simulation


class SimulationRepositoryBase(ABC):
    @abstractmethod
    def save(self, simulation: Simulation) -> None:
        pass
