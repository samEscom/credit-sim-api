from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class SimulationModel(Base):
    __tablename__ = "credit_simulation"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    annual_rate: Mapped[float] = mapped_column(Float, nullable=False)
    months: Mapped[int] = mapped_column(Integer, nullable=False)
    risk_score: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
