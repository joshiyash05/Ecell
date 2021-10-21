from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('Name','Sapid','Branch','contactno','emailid')
        labels = {
            'Name':'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['Branch'].empty_label = "Select"
        self.fields['contactno'].required = False