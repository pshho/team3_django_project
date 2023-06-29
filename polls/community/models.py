from django.db import models

from django.contrib.auth.models import User
from django.db import models

from django.db import models

class Free_Board(models.Model):
    b_num = models.IntegerField()
    b_title = models.CharField(max_length=100)
    b_content = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    b_regdate = models.DateTimeField()
    b_modifydate = models.DateTimeField(null=True, blank=True)
    b_hit = models.IntegerField(default=0)
    b_recommend = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class Review_Board(models.Model):
    r_num = models.IntegerField()
    r_title = models.CharField(max_length=100)
    r_content = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    r_regdate = models.DateTimeField()
    r_modifydate = models.DateTimeField(null=True, blank=True)
    r_hit = models.IntegerField(default=0)
    r_recommend = models.IntegerField(default=0)

    def __str__(self):
        return self.username
