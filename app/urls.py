from rest_framework.routers import SimpleRouter
from .views import PrivateViewSet,PublicViewSet



router = SimpleRouter()
router.register('private', PrivateViewSet, basename='private')
router.register('public', PublicViewSet, basename='publics')
urlpatterns = router.urls