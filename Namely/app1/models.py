from django.db import models

# Create your models here.


# classchoices = (
#     ('LKG','LKG'),
#      ('UKG','UKG'),
#      ('NURSERY','NURSERY'),
#     ('ONE','ONE'),
#     ('TOW', 'TWO'),
#     ('THREE','THREE'),
#     ('FOUR','FOUR'),
#     ('FIVE','FIVE'),
#      ('SIX','SIX'),
#       ('SEVEN','SEVEN'),
#        ('EIGHT','EIGHT'),
#        ('NINE','NINE'),
#        ('TEN','TEN'),
#        ('ELEVEN','ELEVEN'),
#         ('TWELEVE','TWELEVE'),
# ) 
    
class student(models.Model):
    name=models.CharField( max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    clas=models.CharField(max_length=10)
    role_number=models.IntegerField( )
    email=models.EmailField()
    
    def __str__(self):
        return self.name