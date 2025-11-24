from dataclasses import dataclass
from .value_objects import Money

@dataclass
class CustomerRiskProfile:
    customer_id: str
    income: Money
    debt: Money
    age: int
