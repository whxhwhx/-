from django.db import models


class user_info(models.Model):
    uname = models.CharField(max_length=20)
    uphone = models.CharField(max_length=11)
    face_image = models.ImageField(upload_to='face/')
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.uname.encode('utf-8')


class visitor_info(models.Model):
    # vname = models.CharField(max_length=10)
    vtemp = models.FloatField()
    vtime = models.DateTimeField()
    vuser = models.ForeignKey(user_info)

class temporary(models.Model):
    tname = models.CharField(max_length=20)
    tphone = models.CharField(max_length=11)
    temail = models.CharField(max_length=30)
    tkey = models.CharField(max_length=30)
    is_delete = models.BooleanField(default=False)

