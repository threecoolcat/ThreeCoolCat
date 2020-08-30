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


class FineUploadGalleryWidget(Widget):
    @property
    def media(self):
        js = ["fine-uploader/5.14.1/fine-uploader.min.js", "fine-uploader/uploadhelper.js"]
        css = {"all": ("fine-uploader/5.14.1/fine-uploader-gallery.css",)}
        return Media(js=["%s" % path for path in js], css=css)

    def render(self, name, value, attrs=None, renderer=None):
        return """<input type="hidden" id="id_{name}" name="{name}" value="{value}" />
<div id="uploader-{name}" class="col-md-12" style="{style}"></div>
<script type="text/javascript">
uploadhelper.config("{name}", "picture", "/common/upload/session/?url={value}", {multiple});
</script>
        """.format(name=name, value=value, style=self.attrs['style'] if 'style' in self.attrs else '',
                   multiple=self.attrs['multiple'] if 'multiple' in self.attrs else 'false')


class FineUploadThumbnailWidget(Widget):
    @property
    def media(self):
        js = ["fine-uploader/5.14.1/fine-uploader.min.js", "fine-uploader/uploadhelper.js"]
        css = {"all": ("fine-uploader/5.14.1/fine-uploader-new.css",)}
        return Media(js=["%s" % path for path in js], css=css)

    def render(self, name, value, attrs=None, renderer=None):
        disabled = 'true' if 'disabled' in attrs and attrs['disabled'] else 'false'
        return """<input type="hidden" id="id_{name}" name="{name}" value="{value}" />
<input type="hidden" id="{name}_count" name="{name}_count" value="0" />
<div id="uploader-{name}" class="col-md-12" style="{style}"></div>
<script type="text/javascript">
uploadhelper.config("{name}", "{type}", "{value}", {multiple}, {disabled});
</script>
        """.format(name=name, value=value, style=self.attrs['style'] if 'style' in self.attrs else '',
                   multiple=self.attrs['multiple'] if 'multiple' in self.attrs else 'false', type=self.attrs['type'],
                   disabled=disabled)