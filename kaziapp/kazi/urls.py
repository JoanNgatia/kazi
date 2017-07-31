from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = {
    url(r'^employers/$', views.EmployersView.as_view(), name='all_employers'),
    url(r'^employers/(?P<pk>[0-9]+)/$',
        views.EmployersDetailView.as_view(), name='single_employer'),
    url(r'^employers/(?P<employer_id>[0-9]+)/employees/$',
        views.EmployeesView.as_view(), name='all_employees'),
    url(r'^employers/(?P<employer_id>[0-9]+)/employees/(?P<pk>[0-9]+)/$',
        views.EmployeeDetailView.as_view(), name='single_employee'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
