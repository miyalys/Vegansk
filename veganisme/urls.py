from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#For development, media_root:
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('products.views',
    url(r'^$', 'index', name="index"),
	url(r'^id/(?P<product_id>\d+)/$', 'product_page_by_id', name="product_page_by_id"),
	url(r'^ingredient/id/(?P<ingredient_id>\d+)/$', 'ingredient_page_by_id', name="ingredient_page_by_id"),
    url(r'^produktliste/$', 'list_all_products', name="list_all"),
    url(r'^soege-formular/$', 'search_form', name="search_form"),
    url(r'^soeg/$', 'search', name="search"),
    url(r'^tilfoej/(?P<category>\w*)/$', 'add_form', name="add_form"),
    url(r'^id/(?P<product_id>\d+)/rediger/$', 'edit_form', name="edit_form"),
    url(r'^links/$', 'links', name="links"),
    url(r'^comments/', include('django.contrib.comments.urls')),

#   url(r'^tilfoej-produkt/$', 'add_form', name="add_form"),
#   url(r'^tilfoej-(?P<add_category>\[a-z]*)/$', 'add_form', name="add_form"),
#   url(r'^produkt/(?P<q>[0-9a-zA-Z-]+)?/$', 'search_test', name="search_test"),
#   url(r'^search-results/$', views.search),


	# Examples:
    # url(r'^$', 'vegansk.views.home', name='home'),
    # url(r'^vegansk/', include('vegansk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
  url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
#  url(r'^create/$', 'django.views.generic.create_update.create_object', {'model': 'products.product'}),
)

#For development, media_root:
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('', 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))