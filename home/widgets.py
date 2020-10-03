from django.forms import Widget, Media, widgets


# 日期下拉控件，使用LayDate封装
# example code
# birthday = forms.DateField(label='出生日期', required=False, widget=LayDateWidget(attrs={'style': 'width:260px'}))
class LayDateWidget(widgets.TextInput):
    def __init__(self, mintime=None, attrs=None):
        super(LayDateWidget, self).__init__(attrs)
        self.mintime = mintime
        self.attrs = attrs

    @property
    def media(self):
        js = ["laydate/laydate.js"]
        return Media(js=["%s" % path for path in js])

    def render(self, name, value, attrs=None, renderer=None):
        out = super(LayDateWidget, self).render(name, value, attrs)
        out += """
<script>
var $ = django.jQuery
var v = $('#id_{name}').val();
$('#id_{name}').val(v.substr(0,10));
laydate({{
   elem: '#id_{name}',
   format: 'YYYY-MM-DD',
   {mintime} }});
</script>""".format(name=name, mintime="min: '" + self.mintime.strftime("%Y-%m-%d") + "'," if self.mintime else "")
        return out

