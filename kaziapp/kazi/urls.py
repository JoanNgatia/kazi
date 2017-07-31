from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = {
    url(r'^employers/$', views.EmployersView.as_view(), name='all_employers'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
