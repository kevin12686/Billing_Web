import uuid
from django.db import models
from django.utils.timezone import now


# Create your models here.

class Record(models.Model):
    EXPEND = 'EX'
    INCOME = 'IN'
    TRANSFER = 'TR'
    MODE_CHOICES = ((EXPEND, '支出'), (INCOME, '收入'), (TRANSFER, '轉帳'))
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='UUID')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    transaction_date = models.DateField(default=now, verbose_name='交易時間')
    own_account = models.ForeignKey('Account', on_delete=models.CASCADE, verbose_name='帳戶')
    record_type = models.CharField(max_length=2, choices=MODE_CHOICES, null=False, default=EXPEND, verbose_name='記錄型態')
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=False, default=0, verbose_name='金額')
    description = models.TextField(blank=True, verbose_name='備註')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.record_type == self.INCOME:
            self.own_account.balance += self.amount
        else:
            self.own_account.balance -= self.amount
        self.own_account.save()
        super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        if self.record_type == self.INCOME:
            self.own_account.balance -= self.amount
        else:
            self.own_account.balance += self.amount
        self.own_account.save()
        super().delete(using=None, keep_parents=False)


class Account(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='UUID')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    name = models.CharField(max_length=50, verbose_name='帳戶名稱')
    initial_amount = models.DecimalField(max_digits=11, decimal_places=2, null=False, default=0, verbose_name='初始金額')
    balance = models.DecimalField(max_digits=11, decimal_places=2, null=False, default=0, verbose_name='餘額')
    description = models.TextField(blank=True, verbose_name='備註')

    @classmethod
    def create(cls, name, initial_amount, description):
        account = cls(name=name, initial_amount=initial_amount, balance=initial_amount, description=description)
        account.save()

    def __str__(self):
        return self.name
