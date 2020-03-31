# Generated by Django 3.0.4 on 2020-03-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Borrower',
            new_name='BookBorrower',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='contact_no',
            new_name='contact_nr',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='roll_no',
            new_name='nr',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='language',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
