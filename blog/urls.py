from django.urls import path
from .views import one, display, add_post, edit, delete, registeruser, loginuser, logoutuser, search, categories, year_filter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", one, name='one'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', display, name='list'),
    path("add_post/", add_post.as_view(), name='create'),
    path('edit/<int:pk>/', edit.as_view(), name='edit'),
    path("delete/<int:pk>/", delete.as_view(), name='delete'),
    path('register/', registeruser, name='register'),
    path('login/', loginuser, name='login'),
    path("logout/", logoutuser, name='logout'),
    path('search/', search, name='search'),
    path('category/<slug:slug>/', categories, name='cat'),
    path('date_filter/<int:month>/<int:year>/', year_filter, name='date_filter')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)