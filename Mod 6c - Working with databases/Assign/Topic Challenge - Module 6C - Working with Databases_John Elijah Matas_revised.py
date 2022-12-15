""" Topic Challenge - Module 6C - Working With Databases """

import sqlite3

print(sqlite3.__doc__)

class DBOperations():
    """ Class that creates a database file named database.sqlite 
        and inserts a data inside then prints the inserted data.  
    """

    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite")
        print ("Database opened successfully")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("""Create table if not exists samples
                            (id integer primary key autoincrement not null,
                            location text not null,
                            date text not null,
                            max_temp real not null,
                            min_temp real not null,
                            mean_temp real not null);""")
            print("Table created successfully.")
        except Exception as e:
            print("Error:", e)

    def insert_data(self, data):
        """ Inserts data into the database. """
        curseur = self.cur
        connection = self.conn
        location = "Winnipeg, MB"
        sql = """insert into samples(location, date, max_temp, 
                                         min_temp, mean_temp)
                     values(?,?,?,?,?)"""
        
        for key, value in data.items():
            max_temp = value['Max']
            min_temp = value['Min']
            mean_temp = value['Mean']
            data = (location, key, max_temp, min_temp, mean_temp)
            curseur.execute(sql, data)

        connection.commit()
        print("Added data successfully")

    def print_data(self):
        """ Print the inserted data from the database. """
        curseur = self.cur
        connection = self.conn
        records = curseur.execute("select * from samples")
        for row in records:
            print(row)

        curseur.close()
        connection.close()


weather = {"2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 7.1}, 
            "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5},
            "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}}

dbOperations = DBOperations()
dbOperations.insert_data(weather)
dbOperations.print_data()
