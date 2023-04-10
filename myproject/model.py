# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MonitorCnc(models.Model):
    stt = models.AutoField(db_column='STT', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey('MonitorMachine', models.DO_NOTHING, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    rfid = models.ForeignKey('MonitorWorker', models.DO_NOTHING, db_column='RFID', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('MonitorProduct', models.DO_NOTHING, blank=True, null=True)
    tool_numbers = models.ForeignKey('MonitorTool', models.DO_NOTHING, db_column='tool_numbers', blank=True, null=True)
    spindle_speed = models.FloatField(blank=True, null=True)
    feeding_rate = models.FloatField(blank=True, null=True)
    cutting_force = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    prgname = models.CharField(max_length=250, blank=True, null=True)
    production_count = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'monitor_cnc'


class MonitorMachine(models.Model):
    id_check = models.CharField(db_column='ID_check', primary_key=True, max_length=50)  # Field name made lowercase.
    machine_name = models.CharField(max_length=255, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_machine'


class MonitorProduct(models.Model):
    product_id_check = models.CharField(primary_key=True, max_length=50)
    product_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_product'


class MonitorProductionOutput(models.Model):
    stt = models.AutoField(db_column='STT', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey(MonitorProduct, models.DO_NOTHING, blank=True, null=True)
    id = models.ForeignKey(MonitorMachine, models.DO_NOTHING, db_column='id', blank=True, null=True)
    rfid = models.ForeignKey('MonitorWorker', models.DO_NOTHING, db_column='rfid', blank=True, null=True)
    production_amount = models.IntegerField(blank=True, null=True)
    production_quality = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_production_output'


class MonitorTool(models.Model):
    tool_numbers_check = models.CharField(primary_key=True, max_length=50)
    tool_name = models.CharField(max_length=255, blank=True, null=True)
    tool_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tool_diameter = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_tool'


class MonitorWorker(models.Model):
    operator_id = models.CharField(primary_key=True, max_length=50)
    operator_name = models.CharField(max_length=255, blank=True, null=True)
    apartment = models.CharField(max_length=250, blank=True, null=True)
    working_shift = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_worker'
