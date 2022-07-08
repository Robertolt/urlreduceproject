# Generated by Django 4.0.6 on 2022-07-06 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('origem', models.URLField(blank=True, max_length=512, null=True)),
                ('user_agente', models.CharField(blank=True, max_length=512, null=True)),
                ('host', models.CharField(blank=True, max_length=512, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('url_redirect', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='logs',
                                                   to='encurtador.urlredirect')),
            ],
        ),
    ]
