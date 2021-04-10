import numpy as np


def common_PM(EAF, SIZE):
    return 3.2 * EAF * (SIZE ** 1.05)


def common_TM(PM):
    return 2.5 * (PM ** 0.38)


def calc_EAF(params: list):
    return np.prod(params)


def main():
    params = [
        1.0,  # ACAP
        1.0,  # AEXP
        1.0,  # PCAP
        1.0,  # LEXP
        1.0,  # CPLX
        1.0,  # RELY
        1.0,  # DATA
        1.0,  # TIME
        1.0,  # STOR
        1.0,  # VIRT
        1.0,  # TURN
        1.0,  # VEXP
        1.0,  # MODP
        1.0,  # TOOL
        1.0,  # SCED
    ]

    SIZE = 100000


if __name__ == '__main__':
    main()
