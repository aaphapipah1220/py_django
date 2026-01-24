# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClassType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'class_type'


class CustomersStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customers_status'


class DetailChannel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'detail_channel'


class Leads(models.Model):
    leads_in_period = models.DateField(blank=True, null=True)
    lead_source = models.ForeignKey('LeadsSource', models.DO_NOTHING, blank=True, null=True)
    detail_channel = models.ForeignKey(DetailChannel, models.DO_NOTHING, blank=True, null=True)
    parents_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number_of_parents = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255)
    student_aged = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    customer_status = models.ForeignKey(CustomersStatus, models.DO_NOTHING, blank=True, null=True)
    program = models.ForeignKey('Programs', models.DO_NOTHING, blank=True, null=True)
    student_advisor = models.ForeignKey('StudentAdvisor', models.DO_NOTHING, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'


class LeadsSource(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'leads_source'


class Level(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'level'


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'location'


class Module(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'module'


class Programs(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'programs'


class StudentAdvisor(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'student_advisor'


class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'teacher'

class Trial(models.Model):
    id = models.BigAutoField(primary_key=True)
    coding_experience = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    date_and_time = models.DateTimeField(blank=True, null=True)
    trial_location = models.ForeignKey('Location', models.DO_NOTHING, db_column='trial_location', blank=True, null=True)
    teacher_trial = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacher_trial', blank=True, null=True)
    level_trial = models.ForeignKey('Level', models.DO_NOTHING, db_column='level_trial', blank=True, null=True)
    program_trial = models.ForeignKey('Programs', models.DO_NOTHING, db_column='program_trial', blank=True, null=True)
    class_type = models.ForeignKey('ClassType', models.DO_NOTHING, db_column='class_type', blank=True, null=True)
    room = models.TextField(blank=True, null=True)
    lead = models.ForeignKey('Leads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trial'