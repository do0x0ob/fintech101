import numpy as np
from scipy.optimize import fsolve

# Calculate NPV
def npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod):
    n = np.arange(len(cashFlowVec))

    # Determine effective rate based on compounding period
    if cashFlowPeriod == compoundPeriod == 12:
        r_eff = rate
    elif cashFlowPeriod == compoundPeriod == 1:
        r_eff = rate / 12
    else:
        r_eff = (1 + rate / (12 / compoundPeriod)) - 1

    # Precompute the ratio of cashFlowPeriod and compoundPeriod
    p_over_m = cashFlowPeriod / compoundPeriod

    # Compute the discount factor
    df = (1 + r_eff) ** (n * p_over_m)

    # Calculate NPV
    return np.sum(cashFlowVec / df)

# Calculate IRR
def irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod):
    # Define the equation to solve (NPV = 0)
    def equation(rate):
        return npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod)
    
    # Use fsolve to calculate IRR, initial guess set to 0
    irr_solution = fsolve(equation, 0.0)[0]
    return irr_solution

# Main function to read input and write output
def main(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            data = list(map(int, line.split()))  # Read input data
            
            # Get Data
            cashFlowVec = data[:-2]
            cashFlowPeriod = data[-2]
            compoundPeriod = data[-1]

            irr = irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod)
            f_out.write(f"{irr * 100:.4f}\n")