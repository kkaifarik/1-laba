def move_disk(source, target):
    disk = source.pop()
    target.append(disk)

def hanoi_towers(n, source, target, auxiliary):
    if n == 1:
        move_disk(source, target)
    else:
        hanoi_towers(n-1, source, auxiliary, target)
        move_disk(source, target)
        hanoi_towers(n-1, auxiliary, target, source)

# Загружаем диски из файла в стек A
with open("input.txt", "r") as file:
    disks = list(map(int, file.readline().strip().split()))
stack_a = disks[::-1]

# Создаем пустые стеки B и C
stack_b = []
stack_c = []

# Вызываем рекурсивную функцию для перемещения дисков со стержня A на стержень C)
hanoi_towers(len(disks), stack_a, stack_c, stack_b)

# Выводим результат в файл
with open("output.txt", "w") as file:
    file.write(" ".join(map(str, stack_c[::-1])))