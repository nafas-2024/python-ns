import sqlite3

class Back_End:
    def __init__(self):
        # create a database and handing in it .
        self.conn = sqlite3.connect("Back_end.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS commodities (id INTEGER PRIMARY KEY,commodity NVARCHAR, p_price INTEGER, s_price INTEGER, number INTEGER)""")
        self.conn.commit()
        
        
   
    def add_commodity(self, commo, p_price, s_price, num):
        """This is a function that takes commodity's name , 
    its purchase price , its selling price and the number of commodity.
    add them to the database.
        """
        self.cursor.execute("INSERT INTO commodities (commodity, p_price, s_price, number) VALUES (?, ?, ?, ?)",
            (commo,p_price,s_price,num,))
        self.conn.commit()
        
    def clear(self, id):
        """get commodity's id and delete it from database
        """
        self.cursor.execute("DELETE FROM commodities WHERE id=?", (id,))
        self.conn.commit()
        
    def edit(self,id, commo, p_price, s_price, number):
        """This is a function that takes  commodity's name , 
    its purchase price , its selling price and the number of commodity.
    update them from the database.
        """
        self.cursor.execute("UPDATE commodities SET commodity=? , p_price=?, s_price=?, number=? WHERE id=?", (commo, p_price, s_price, number, id))
        self.conn.commit()
    
    def search_c(self, commo, p_price, s_price, num):
        """This is a function that takes  commodity's name or 
    its purchase price or its selling price or the number of commodity and 
    select every filds with that info from database.
        """
        self.cursor.execute("SELECT * FROM commodities WHERE commodity=? OR p_price=? OR s_price=? OR number=?", (commo, p_price, s_price, num,))
        rows=self.cursor.fetchall()
        return rows