from django.db import models

# Create your models here.
CATEGORY = (('Fortnite','フォートナイト') , ('programming','プログラミング') , ('other','その他'))

class BlogModel(models.Model) :
    title    = models.CharField( max_length=50)
    titleImages  = models.ImageField(upload_to='',blank = True ,null = True)

    headline        = models.TextField(blank = True ,null = True)
    articleContent  = models.TextField(blank = True ,null = True)


    images1   = models.ImageField(upload_to='',blank = True ,null = True)
    articleHeadline1 = models.TextField(blank = True ,null = True)    
    articleContent1 = models.TextField(blank = True ,null = True)


    images2   = models.ImageField(upload_to='',blank = True ,null = True)
    articleHeadline2 = models.TextField(blank = True ,null = True)    
    articleContent2 = models.TextField(blank = True ,null = True)
    
    images3   = models.ImageField(upload_to='',blank = True ,null = True)
    articleHeadline3 = models.TextField(blank = True ,null = True)    
    articleContent3 = models.TextField(blank = True ,null = True)

    images4   = models.ImageField(upload_to='',blank = True ,null = True)
    articleHeadline4 = models.TextField(blank = True ,null = True)    
    articleContent4 = models.TextField(blank = True ,null = True)

    images5   = models.ImageField(upload_to='',blank = True ,null = True)
    articleHeadline5 = models.TextField(blank = True ,null = True)    
    articleContent5 = models.TextField(blank = True ,null = True)
    
    endContents = models.TextField(blank = True ,null = True)

    postdate = models.DateField( auto_now_add=True)
    category = models.CharField(max_length = 50 ,choices =CATEGORY)
    

    
    def __str__(self):
        return self.title
