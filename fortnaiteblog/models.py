from django.db import models

# Create your models here.
CATEGORY = (('business','ビジネス') , ('life','生活') , ('other','その他'))

class BlogModel(models.Model) :
    title    = models.CharField( max_length=50)
    images1  = models.ImageField(upload_to='')
    images2   = models.ImageField(upload_to='',blank = True ,null = True)
    images3   = models.ImageField(upload_to='',blank = True ,null = True)
    images4   = models.ImageField(upload_to='',blank = True ,null = True)
    images5   = models.ImageField(upload_to='',blank = True ,null = True)
    headline  = models.TextField()
    
    content = models.FileField(upload_to='',verbose_name='添付ファイル')
    
    postdate = models.DateField( auto_now_add=True)
    category = models.CharField(max_length = 50 ,choices =CATEGORY)
    

    
    def __str__(self):
        return self.title
