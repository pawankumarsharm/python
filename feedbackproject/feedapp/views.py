from django.shortcuts import render
from . import forms
# Create your views here.
def feedback_view(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('validation completed. printing feedback info')
            print('student Name:',form.cleaned_data['name'])
            print('student roll no:',form.cleaned_data['rollno'])
            print('student Email:',form.cleaned_data['email'])
            print('student Feedback:',form.cleaned_data['feedback'])
            return render(request,'feedapp/thanku.html',{'name':form.cleaned_data['name']})
    return render(request,'feedapp/feedback.html',{'form':form})
