# Generated by Django 4.2.7 on 2023-11-30 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('rarity', models.CharField(blank=True, choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare')], max_length=100, null=True)),
                ('hp', models.IntegerField(blank=True, null=True)),
                ('card_type', models.CharField(blank=True, choices=[('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon'), ('Dark', 'Dark'), ('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Steel', 'Steel'), ('Fairy', 'Fairy')], max_length=100, null=True)),
                ('attack', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('weakness', models.CharField(blank=True, max_length=250, null=True)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('evolution_stage', models.CharField(blank=True, max_length=250, null=True)),
                ('abilities', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('collection_date', models.DateField()),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.pokemoncard')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.trainer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]