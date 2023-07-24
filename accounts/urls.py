# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.user_registration_view, name='register'),
#     path('login/', views.user_login_view, name='login'),
#     path('logout/', views.user_logout_view, name='logout'),
# ]

#from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),  # Replace 'accounts' with the name of your app
#     # Other URL patterns for your project
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.user_registration_view, name='register'),
#     path('login/', views.user_login_view, name='login'),
#     path('logout/', views.user_logout_view, name='logout'),
# ]


from django.urls import path
from .views import UserRegistrationView, CustomAuthToken
from .views import WorkListCreateView, WorkFilterListView,  ArtistSearchView
from . import views

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', CustomAuthToken.as_view(), name='user-login'),
    path('api/works/new_works/', views.new_works, name='new_works'),
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('works/<str:work_type>/', WorkFilterListView.as_view(), name='work-filter-list'),
    path('works/search/', ArtistSearchView.as_view(), name='work-artist-search'),
]

