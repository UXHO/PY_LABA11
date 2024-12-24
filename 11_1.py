def remove_elements(vectori, count):
    if isinstance(vectori, list) and isinstance(count, int) and count >= 0:
        if count <= len(vectori):
            return vectori[:-count]
        else:
            return []
    return vectori


file1 = open('vector.txt', 'r')
vectrs = [float(line.strip()) for line in file1]
file1.close()

cnt = int(input("Введите количество элементов для удаления: "))
new_vectors = remove_elements(vectrs, cnt)
print("Новый вектор:", new_vectors)

file2 = open('new_vector.txt', 'w')
for number in new_vectors:
    file2.write(f"{number}\n")
file2.close()
