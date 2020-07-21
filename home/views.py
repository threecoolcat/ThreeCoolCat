from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


#自定义网站主页
class IndexView(TemplateView):
    template_name = 'home/index.html'

    # 页面加载时，给页面传值
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '三酷猫'
        return context


# 自定义404页面
def page_not_found(request, exception=None, template_name='404.html'):
    context = {'hello': 'world'}
    return render(request, '404.html', context)
