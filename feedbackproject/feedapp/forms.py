from django import forms
from django.core import validators
def gmail_varification(value):
    if value[len(value)-9:] !='gmail.com':
            raise forms.ValidationError('must be gmail')

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_varification])
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

#     def clean_name(self):
#         inputname=self.cleaned_data['name']
#         if len(inputname)<4:
#             raise forms.ValidationError('The lenght of name field should be less & equal to 4')
#         return inputname
#
# def clean_rollno(self):
#     inputrollno=self.cleaned_data['rollno']
#     print('validating rollno')
#     return inputrollno
#
# def clean_email(self):
#     inputemail=self.cleaned_data['email']
#     print('validating email')
#     return inputemail
#
# def clean_feedback(self):
#     inputfeedback=self.cleaned_data['feedback']
#     print('validating feedback')
#     return inputfeedback
