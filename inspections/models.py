from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class InspectionRecord(models.Model):
    STATUS_CHOICES = [
        ('PASS', 'Pass'),
        ('NOT_PASS', 'Not Pass'),
    ]

    inspection_no = models.CharField(max_length=50, unique=True, verbose_name='เลขที่ใบตรวจสินค้า')
    product_code  = models.CharField(max_length=50, verbose_name='รหัสสินค้า')
    product_name  = models.CharField(max_length=100, blank=True, null=True, verbose_name='ชื่อสินค้า')   # ใหม่
    price         = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='ราคา')  # ใหม่
    smell         = models.CharField(max_length=100, verbose_name='แยกกลิ่น')
    ph            = models.DecimalField(max_digits=4, decimal_places=2,
                                        validators=[MinValueValidator(0), MaxValueValidator(14)],
                                        verbose_name='ค่า pH')
    status        = models.CharField(max_length=8, choices=STATUS_CHOICES, verbose_name='สถานะ')
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['inspection_no']),
            models.Index(fields=['product_code']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.inspection_no} - {self.product_code}'