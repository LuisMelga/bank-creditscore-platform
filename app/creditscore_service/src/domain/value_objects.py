from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "PEN"

    def ratio(self, other: "Money") -> float:
        """Devuelve el ratio entre dos montos, usado para calcular endeudamiento."""
        if other.amount == 0:
            return 0.0
        return self.amount / other.amount
