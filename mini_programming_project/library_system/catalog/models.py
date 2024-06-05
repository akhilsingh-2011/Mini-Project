from django.db import models

class Item(models.Model):
    Title = models.CharField(max_length=255)
    Release_date = models.DateField()
    Image = models.URLField()


    class Meta:
        abstract = True

class Book(Item):
    Author = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50)

class Magazine(Item):
    Publisher = models.CharField(max_length=100)
    Content_type = models.CharField(max_length=100, help_text="types of content featured (e.g., articles, interviews, reviews)")

class Movie(Item):
    Director = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in minutes")