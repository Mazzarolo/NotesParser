import csv

for count in range(134):
    with open("notas\\produtos" + str(count + 1) + ".csv", "r", encoding="utf8") as arq:
        arq_csv = list(csv.reader(arq, delimiter=";"))
        for i, coluna in enumerate(arq_csv):
            if i == len(arq_csv) - 1:
                print(coluna[1])
            elif i > 0 and i != len(arq_csv) - 2:
                print(coluna[0] + " " + coluna[1] + " " + coluna[4])
    print()
