SalaryYear = float(input("Insira o salário anual:"))

if (SalaryYear <= 15000):
    taxPay = SalaryYear * 0.2
    print("Irá pagar uma taxa de 20 porcento, total de", taxPay)
    SalaryAfterTax = SalaryYear - taxPay
    print("O valor final do salário é de", SalaryAfterTax)

if (SalaryYear >= 15000 and SalaryYear <= 20000):
    taxPay = SalaryYear * 0.3
    print("Irá pagar uma taxa de 30 porcento, total de", taxPay)
    SalaryAfterTax = SalaryYear - taxPay
    print("O valor final do salário é de", SalaryAfterTax)

if (SalaryYear >= 20000 and SalaryYear <= 25000):
    taxPay = SalaryYear * 0.35
    print("Irá pagar uma taxa de 35 porcento, total de", taxPay)
    SalaryAfterTax = SalaryYear - taxPay
    print("O valor final do salário é de", SalaryAfterTax)

if (SalaryYear >= 25000):
    taxPay = SalaryYear * 0.3
    print("Irá pagar uma taxa de 40 porcento, total de", taxPay)
    SalaryAfterTax = SalaryYear - taxPay
    print("O valor final do salário é de", SalaryAfterTax)