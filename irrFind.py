import numpy as np
from scipy.optimize import fsolve

# Calculate NPV
def npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod):
    n = np.arange(len(cashFlowVec))

    # Determine effective rate based on compounding period
    r_eff = rate if cashFlowPeriod == compoundPeriod == 12 else (1 + rate / (12 / compoundPeriod)) - 1

    # Compute the discount factor
    df = (1 + r_eff) ** (n * cashFlowPeriod / compoundPeriod)

    # Calculate NPV
    return np.sum(cashFlowVec / df)

# Calculate IRR
def irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod):
    return fsolve(lambda rate: npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod), 0.0)[0]