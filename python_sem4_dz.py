# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
n_numbers=set()
m_numbers=set()

for i in range(n):
    n_numbers.add(int(input("Введите элемент первого множества: ")))
print(n_numbers)

for i in range(m):
    m_numbers.add(int(input("Введите элемент второго множества: ")))
print(m_numbers)

q_set=n_numbers.intersection(m_numbers)
print(sorted(q_set))


