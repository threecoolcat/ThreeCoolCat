from django import forms
import datetime
from home.widgets import LayDateWidget


class CourseForm(forms.ModelForm):
    start_date = forms.DateField(label='开课日期', required=False,
                                 widget=LayDateWidget(attrs={'style': 'width:120px', 'readonly': 'true'}),
                                 initial=datetime.date.today())
