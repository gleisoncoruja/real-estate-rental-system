# Generated by Django 4.0.3 on 2022-04-13 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_alter_imovelfoto_options_alter_imovelfoto_imovel'),
        ('mensagem', '0005_alter_mensagens_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='imovel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.imovel'),
        ),
    ]
