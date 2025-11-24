from fastapi import FastAPI
from pydantic import BaseModel

# IMPORTS RELATIVOS dentro del paquete src
from .domain.entities import CustomerRiskProfile
from .domain.value_objects import Money
from .application.services import CreditScoreService
from .infrastructure.repositories import RiskRepository


app = FastAPI(title="CreditScore Engine - DDD + Clean")

class CreditRequest(BaseModel):
    customer_id: str
    income: float
    debt: float
    age: int

class CreditResponse(BaseModel):
    score: int
    risk_level: str
    approved: bool

service = CreditScoreService()
repository = RiskRepository()

@app.post("/score", response_model=CreditResponse)
def get_score(req: CreditRequest):
    profile = CustomerRiskProfile(
        customer_id=req.customer_id,
        income=Money(amount=req.income, currency="PEN"),
        debt=Money(amount=req.debt, currency="PEN"),
        age=req.age,
    )
    result = service.calculate_score(profile)
    repository.save_decision(result)
    return CreditResponse(**result)
