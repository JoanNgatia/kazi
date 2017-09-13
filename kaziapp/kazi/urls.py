# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# import views

# Method One of routing the modelviewset
# urlpatterns = {
#     url(r'^employers/$', views.EmployersView.as_view(
#         {'get': 'list', 'post': 'create'}), name='all_employers'),
#     url(r'^employers/(?P<pk>[0-9]+)/$',
#         views.EmployersView.as_view({'get': 'retrieve', 'put': 'update'}),
#         name='single_employer'),
#     url(r'^employers/(?P<employer_id>[0-9]+)/employees/$',
#         views.EmployeesView.as_view({'get': 'list', 'post': 'create'}),
#         name='all_employees'),
#     url(r'^employers/(?P<employer_id>[0-9]+)/employees/(?P<pk>[0-9]+)/$',
#         views.EmployeesView.as_view({'get': 'retrieve', 'put': 'update'}),
#         name='single_employee'),
# }

# urlpatterns = format_suffix_patterns(urlpatterns)

from rest_framework.routers import SimpleRouter

from .views import EmployeesView, EmployersView

router = SimpleRouter()
router.register("employers", EmployersView)
router.register("employees", EmployeesView)

urlpatterns = router.urls
