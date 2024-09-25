# from django.urls import path
# from .views import PostListView, PostDetailView
#
# urlpatterns = [
#     path('', PostListView.as_view()),
#     path('<int:pk>/', PostDetailView.as_view()),
#
# ]
#
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView

# urlpatterns = [
#     path('', PostView.as_view({'get': 'list', 'post': 'create'})),
#     path('<int:pk>/', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
# ]

router = DefaultRouter()
router.register(r'', PostView, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]

