from ..domain.entities import CustomerRiskProfile


class CreditScoreService:
    """
    Capa de aplicación: orquesta reglas de negocio del scoring.
    No sabe nada de HTTP, BD, cloud, etc. Solo domina el dominio.
    """

    def calculate_score(self, profile: CustomerRiskProfile) -> dict:
        ratio = profile.debt.ratio(profile.income)

        base_score = 800
        penalty_debt = ratio * 300
        penalty_age = 50 if profile.age < 25 else 0

        score = int(base_score - penalty_debt - penalty_age)
        score = max(300, min(score, 850))

        if score >= 750:
            risk = "LOW"
            approved = True
        elif score >= 650:
            risk = "MEDIUM"
            approved = True
        else:
            risk = "HIGH"
            approved = False

        return {
            "score": score,
            "risk_level": risk,
            "approved": approved,
        }
