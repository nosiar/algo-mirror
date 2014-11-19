from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Problem(models.Model):
    keyword = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    submitted = models.IntegerField()
    accepted = models.IntegerField()
    source = models.ForeignKey(Source)
    category = models.ManyToManyField(Category)

    def ratio(self):
        return int(100 * self.accepted / self.submitted)

    def __str__(self):
        return "{0}".format(self.keyword)

class User(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=50)
    problem = models.ManyToManyField(Problem)

    def __str__(self):
        return "{0} {1}".format(self.uid, self.name)
