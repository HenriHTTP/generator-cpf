from numpy.random import default_rng

rng = default_rng()


def create_cpf_valid(num) -> str:
    num = str(num)
    return_cpf_first = num[:9]
    count_first = 10
    value_first = 0

    for i in return_cpf_first:
        value_first += int(i) * count_first
        count_first -= 1

    numbers_first = (value_first * 10) % 11

    numbers_first = numbers_first if numbers_first <= 9 else 0

    return_cpf_second = num[:9] + str(numbers_first)
    count_second = 11
    value_second = 0

    for i in return_cpf_second:
        value_second += int(i) * count_second
        count_second -= 1

    numbers_second = (value_second * 10) % 11
    numbers_second = numbers_second if numbers_second <= 9 else 0

    cpf = return_cpf_second + str(numbers_second)
    cpf_sformat = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf_sformat


# test method 
cpf_test = create_cpf_valid(rng.integers(1000000000))
print(cpf_test)