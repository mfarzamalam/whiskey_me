from django import forms
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
