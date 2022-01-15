from django import forms
from django.http import request
from order.models import Address
from .models import Review

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'



    class Meta:
        model = Review
        fields = '__all__'



class CustomerAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['fname'].widget.attrs['placeholder'] = 'Enter Your First Name'

        self.fields['lname'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['lname'].widget.attrs['placeholder'] = 'Enter Last Name'

        self.fields['country'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter Your Country'

        self.fields['address_1'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['address_1'].widget.attrs['placeholder'] = 'Enter First Address'

        self.fields['address_2'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['address_2'].widget.attrs['placeholder'] = 'Enter Second Address'

        self.fields['city'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['city'].widget.attrs['placeholder'] = 'Enter Your City'

        self.fields['state'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['state'].widget.attrs['placeholder'] = 'Enter Your State'

        self.fields['contact'].widget.attrs['class'] = 'form-input col-12 my-1'
        self.fields['contact'].widget.attrs['placeholder'] = 'Enter Your Contact'


    class Meta:
        model = Address
        fields = '__all__'