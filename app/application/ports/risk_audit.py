from abc import ABC, abstractmethod


class RiskAuditPort(ABC):
    @abstractmethod
    def execute(self, simulation_id: str) -> str:
        pass
