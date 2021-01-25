from django.urls import path, include
from rest_framework import routers
# from api
from .views import CustomUserViewSet, AuthorViewSet, BookViewSet, OrderViewSet


router = routers.DefaultRouter()

router.register(r"user", CustomUserViewSet)
router.register(r"author", AuthorViewSet)
router.register(r"book", BookViewSet)
router.register(r"order", OrderViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# urlpatterns = [
#     path('<slug:ob>/create/', views.create),
#     path('<slug:ob>/view/', views.view_all),
# ]
