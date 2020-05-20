"""Main module."""


import os.path
import sys
from diary import db

class DiaryItem():
    item_id=None
    item_date=""
    item_content=""
    def __init__(self,db,diary_date_obj):
        self.db = db
        self.item_date = diary_date_obj
        item = db.get_item(diary_date_obj)
        if item is not None:
            self.item_id = item[0]
            self.item_content = item[1]

    def get_item_content(self):
        return self.item_content

    def get_item_date(self):
        return self.item_date

    def set_diary_item_id(self,item_id ):
        self.item_id = item_id

    def set_diary_item_date(self,item_date ):
        self.item_date = item_date

    def set_diary_item_content(self,item_content ):
        self.item_content = item_content

    def save_diary_item(self ):
        if self.item_content == "" :
            return False
        if self.item_id == None:
            self.db.insert_item(self.item_date,self.item_content)
        else:
            self.db.update_item(self.item_id,self.item_content)





    def __repr__(self):
        return {'item_id': self.item_date, 'item_date': self.item_date, 'item_content': self.item_content}

    def __str__(self):
        return 'DiaryItem(item_id=' + str(self.item_id) + ', item_date=' + str( self.item_date) + ', item_content=' + str(self.item_content) + ')'






