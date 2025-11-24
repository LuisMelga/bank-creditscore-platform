import sys
from pathlib import Path

# ================================
# Ajuste de ruta para encontrar src
# ================================
# __file__ = .../bank-creditscore-platform/app/creditscore_service/tests/test_main.py
ROOT = Path(__file__).resolve().parents[3]  # bank-creditscore-platform
APP_PATH = ROOT / "app" / "creditscore_service"

if str(APP_PATH) not in sys.path:
    sys.path.insert(0, str(APP_PATH))

# Ahora sí, podemos importar desde src
from src.application.services import CreditScoreService
from src.domain.entities import CustomerRiskProfile
from src.domain.value_objects import Money


def test_high_income_low_debt_gets_good_score():
    service = CreditScoreService()
    profile = CustomerRiskProfile(
        customer_id="123",
        income=Money(5000),
        debt=Money(500),
        age=30,
    )
    result = service.calculate_score(profile)
    assert result["approved"] is True
    assert result["risk_level"] in ("LOW", "MEDIUM")

def test_low_income_high_debt_is_rejected():
    service = CreditScoreService()
    profile = CustomerRiskProfile(
        customer_id="999",
        income=Money(1000),
        debt=Money(5000),
        age=22,
    )
    result = service.calculate_score(profile)
    assert result["approved"] is False
    assert result["risk_level"] == "HIGH"