from django.db import models

# Create your models here.

class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    role=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


# class userpolicies(models.Model):
#     created=models.DateTimeField(auto_now_add=True)
#     fullname=models.CharField(max_length=50)
#     age=models.IntegerField()
#     place=models.CharField(max_length=40)
#     gender=models.CharField(max_length = 50)
#     profession=models.CharField(max_length=100)
#     mobile_number = models.BigIntegerField()
#     select_type = models.CharField(max_length= 500)
    



# class user_policies(models.Model):
#     created=models.DateTimeField(auto_now_add=True)
#     fullname=models.CharField(max_length=50)
#     age=models.IntegerField()
#     place=models.CharField(max_length=40)
#     gender=models.CharField(max_length = 50)
#     profession=models.CharField(max_length=100)
#     mobile_number = models.BigIntegerField()
#     mail = models.EmailField()
#     select_type = models.CharField(max_length= 500)
#     grant_policy = models.CharField(max_length=20, null=True)


class user_policies_new(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=40)
    gender=models.CharField(max_length = 50)
    profession=models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()
    mail = models.EmailField()
    select_type = models.CharField(max_length= 500)
    grant_policy = models.CharField(max_length=20, null=True)

class feedback(models.Model):
    name=models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    mail = models.EmailField()
    msg = models.TextField() 