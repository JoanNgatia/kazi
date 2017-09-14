from rest_framework.routers import SimpleRouter

from .views import EmployeesView, EmployersView

router = SimpleRouter()
router.register("employers", EmployersView)
router.register("employees", EmployeesView)

urlpatterns = router.urls
