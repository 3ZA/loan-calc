from utils.exceptions import *

SALARY_GROWTH = 1.05
REPAYMENT_RATE = 0.09
REPAYMENT_THRESHOLD = 25000

def calculate_monthly_repayment(annual_salary: float) -> float:
    """
    params:
    :float annual_salary: yearly income before tax
    """
    if annual_salary < 0:
        raise LessThanZeroException(
        "Recevied {:10.2f} Negative salary is invalid".format(annual_salary)
        )
    if annual_salary <= REPAYMENT_THRESHOLD:
        return 0.00
    repayment = REPAYMENT_RATE * (annual_salary - REPAYMENT_THRESHOLD)/12
    return float('{0:,.2f}'.format(repayment))
