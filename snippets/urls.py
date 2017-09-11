from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
]

# format_suffix_patterns : 이거 어떤거 하는건지? 설명 제대로 안되어있는듯
urlpatterns = format_suffix_patterns(urlpatterns)
