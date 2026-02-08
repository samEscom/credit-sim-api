import random
import time

from fastapi import BackgroundTasks
from app.application.ports.risk_audit import RiskAuditPort

import logging

logger = logging.getLogger(__name__)


class RiskAuditClient(RiskAuditPort):
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    def execute(self, simulation_id: str, on_complete=None) -> None:
        self.background_tasks.add_task(
            self._notify_and_callback,
            simulation_id,
            on_complete,
        )

    @staticmethod
    def _notify_and_callback(simulation_id: str, on_complete=None) -> None:
        try:
            result = RiskAuditClient._notify(simulation_id)
            if on_complete:
                on_complete(simulation_id, result)
        except Exception as e:
            logger.error(
                "Risk audit failed (simulation_id=%s): %s",
                simulation_id,
                str(e),
            )
            if on_complete:
                on_complete(simulation_id, "FAILED")

    @staticmethod
    def _notify(simulation_id: str) -> str:
        delay = random.uniform(1, 3)
        time.sleep(delay)

        if random.random() < 0.1:
            logger.error(
                "Risk audit failed (simulation_id=%s)",
                simulation_id,
            )
            raise Exception("Risk audit failed")

        logger.info(
            "Risk audit completed (simulation_id=%s)",
            simulation_id,
        )

        return "COMPLETED"
