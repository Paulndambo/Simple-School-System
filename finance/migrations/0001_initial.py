# Generated by Django 4.1.2 on 2022-11-09 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('semester', models.CharField(choices=[('1', 'Semester One'), ('2', 'Semester Two'), ('3', 'Semester Three')], max_length=255)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='FeePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_method', models.CharField(choices=[('mpesa', 'M-pesa'), ('bank', 'Bank'), ('cash', 'Cash')], max_length=255)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.fee')),
            ],
        ),
    ]