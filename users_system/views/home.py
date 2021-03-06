__author__ = 'learnercys'

from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super(HomeView, self).get_context_data(**kwargs)
