import math

def baby_step_giant_step(alpha, beta, p):
    m = math.ceil(math.sqrt(p))
    exp_table = {(alpha ** i) % p: i for i in range(1, m + 1)}
    a_m_inv = pow(alpha, -m, p)
    gamma = beta
    for i in range(m + 1):
        if gamma in exp_table:
            return i * m + exp_table[gamma]
        else:
            gamma = (gamma * a_m_inv) % p