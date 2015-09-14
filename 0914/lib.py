# Present Value of Future Cash Flow

def pv_f(fv, r, n):
    return fv/(1+r)**n

def fv_p(pv, r, n):
    return pv*(1+r)**n
