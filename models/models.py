# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    author_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    organisation = models.ForeignKey('Organisation', models.DO_NOTHING, blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Bookauthors(models.Model):
    book = models.OneToOneField('Books', models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, author_id) found, that is not supported. The first column is selected.
    author = models.ForeignKey(Authors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookauthors'
        unique_together = (('book', 'author'),)


class Bookkeywords(models.Model):
    book = models.OneToOneField('Books', models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, keyword_id) found, that is not supported. The first column is selected.
    keyword = models.ForeignKey('Keywords', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookkeywords'
        unique_together = (('book', 'keyword'),)


class Bookquotes(models.Model):
    quote_id = models.IntegerField(primary_key=True)
    ref_book = models.ForeignKey('Books', models.DO_NOTHING, blank=True, null=True)
    in_ref_book = models.ForeignKey('Books', models.DO_NOTHING, related_name='bookquotes_in_ref_book_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookquotes'


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.TextField()
    isbn = models.TextField(unique=True)
    url = models.TextField(unique=True)
    organisation = models.ForeignKey('Organisation', models.DO_NOTHING, blank=True, null=True)
    magazines = models.ForeignKey('Magazines', models.DO_NOTHING, blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    annotation = models.TextField()
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Keywords(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    keyword = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'keywords'


class Magazines(models.Model):
    magazine_id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'magazines'


class Organisation(models.Model):
    organisation_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organisation'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.TextField(unique=True)
    password = models.TextField()
    email = models.TextField(unique=True)
    confirmed_email = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Usersbooks(models.Model):
    book = models.OneToOneField(Books, models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(Users, models.DO_NOTHING)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usersbooks'
        unique_together = (('book', 'user'),)
