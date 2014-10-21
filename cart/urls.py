from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^Products/$','shop.views.ProductALL'),
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^Products/(?P<productslug>.*)/$','shop.views.SpecificProduct'),
    (r'^brand/(?P<brandslug>.*)/$','shop.views.SpecificBrand'),
)
