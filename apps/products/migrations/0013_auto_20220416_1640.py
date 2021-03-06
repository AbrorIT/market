# Generated by Django 3.2.7 on 2022-04-16 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_alter_favoriteproduct_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='favoriteproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_product', to='products.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='favoriteproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorite_product', to=settings.AUTH_USER_MODEL),
        ),
    ]
