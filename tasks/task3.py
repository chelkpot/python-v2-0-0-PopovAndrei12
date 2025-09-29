# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    a, b = map(int, input("Введите 2 числа через пробел: ").split())

    total = a + b - 1

    harry_missed = total - a

    larry_missed = total - b

    print(harry_missed, larry_missed)    
 


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()