import numpy
import pandas as pd

from calendar import monthrange
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils.exceptions import *

SALARY_GROWTH = 1.05
REPAYMENT_RATE = 0.09
LOWER_REPAYMENT_THRESHOLD = 25000
UPPER_REPAYMENT_THRESHOLD = 45000
RPI = 0.03
# interest charged on the loan above rpi depends on how much you earn
# over the LOWER_REPAYMENT_THRESHOLD. e.g. LOWER=25k, UPPER=45k a salary of 35k
# would have interest charges of rpi + 0.5 * VARIABLE_INTEREST
VARIABLE_INTEREST = 0.03
SALARY_GROWTH = RPI + 0.02 
DATE_FMT = "%d/%m/%Y"

def get_monthly_repayment(annual_salary: float) -> float:
    """
    params:
    :float annual_salary: Non negative float. Yearly income before tax.
    """
    if annual_salary < 0:
        raise LessThanZeroException(
        "Recevied {:10.2f} Negative salary is invalid".format(annual_salary)
        )
    if annual_salary <= REPAYMENT_THRESHOLD:
        return 0.00
    repayment = REPAYMENT_RATE * (annual_salary - REPAYMENT_THRESHOLD)/12
    return float('{0:,.2f}'.format(repayment))


def daily_interest(apr: float):
    """
    Calculates the day interest rate.

    :float apr: annual percentage rate is the interest rate for a whole year.
    """
    return apr/365

def monthly_interest(apr: float):
    """
    Calculates the month interest rate.
    
    :float apr: annual percentage rate is the interest rate for a whole year.
    """
    return apr/12

def simulate_loan(
        starting_balance: float,
        start_date: datetime.datetime,
        starting_salary: float
    ) -> list:
    """
    Simulates the repayment of student loan over 30 years

    :float balance: value of loan currently.
    :int start_month: month to begin simulation of repayments.
    """
    # starting calculations from the beginning of the month
    current_date = datetime.strptime(start_date, DATE_FMT)
    current_date.replace(day=1)
    end_date = current_date + relativedelta(years=30)

    # store the values inside a dataframe
    date_range = pd.date_rate(start=start_date, end=end_date, freq='M')
    results = pd.DataFrame(index=date_range)
    # create placeholders to be populated
    df['balance'], df['interest'], df['payment'] = np.empty((len(date_range), 3)).T
    
    # ininitialise variables for calculations
    current_balance = starting_balance
    current_salary = starting_salary
    current_interest_rate = salary_to_interest_rate(current_salary)
    current_monthly_repayment = get_monthly_repayment(current_salary)

    
    while current_date < end_date:
        if current_date.month == 1:
            current_salary *= 1 + SALARY_GROWTH
            current_interest_rate = salary_to_interest_rate(current_salary)
            current_monthly_repayment = get_monthly_repayment(current_salary)

        monthly_accrued_interest = get_monthly_interest_daily_accrual(
                balance=current_balance,
                day_interest_rate=current_interest_rate,
                date=current_date
        )
        current_balance += monthly_accrued_interest
        current_balance -= current_monthly_repayment
            current_date += relativedelta(months=1)
        df.loc[current_date][

    
def get_monthly_interest_daily_accrual(
    balance: float, day_interest_rate: float, date: datetime
) -> float:
    """
    Calcaultes the sum of daily interest accruals over a given month.
    This sum is used to compound the balance by adding the interest at the end
    of the month.

    :params:
    :float balance: balance at the start of the month.
    :float day_interest_rate: daily interest rate; 5% would be input as 0.05.
    :datetime.datetime date: provides the month/year to work out the number of
    days that interest is accrued over.
    """
    day_interest_amount = (1 + day_interest_rate) * balance
    # get the number of days that we need to accrue over from the date
    n_days = calendar.monthrange(date.year, date.month)[-1]
    return n_days * day_interest_amount

def salary_to_interest_rate(salary: float) -> float:
    """
    interest rate above rpi varies on a scale proportional when salary is
    between LOWER_REPAYMENT_THRESHOLD and UPPER_REPAYMENT_THRESHOLD
    
    :params:
    :float salary: salary for the year of calculation.
    :return float: interest rate as a decimal.
    """
    if salary <= LOWER_REPAYMENT_THRESHOLD:
        return RPI
    if salary >= UPPER_REPAYMENT_THRESHOLD:
        return RPI + VARIABLE_INTEREST
    return 1 + (salary - LOWER_REPAYMENT_THRESHOLD) / (
        UPPER_REPAYMENT_THRESHOLD-LOWER_REPAYMENT_THRESHOLD
        ) * VARIABLE_INTEREST






# TODO(): start the simulation from an arbitary date.
#def remaining_days_in_month()
#
#
#    n_days_in_start_month = calendar.monthrange(start_date.year, start_date.month)[-1]
#    end_date_of_start_month = datetime(
#        start_date.year, start_date.month, n_days_in_start_month
#    )
#    days_remaining = (end_date_of_start_month - start_date).days + 1










































<F4>








