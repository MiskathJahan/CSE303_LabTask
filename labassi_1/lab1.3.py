def compound_interest_2019_2_60_056(P, R, T):
    A = P * (pow((1 + R / 100), T))
    compound_interest = A - P
    return compound_interest


P = float(input("Enter the principle amount:"))
R = float(input("Enter interest rate:"))
T = float(input("Enter time:"))
c = compound_interest_2019_2_60_056(P, R, T)
print("Compound interest :{:.2f}".format(c))