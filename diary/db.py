"""Main module."""

import os
import os.path
import sys

import sqlite3

#DatabaseSqlite
class DB():

    def __init__(self,homedir,db_name):



        #self.database_file=dbdir+"/"+db_name
        #self.database_file = "~/.config/diary/" + db_name

        #config_folder = dbdir+ "/.config/diary/"
        #try:
        #    os.mkdir("/home/user/.config/diary/")
            #os.mkdir(config_folder)
        #except:
        #    print("Error: Can not create " + config_folder + " directory.")
        #    exit()

        self.database_file = homedir + "/" + db_name

        #print("self.database_file=",self.database_file)

        try:
            self.conn = sqlite3.connect(self.database_file, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            self.cur = self.conn.cursor()
            # link https://www.sqlite.org/datatype3.html

            #create needed tables
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS items (item_id INTEGER PRIMARY KEY, item_content TEXT, item_datetime DATE)")
            self.conn.commit()
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS options (id INTEGER PRIMARY KEY, option_name TEXT, option_value TEXT )")
            self.conn.commit()
        except:
            print("Sqlite3 Connection Error")
            exit()

    #close db to free up resourse
    def close(self):
        if  self.conn is not None:
            self.conn.close()

    # ------------------------------- options table functions -------------------------------------
    def get_option(self, option_name):
        self.cur.execute("SELECT option_value FROM options WHERE option_name=?", (option_name,))
        row = self.cur.fetchone()
        # print('row-->',row)
        try:
            return row[0]
        except:
            return None


    def save_option(self, option_name, option_value):
        self.delete_option(option_name),

        self.cur.execute("INSERT INTO options VALUES (NULL,?,?)", (option_name, option_value))
        self.conn.commit()

    def delete_option(self, option_name):
        self.cur.execute("DELETE FROM options WHERE option_name=?", (option_name,))
        self.conn.commit()

    # ------------------------------- diary table functions -------------------------------------

    def get_item(self, diary_date_obj):
        self.cur.execute("SELECT item_id, item_content, item_datetime as '[timestamp]' FROM items WHERE item_datetime=?", (diary_date_obj,))
        row = self.cur.fetchone()
        try:
            return row
        except:
            return None

    def insert_item(self, item_date,item_content):
        self.cur.execute("INSERT INTO items VALUES (NULL,?,?)", (item_content,item_date))
        self.conn.commit()

    def update_item(self,item_id, item_content):
        #self.cur.execute(
        #    "UPDATE topic SET topic_type=?, topic_stars=?, topic_date_start=?, topic_question=?, topic_answer=? WHERE id=?",
        #    (topic_type, topic_stars, topic_date_start, topic_question, topic_answer, topic_id))

        self.cur.execute("UPDATE items SET item_content=? WHERE item_id=?", (item_content,item_id))
        self.conn.commit()


    def get_first_item_date_obj(self):
        query = "SELECT item_id, item_content, item_datetime as '[timestamp]' FROM items  ORDER BY item_datetime ASC LIMIT 1"
        try:
            self.cur.execute(query)
            row = self.cur.fetchone()
            return row[2]
        except:
            return None

    def get_last_item_date_obj(self):
        query = "SELECT item_id, item_content, item_datetime as '[timestamp]' FROM items  ORDER BY item_datetime DESC LIMIT 1"
        try:
            self.cur.execute(query)
            row = self.cur.fetchone()
            return row[2]
        except:
            return None
