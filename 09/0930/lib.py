# Present Value of Future Cash Flow

def get_pv(fv, r, n):
    ### fv : future value
    ### r : interest rate
    ### n : number of periods
    return fv/(1+r)**n

def get_fv(pv, r, n):
    ### pv : present value
    ### r : interest rate
    ### n : number of periods
    return pv*(1+r)**n

def get_nfv(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow * (1+rate)**i
    return total

def get_npv(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1+rate)**i
    return total

def get_irr(cashflows, interations=100):
    rate = 1.0
    investment = cashflows[0]
    for i in range(1, interations+1):
        rate*= (1-get_npv(rate,cashflows)/investment)
    return rate
