from django.db import models

# Create your models here.


class MonitorCnc(models.Model):
    # Field name made lowercase.
    stt = models.AutoField(db_column='STT', primary_key=True)
    # Field name made lowercase.
    id = models.ForeignKey('MonitorMachine', models.DO_NOTHING,db_column='ID', blank=True, null=True)
    # Field name made lowercase.
    rfid = models.ForeignKey('MonitorWorker', models.DO_NOTHING, db_column='operator_id', blank=True, null=True)
    product = models.ForeignKey('MonitorProduct', models.DO_NOTHING, blank=True, null=True)
    tool_numbers = models.ForeignKey('MonitorTool', models.DO_NOTHING, db_column='tool_numbers', blank=True, null=True)
    spindle_speed = models.FloatField(blank=True, null=True)
    feeding_rate = models.FloatField(blank=True, null=True)
    cutting_force = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    prgname = models.CharField(max_length=250, blank=True, null=True)
    production_count = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField()

    #@property
    #def worker(self):
        #return self.rfid.operatorname

    class Meta:
        managed = False
        db_table = 'monitor_cnc'


class MonitorMachine(models.Model):
    # Field name made lowercase.
    id_check = models.CharField(
    db_column='ID_check', primary_key=True, max_length=50)
    machine_name = models.CharField(max_length=255, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
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
    # Field name made lowercase.
    stt = models.AutoField(db_column='STT', primary_key=True)
    product = models.ForeignKey(
        MonitorProduct, models.DO_NOTHING, blank=True, null=True)
    id = models.ForeignKey(MonitorMachine, models.DO_NOTHING,
                           db_column='id', blank=True, null=True)
    rfid = models.ForeignKey(
        'MonitorWorker', models.DO_NOTHING, db_column='rfid', blank=True, null=True)
    production_amount = models.IntegerField(blank=True, null=True)
    production_quality = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_production_output'


class MonitorTool(models.Model):
    tool_numbers_check = models.CharField(primary_key=True, max_length=50)
    tool_name = models.CharField(max_length=255, blank=True, null=True)
    tool_length = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    tool_diameter = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
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
