from django.urls import path
# from .views import postbooklistapi, retrieveapi, postcreateapi
from .views import postsviewset, userviewset


urlpatterns = [
    path('posts/', postsviewset.as_view({'get' : 'list'})),
    path('post/<int:pk>', postsviewset.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    path('create/', postsviewset.as_view({'post' : 'create'})),
    path('user/', userviewset.as_view({'get' : 'list'})),
    path('user/<int:pk>/', userviewset.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}))
    # path("posts/", postlistapi.as_view(), name='postlist'),
    # path("posts/<int:pk>/", retrieveapi.as_view(), name='retrive'),
    # path('create/', postcreateapi.as_view(), name='postcreate')
]