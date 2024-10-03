import mysql.connector

# Mancano i parametri per la configurazionedel database
# andarli a prendere da colab
# problema dei secrets su github


def execute_query(query):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)

        # Se la query è un SELECT o SHOW TABLES, recupera i risultati
        if query.lower().startswith("select") or query.lower().startswith("show"):
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            # Se non è un SELECT o SHOW, esegui l'operazione
            conn.commit()
            print(f"{cursor.rowcount} righe affette.")

    except mysql.connector.Error as err:
        print(f"Errore: {err}")

    finally:
        cursor.close()
        conn.close()

def main():
    while True:
        query = input("Inserisci il comando SQL (o 'exit' per uscire): ")
        if query.lower() == 'exit':
            break
        execute_query(query)

if __name__ == "__main__":
    main()