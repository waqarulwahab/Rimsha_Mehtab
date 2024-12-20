# Generated by Django 5.1.1 on 2024-10-31 04:33

import app.models
import colorfield.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Rimsha Mehtab', max_length=255, null=True)),
                ('title', models.CharField(blank=True, default='Interior Designer', max_length=255, null=True)),
                ('birthday', models.DateField()),
                ('website', models.URLField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(default='+92 3368297079', max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('email', models.EmailField(default='rimshamehtab432@gmail.com', max_length=254)),
                ('freelance', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=50)),
                ('profile_image', models.ImageField(upload_to='about/')),
                ('bio', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AchievementsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='What we have achieved so far', max_length=255)),
                ('description', models.TextField(default='Crafting innovative spaces with precision and creativity, building structures that stand the test of time.')),
                ('clients', models.IntegerField(default=0)),
                ('projects', models.IntegerField(default=0)),
                ('hours_of_support', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('background_image_1', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
                ('background_image_1_opacity', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('background_image_2', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
                ('background_image_2_opacity', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('background_image_3', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
                ('background_image_3_opacity', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='clients/logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='experience_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon_image', models.ImageField(upload_to='service_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='skills/')),
                ('percentage', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThemeSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('default_color', colorfield.fields.ColorField(default='#212529', image_field=None, max_length=25, samples=None)),
                ('heading_color', colorfield.fields.ColorField(default='#37373f', image_field=None, max_length=25, samples=None)),
                ('accent_color', colorfield.fields.ColorField(default='#ce1212', image_field=None, max_length=25, samples=None)),
                ('surface_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('contrast_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('nav_color', colorfield.fields.ColorField(default='#7f7f90', image_field=None, max_length=25, samples=None)),
                ('nav_hover_color', colorfield.fields.ColorField(default='#ce1212', image_field=None, max_length=25, samples=None)),
                ('nav_mobile_background_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('nav_dropdown_background_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('nav_dropdown_color', colorfield.fields.ColorField(default='#7f7f90', image_field=None, max_length=25, samples=None)),
                ('nav_dropdown_hover_color', colorfield.fields.ColorField(default='#ce1212', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('project_url', models.URLField(blank=True, null=True)),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_date', models.DateField(blank=True, null=True)),
                ('detail_title', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_description', models.TextField(blank=True, null=True)),
                ('display_details', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='app.projectcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=app.models.project_image_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.project')),
            ],
        ),
    ]
