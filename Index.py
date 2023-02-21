from numpy.random import default_rng
rng = default_rng()

def CPF (num): 
    
    num = str(num)
    returnCpfFirst = num[:9]
    countFirst=10
    valueFirst = 0

    for i  in returnCpfFirst : 
        valueFirst += int(i)*countFirst
        countFirst -= 1

    numbersFirst = (valueFirst * 10)  % 11
    
    numbersFirst = numbersFirst  if numbersFirst  <= 9 else   0 
    
    returnCpfSecond= num[:9] + str(numbersFirst)
    countSecond=11
    valueSecond = 0

    for i in returnCpfSecond : 
        valueSecond += int(i) * countSecond
        countSecond -=1

    numbersSecond = (valueSecond * 10) %11
    numbersSecond = numbersSecond if numbersSecond <=9 else 0
  
    Cpf = returnCpfSecond + str(numbersSecond)
    CpfiSformat = f'{Cpf[:3]}.{Cpf[3:6]}.{Cpf[6:9]}-{Cpf[9:]}'

    return CpfiSformat

print(CPF(rng.integers(1000000000)))