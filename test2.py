print()
print("Таблица умножения")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:>4}", end="")
    print()

print()
print("Квадраты чисел")
print("-----------------")

for i in range(100):
    print(f"|{i:^7}|{i * i:^7}|")
    print("-----------------")

print()
print("Километры в мили")
print("---------------")
print("| км/ч | мил/ч |")
print("---------------")
for i in range(60, 131, 10):
    print(f"|{i:^6}|{i * 0.6214:^7.1f}|")
    print("---------------")