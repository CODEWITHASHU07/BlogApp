# Generated by Django 5.0.6 on 2024-06-02 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_blog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comment_content',
        ),
    ]
