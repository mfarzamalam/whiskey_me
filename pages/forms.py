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

        self.fields['fname'].label = "Enter Your First Name"
        self.fields['fname'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['lname'].label = "Enter Last Name"
        self.fields['lname'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['country'].label = "Enter Your Country"
        self.fields['country'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['address_1'].label = "Enter First Address"
        self.fields['address_1'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['address_2'].label = "Enter Second Address"
        self.fields['address_2'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['city'].label = "Enter Your City"
        self.fields['city'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['state'].label = "Enter Your State"
        self.fields['state'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'

        self.fields['contact'].label = "Enter Your Contact"
        self.fields['contact'].widget.attrs['class'] = 'form-input fw-bold col-12 my-1'


    class Meta:
        model = Address
        exclude=('user',)
        fields = '__all__'