# Generated by Django 3.0.2 on 2020-01-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200128_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='ac_bonus',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ac_checkpenalty',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ac_properties',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ac_spellfailure',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ac_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ac_weight',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='acrobatics',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ammunition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='appraise',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='armor_class',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='armour_class_item',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='base_attack_bonus',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='base_speed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='bluff',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='burrow_speed',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='climb',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='climb_speed',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='cmb',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='cmd',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='copper',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='craft',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='craft_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='critical',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='damage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='diplomacy',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='disable_device',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='disguise',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='domain_or_speciality_magic',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='drag_or_push',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='escape_artist',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='feats',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='flat_footed_ac',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='fly',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='fly_speed',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='fortitude',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='gold',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='handle_animal',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='heal',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='heavy_load',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='hit_points',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='character_pics'),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='intimidate',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='item',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='item_wt',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='knowledge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='knowledge_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='languages',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='lift_off_ground',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='lift_over_head',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='light_load',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='linguistics',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='medium_load',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='perception',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='perform',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='perform_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='platinum',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='profession_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='reflex',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='ride',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='sense_motive',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='silver',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='sleight_of_hand',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='special_abilities',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='speed_with_armour',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='spell_resistance',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='spellcraft',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='spells_known',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='spells_per_day',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='stealth',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='strength_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='survival',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='swim',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='swim_speed',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='touch_ac',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='use_magic_device',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon_attack_bonus',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon_range',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='will',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom_mod',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='diety',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='eye_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='hair_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='homeland',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]