from functools import reduce
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.sites.models import Site


class SitesView(ListView):
    model = Site
    template_name = 'sites.html'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        context.update({'sites': Site.objects.all(),
                        'active': 'sites'})
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )


class SiteDetailView(DetailView):
    model = Site
    pk_url_kwarg = 'site_id'
    template_name = 'site.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context.update({'active': 'sites'})
        return self.render_to_response(context)


class SummaryView(ListView):
    model = Site
    template_name = 'summary.html'

    def render_to_response(self, context, **response_kwargs):
        context.update({'active': 'summary'})

        for i in context['object_list']:
            a_value = reduce(lambda x, y: x + y, [i.a_value for i in i.values.all()])
            b_value = reduce(lambda x, y: x + y, [i.b_value for i in i.values.all()])

            setattr(i, 'a_value', a_value)
            setattr(i, 'b_value', b_value)

        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )


class SummaryAverageView(ListView):
    model = Site
    template_name = 'summary.html'

    def render_to_response(self, context, **response_kwargs):
        context.update({'active': 'average'})

        for i in context['object_list']:
            total_values = len(i.values.all())
            a_value = reduce(lambda x, y: x + y, [i.a_value for i in i.values.all()])
            b_value = reduce(lambda x, y: x + y, [i.b_value for i in i.values.all()])

            a_value /= total_values
            b_value /= total_values

            setattr(i, 'a_value', a_value)
            setattr(i, 'b_value', b_value)

        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
