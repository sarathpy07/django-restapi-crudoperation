from rest_framework.routers import DefaultRouter
from . views import userapiviewset
from django.urls import path, include
router=DefaultRouter()
router.register('apiuser',userapiviewset)

urlpatterns= [
    path('api/',include(router.urls))

]
