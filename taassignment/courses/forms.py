from django import forms
from .models import Course
from taassignment.users.models import User

class UploadFileForm(forms.Form):
    file  = forms.FileField()


class CourseForm(forms.ModelForm):
       
    course_no = forms.CharField(label="Course", required=True, widget=forms.TextInput(attrs={'placeholder': 'Course No.', 'class' : 'form-control'}))
    course_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Course Name', 'class' : 'form-control'}))
    
    list_of_faculties = User.objects.filter(is_faculty=True)
    list_of_tas = User.objects.filter(is_ta=True)

    faculties = forms.ModelMultipleChoiceField(label="Teacher", required=True, queryset=list_of_faculties)
    tas = forms.ModelMultipleChoiceField(label="TA", required=False, queryset=list_of_tas)

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
       
        self.fields['faculties'].widget.attrs['class'] = 'form-control'
        self.fields['tas'].widget.attrs['class'] = 'form-control'

    def clean_faculties(self):
        faculties = self.cleaned_data.get('faculties')
        
        return User.objects.filter(id__in=faculties)

    def clean_tas(self):
        tas = self.cleaned_data.get('tas')

        return User.objects.filter(id__in=tas)

    class Meta:
        model = Course
        fields = (
            'course_no',
            'course_name',
            'faculties',
            'tas'
        )


class SelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(SelectionForm, self).__init__(*args, **kwargs)

        self.courses = Course.objects.filter(faculties=self.user)
        tas = User.objects.filter(is_ta=True)
        for course in self.courses:
            field = forms.ModelMultipleChoiceField(queryset=tas, required=False, widget=forms.SelectMultiple(attrs={'class': 'multi_select form-control' }))
            field.initial = course.tas.all()
            self.fields[str(course.pk)] = field

    def save(self):
        for course in self.courses:
            tas = self.cleaned_data.get(str(course.pk), [])
            course.tas.clear()
            for ta in tas:
                course.tas.add(ta)