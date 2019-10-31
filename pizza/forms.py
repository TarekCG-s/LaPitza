from django.forms import CharField, Form, ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Address

class Address(ModelForm):
    # city = CharField(max_length=24)
    # district = CharField(max_length=24)
    # street = CharField(max_length=24)
    # building_num = CharField(max_length=24)
    # phone = PhoneNumberField()
    class Meta:
        model = Address
        fields = ['city', 'district', 'street', 'building_num', 'phone']
