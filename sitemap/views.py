from django.views import generic


class IndexView(generic.TemplateView):
    """
    This is the home page of the site when no one is logged in
    """
    template_name = 'sitemap/index.html'


class AboutView(generic.TemplateView):
    """
    This is about page of the site
    """
    template_name = 'sitemap/about.html'


class FaqView(generic.TemplateView):
    """
    This is FAQ(Frequently Asked Questions) page of the site
    """
    template_name = 'sitemap/faq.html'


class TosView(generic.TemplateView):
    """
    This is TOS(Terms of Service) page of the site
    """
    template_name = 'sitemap/tos.html'
