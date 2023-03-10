# install peewee
from peewee import *
from os import path
import sqlite3
from peewee import Model
from peewee import Database

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Swabir.db"))


# creating our tables
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Student(Model):
    student_name = CharField()
    student_id = CharField(unique=True)
    student_class = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)


class People(Model):
    name = CharField()
    phone = CharField()
    email = CharField()
    county = CharField()
    gender = CharField()
    religion = CharField()
    password = CharField()

    class Meta:
        database = db


People.create_table(fail_silently=True)
