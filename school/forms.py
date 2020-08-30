from django import forms
import datetime
from home.widgets import LayDateWidget, FineUploadThumbnailWidget


class CourseForm(forms.ModelForm):
    start_date = forms.DateField(label='开课日期', required=False,
                                 widget=LayDateWidget(attrs={'style': 'width:120px', 'readonly': 'true'}),
                                 initial=datetime.date.today())
    # cover = forms.CharField(label='封面', max_length=500, required=False,
    #                         widget=FineUploadThumbnailWidget(
    #                             attrs={'title': '', 'multiple': 'false', 'type': 'jpg'}))