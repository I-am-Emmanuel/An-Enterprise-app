# Generated by Django 4.1.3 on 2023-01-19 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_cartitem_cart_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set(),
        ),
    ]
