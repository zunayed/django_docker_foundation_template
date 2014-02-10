from django.db import models


class People(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    profile_pic = models.URLField(default='sample')

    def __unicode__(self):
        return ''.join([self.first_name, ' ', self.last_name])
