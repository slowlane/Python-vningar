import math
import statistics

# Faktorial
def beräkna_faktorial(n):
    if n < 0:
        return "Ingen faktorial för negativa tal!"
    return math.factorial(n)

# Primtal
def är_primtal(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Fibonacci
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[:n]

# Statistik
def statistik_värden(betyg):
    medelvärde = statistics.mean(betyg)
    median = statistics.median(betyg)
    std_avvikelse = statistics.stdev(betyg)
    return {
        'Genomsnitt': medelvärde,
        'Median': median,
        'Standardavvikelse': std_avvikelse
    }


betyg = [85, 90, 78, 92, 88]
print("Faktorial av 5:", beräkna_faktorial(5))
print("Är 7 ett primtal?:", är_primtal(7))
print("Fibonacci-sekvens för 10 tal:", fibonacci(10))
print("Statistiska värden:", statistik_värden(betyg))
