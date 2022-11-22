from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


    #def __str__(self) ->str:
        #return self.name


class Good(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class Make(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class Gif(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class Kok(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self) ->str:
        return self.name
        