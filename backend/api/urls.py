from rest_framework import routers

from api.views import ShipmentViewSet, ShippingCompanyViewSet

router = routers.SimpleRouter()
router.register(r'api/shipments', ShipmentViewSet)
router.register(r'api/companies', ShippingCompanyViewSet)
urlpatterns = router.urls
