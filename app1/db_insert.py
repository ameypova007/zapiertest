import mysql.connector


class sql_conn:
    def fndbinsert(self,message,sender,receiver,description):
        try:
            self.messageimport mysql.connector


class sql_conn:
    def fndbinsert(self,message,sender,receiver,description):
        try:
            self.message = message
            self.sender = sender
            self.receiver = receiver
            self.description = description
            connection = mysql.connector.connect(host = 'localhost',database='kaleyra_sms',user='root',password='root')
            sql_insert = "insert into app1_message(message,sender,receiver,description) values(%s,%s,%s,%s)"
            record = (self.message,self.sender,self.receiver,self.description)

            cursor = connection.cursor()
            cursor.execute(sql_insert,record)
            connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(" failed to insert".format(err))
        finally:
            if connection.is_connected():
                connection.close()
