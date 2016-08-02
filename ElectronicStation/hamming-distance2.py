# "The Hamming Distance" downloaded: Sun Jul 31 18:30:30 2016
from math import pow
def checkio(n, m):
    hams = 0
    for p in [pow(2, i) for i in range(20, -1, -1)]:
        n_bit = n >= p
        m_bit = m >= p
        n -= p * n_bit
        m -= p * m_bit
        hams += n_bit ^ m_bit
    return hams
        
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

