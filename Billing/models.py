import uuid
from django.db import models


# Create your models here.

class Record(models.Model):
    EXPEND = 'EX'
    INCOME = 'IN'
    TRANSFER = 'TR'
    MODE_CHOICES = ((EXPEND, '支出'), (INCOME, '收入'), (TRANSFER, '轉帳'))
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='UUID')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    transaction_time = models.DateTimeField(auto_now=True, verbose_name='交易時間')
    record_type = models.CharField(max_length=2, choices=MODE_CHOICES, null=False, default=EXPEND, verbose_name='記錄型態')
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=False, default=0, verbose_name='金額')
    fee = models.DecimalField(max_digits=11, decimal_places=2, null=False, default=0, verbose_name='手續費')
