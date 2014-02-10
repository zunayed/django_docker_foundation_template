from django.db import models


class Post(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def createPost(self, fname, lname, title, content):
        '''assign values to post'''
        self.first_name = fname
        self.last_name = lname
        self.title = title
        self.content = content

    def __unicode__(self):
        return ''.join([self.first_name, ' - ', self.title])
