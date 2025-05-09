import psycopg2

class SQLQuery:
    def __init__(self, table):
        self.table = table
        self.columns = '*'
        self.conditions = []
        self.group_by = []
        self.order_by = []
        self.values = None  
        self.query_type = 'SELECT' 

    #methode select
    
    def methode_select(self, columns):
        self.query_type = 'SELECT'
        self.columns = ', '.join(columns)
        return self
        
    #methode insert
    def methode_insert(self, columns, values):
        if len(columns) != len(values):
            raise ValueError("nombre de collonne non correspondants")
        
        self.query_type = 'INSERT'
        self.columns = ', '.join(columns)
        self.values = values
        return self

    #methode delete 
    def methode_delete(self, columns):
        self.query_type = 'DELETE'
        self.columns = ', '.join(columns)
        return self

    #condition where
    def methode_where(self, condition):
        self.conditions.append(condition)
        return self

    #clause group by
    def methode_group_by(self, columns):
        self.group_by.extend(columns)
        return self

    #clause order by
    def methode_order_by(self, columns):
        self.order_by.extend(columns)
        return self

    #implementation des requettes
    def build_query(self):
        if self.query_type == 'SELECT':
            query = f"SELECT {self.columns} FROM {self.table}"
            if self.conditions:
                query += f" WHERE {' AND '.join(self.conditions)}"
            if self.group_by:
                query += f" GROUP BY {', '.join(self.group_by)}"
            if self.order_by:
                query += f" ORDER BY {', '.join(self.order_by)}"
            return query + ";"
        
        elif self.query_type == 'INSERT':
            if self.values is None:
                raise ValueError("Aucune valeur spécifiée pour l'insertion")
            
            formatted_values = ", ".join([f"'{value}'" for value in self.values])
            return f"INSERT INTO {self.table} ({self.columns}) VALUES ({formatted_values});"
            
        elif self.query_type == 'DELETE':
            query = f" DELETE FROM {self.table}"
            if self.conditions:
                query += f"WHERE {' '.join(self.condition)}"
            return query + ";"

        else:
            raise ValueError("Type de requête non pris en charge")
            
#implementation du builder
class SQLQueryFactory:
    @staticmethod
    def create_query(table):
        return SQLQuery(table)

#execution des 
def executer_requete(query, conn_params, is_select=True):
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        cursor.execute(query)
        
        if is_select:
            resultats = cursor.fetchall()
        else:
            conn.commit() 

        cursor.close()
        conn.close()

        return resultats if is_select else None

    except Exception as e:
        print("Erreur :", e)
        return None

# Exécution principale
if __name__ == "__main__":
    conn_params = {
        'dbname': 'Agenda',
        'user': 'postgres',
        'password': '0000',
        'host': 'localhost',
        'port': 5432
    }

    insert_query = (SQLQueryFactory.create_query('gps_data')
                    .methode_+insert(['latitude', 'longitude'], [45.678, -73.456])
                    .build_query())

    print("Requête générée pour INSERT :", insert_query)
    executer_requete(insert_query, conn_params, is_select=False)

    select_query = (SQLQueryFactory.create_query('gps_data')
                    .methode_select(['latitude', 'longitude'])
                    .methode_where("latitude > 30")
                    .methode_group_by(['latitude', 'longitude'])
                    .methode_order_by(['latitude'])
                    .build_query())

    print("Requête générée pour SELECT :", select_query)
    resultats = executer_requete(select_query, conn_params, is_select=True)

    if resultats:
        for ligne in resultats:
            print(ligne)
