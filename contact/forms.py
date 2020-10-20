from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    from_email = forms.EmailField(required = True)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea ,  required = True)