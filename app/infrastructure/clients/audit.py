import random
import time

from fastapi import BackgroundTasks
from app.application.ports.risk_audit import RiskAuditPort

import uuid
import logging

logger = logging.getLogger(__name__)


class RiskAuditClient(RiskAuditPort):
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    def execute(self, simulation_id: str) -> str | None:
        try:
            audit_id = self.background_tasks.add_task(
                self._notify,
                simulation_id,
            )
            return audit_id
        except Exception:
            logger.error(
                "Risk audit failed (simulation_id=%s)",
                simulation_id,
            )
            return None

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

        return str(uuid.uuid4())
