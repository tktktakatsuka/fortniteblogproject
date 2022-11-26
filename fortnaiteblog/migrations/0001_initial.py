# Generated by Django 4.1.3 on 2022-11-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('titleImages', models.ImageField(upload_to='')),
                ('headline', models.TextField()),
                ('images1', models.ImageField(blank=True, null=True, upload_to='')),
                ('articleHeadline1', models.TextField(blank=True, null=True)),
                ('articleContent1', models.TextField(blank=True, null=True)),
                ('images2', models.ImageField(blank=True, null=True, upload_to='')),
                ('articleHeadline2', models.TextField(blank=True, null=True)),
                ('articleContent2', models.TextField(blank=True, null=True)),
                ('images3', models.ImageField(blank=True, null=True, upload_to='')),
                ('articleHeadline3', models.TextField(blank=True, null=True)),
                ('articleContent3', models.TextField(blank=True, null=True)),
                ('images4', models.ImageField(blank=True, null=True, upload_to='')),
                ('articleHeadline4', models.TextField(blank=True, null=True)),
                ('articleContent4', models.TextField(blank=True, null=True)),
                ('images5', models.ImageField(blank=True, null=True, upload_to='')),
                ('articleHeadline5', models.TextField(blank=True, null=True)),
                ('articleContent5', models.TextField(blank=True, null=True)),
                ('postdate', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Fortnite', 'フォートナイト'), ('programming', 'プログラミング'), ('other', 'その他')], max_length=50)),
            ],
        ),
    ]
