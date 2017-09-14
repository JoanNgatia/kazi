from rest_framework.routers import SimpleRouter

from .views import EmployeesView, EmployersView

router = SimpleRouter()
router.register("employers", EmployersView, base_name="all_employers")
router.register("employees", EmployeesView, base_name="all_employees")

urlpatterns = router.urls
