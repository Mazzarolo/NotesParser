import csv
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="D4t@B3!z3d1",
    database="NotasFiscais"
)

mycursor = db.cursor()

for count in range(134):
    with open("notas\\produtos" + str(count + 1) + ".csv", "r", encoding="utf8") as arq:
        arq_csv = list(csv.reader(arq, delimiter=";"))
        est = arq_csv[len(arq_csv) - 1][1]
        try:
            mycursor.execute("insert into estabelecimento (nomeEst) values ('" + est + "')")
            db.commit()
        except:
            print("Estabelecimento já adicionado!")
        for i, coluna in enumerate(arq_csv):
            if i > 0 and i < len(arq_csv) - 2:
                try:
                    preco = coluna[4].replace(",", ".")
                    mycursor.execute("insert into produto values ('" + coluna[0] + "', '" + coluna[1] + "', '" + preco + "', '" + est + "')")
                    db.commit()
                except:
                    print("Produto já adicionado")
