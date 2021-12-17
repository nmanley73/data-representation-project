import mysql.connector

class DogDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mano',
            database = 'datarepresentation'
        )
        print ("working")



    def create(self, dog):
        cursor = self.db.cursor()
        sql = "Insert into dogs (ID, Breed, Ownedby, Price) values (%s, %s, %s, %s)"
        values = [
            dog['ID'],
            dog['Breed'],
            dog['Ownedby'],
            dog['Price'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from dogs"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultasDict = self.converttoDict(result)
            returnArray.append(resultasDict)

        return returnArray

    def findbyID(self, ID):
        cursor = self.db.cursor()
        sql = "select * from dogs where ID = %s"
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.converttoDict(result)

    def update(self, dog):
        cursor = self.db.cursor()
        sql = "update dogs set Breed = %s, Ownedby = %s, Price = %s where ID = %s"
        values = [
            dog['Breed'],
            dog['Ownedby'],
            dog['Price'],
            dog['ID']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return dog

    def delete(self, ID):
        cursor = self.db.cursor()
        sql = "delete from dogs where ID = %s"
        values = [ID]
        cursor.execute(sql, values)
        return {}


    def converttoDict(self, result):
        colnames = ['ID', 'Breed', 'Ownedby', 'Price']
        dog = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                dog[colName] = value
        return dog

dogDao = DogDao()