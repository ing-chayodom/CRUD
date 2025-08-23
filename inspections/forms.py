from django import forms
from .models import InspectionRecord

class InspectionForm(forms.ModelForm):
    class Meta:
        model = InspectionRecord
        fields = ['inspection_no','product_code','product_name','price','smell','ph','status']
        labels = {
            'inspection_no': 'เลขที่ใบตรวจสินค้า',
            'product_code':  'รหัสสินค้า',
            'product_name':  'ชื่อสินค้า',
            'price':         'ราคา',
            'smell':         'แยกกลิ่น',
            'ph':            'ค่า pH',
            'status':        'สถานะ',
        }
        widgets = {
            'inspection_no': forms.TextInput(attrs={'class':'form-control','placeholder':'เช่น CHK-2025-0001'}),
            'product_code':  forms.TextInput(attrs={'class':'form-control','placeholder':'เช่น P-001'}),
            'product_name':  forms.TextInput(attrs={'class':'form-control','placeholder':'เช่น สบู่กลิ่นส้ม'}),
            'price':         forms.NumberInput(attrs={'class':'form-control','step':'0.01','min':'0','placeholder':'เช่น 120.00'}),
            'smell':         forms.TextInput(attrs={'class':'form-control','placeholder':'เช่น Citrus'}),
            'ph':            forms.NumberInput(attrs={'class':'form-control','step':'0.01','min':'0','max':'14','placeholder':'0–14'}),
            'status':        forms.Select(attrs={'class':'form-select'}),
        }

    def clean_ph(self):
        ph = self.cleaned_data['ph']
        # เผื่อมี logic เพิ่มเติมทีหลัง
        return ph
