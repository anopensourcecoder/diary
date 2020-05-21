"""Main module."""

import datetime
from datetime import date, timedelta
import os.path
import sys
from diary.db import DB
from diary.diaryitem import DiaryItem
from diary.humandate import HumanDate


# Diary App
class Diary():
    db_type="sqlite"
    db_name = "diary.db"
    appdir=os.path.dirname(__file__)
    homedir = os.path.expanduser("~")
    date_slug_format_str = '%Y-%m-%d'
    datetime_slug_format_str = '%Y-%m-%d 00:00:00'

    def __init__(self):
        self.db = DB(self.homedir,self.db_name)
        self.go_date=self.get_date()

    def __del__(self):
        if self.db is not None:
            self.db.close()


    def get_date(self):
        godate_str = self.db.get_option("go_date_str")
        try:
            go_date_obj = datetime.datetime.strptime(godate_str, self.datetime_slug_format_str)
        except:
            go_date_obj= datetime.datetime.now().replace(hour=00, minute=00, second=00,microsecond=0)
        #print(type(self.go_date))
        #2020-05-19 08:34:36.300832
        #print("go_date_obj=", go_date_obj)
        #go_date_obj= 2020-05-16 00:00:00

        self.go_date = go_date_obj;

        return  self.go_date

    def set_day(self, days):

        godate_str = self.db.get_option("go_date_str")
        try:
            current_go_date_obj = datetime.datetime.strptime(godate_str, self.datetime_slug_format_str)
        except:
            current_go_date_obj = datetime.datetime.now().replace(hour=00, minute=00, second=00,microsecond=0)

        new_go_date_obj = current_go_date_obj +  timedelta(days=int(days))
        new_go_date_str = new_go_date_obj.strftime(self.datetime_slug_format_str)
        # print( go_date_str )
        self.db.save_option("go_date_str", new_go_date_str)

        return self.get_date()




    def set_date(self,diary_date_str):

        try:
            go_date_obj = datetime.datetime.strptime(diary_date_str, self.date_slug_format_str)
            go_date_str = go_date_obj.strftime(self.datetime_slug_format_str)
        except:
            go_date_obj = datetime.datetime.now().replace(hour=00, minute=00, second=00,microsecond=0)
            go_date_str = go_date_obj.strftime(self.datetime_slug_format_str)
        #print( go_date_str )
        self.db.save_option("go_date_str", go_date_str)

        return self.get_date()


        #self.go_date.strptime(diary_date_str, self.date_slug_format_str)
        #try:
        #    diary_date_obj = datetime.datetime.strptime(diary_date_str, self.date_slug_format_str)
        #except:
        #    diary_date_obj = date.today()

        #self.go_date = diary_date_obj

        #self.get_date()

    def go_first_diary(self):
        """ set the date to first diary date."""
        first_diary_date_obj = self.db.get_first_item_date_obj()
        if first_diary_date_obj is not None:
            go_date_str = first_diary_date_obj.strftime(self.datetime_slug_format_str)
            self.db.save_option("go_date_str", go_date_str)
            self.get_date()

    def go_last_diary(self):
        """ set the date to last diary date."""
        last_diary_date_obj = self.db.get_last_item_date_obj()
        if last_diary_date_obj is not None:
            go_date_str = last_diary_date_obj.strftime(self.datetime_slug_format_str)
            self.db.save_option("go_date_str", go_date_str)
            self.get_date()

    def get_diary(self):

        diary_item=DiaryItem(self.db,self.go_date)
        return  diary_item


    def get_diary_content(self):

        diary_item=DiaryItem(self.db,self.go_date)
        return  diary_item.get_item_content()


    def add_diary(self,content):

        diary_item=DiaryItem(self.db,self.go_date)
        diary_item.set_diary_item_content(content)
        diary_item.save_diary_item()




    def __repr__(self):
        return {
            'appdir': self.appdir,
            'homedir': self.homedir,
            'db_name': self.db_name,
            'go_date': self.go_date,
            'db': self.db,
        }

    def __str__(self):
        print( "str" )






