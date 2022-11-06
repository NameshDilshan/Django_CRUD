from django.db import models


# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_member"
