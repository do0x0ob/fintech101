import numpy as np
from scipy.optimize import fsolve

def npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod):
    n = np.arange(len(cashFlowVec))

    if cashFlowPeriod == compoundPeriod == 12:
        r_eff = rate
    elif cashFlowPeriod == compoundPeriod == 1:
        r_eff = rate / 12
    else:
        r_eff = (1 + rate / (12 / compoundPeriod)) - 1

    p_over_m = cashFlowPeriod / compoundPeriod
    df = (1 + r_eff) ** (n * p_over_m)

    print(f"Rate: {rate}, Effective Rate: {r_eff}, Discount Factor: {df}, Cash Flow: {cashFlowVec}")
    
    return np.sum(cashFlowVec / df)


def irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod):
    def equation(rate):
        return npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod)
    
    irr_solution = fsolve(equation, 0.0)[0]
    return irr_solution

def main_assert(input_file, output_file, answer1):
    with open(input_file, 'r', encoding='big5') as f_in, open(output_file, 'w', encoding='big5') as f_out, open(answer1, 'r', encoding='big5') as answer:
        answer_lines = answer.readlines()
        error_lines = []

        for index, line in enumerate(f_in):
            data = list(map(int, line.split()))

            cashFlowVec = data[:-2]
            cashFlowPeriod = data[-2]
            compoundPeriod = data[-1]

            irr = irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod)
            output_irr = f"{irr * 100:.4f}\n"
            f_out.write(output_irr)
            correct_irr = answer_lines[index].strip()

            if output_irr.strip() != correct_irr:
                error_lines.append(index + 1)

        if error_lines:
            print(f"Incorrect lines: {', '.join(map(str, error_lines))}")
        else:
            print("Pass")