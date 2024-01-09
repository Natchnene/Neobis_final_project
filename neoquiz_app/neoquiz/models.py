from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images_articles/', null=True, blank=True)
    reading_time = models.PositiveIntegerField()
    content = models.TextField()
    category = models.ForeignKey(Category, models.SET_NULL, null=True)

    def __str__(self):
        return self.title

