from rest_framework.routers import SimpleRouter
from django.urls import include, path
from . import views
from .views import func1, second_view

router = SimpleRouter()
router.register('newfunc', func1)
router.register('fun', second_view)
urlpatterns = [

    path('car/create', views.func1.as_view({'post': 'create'}), name='car'),
    path('c/', include(router.urls)),
    path('c/create_2', views.second_view.as_view({'post': 'create_2'}), name='create_2'),

]
