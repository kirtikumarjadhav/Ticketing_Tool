from django.urls import path
from .views import CustomSignupView, ticket_list, ticket_detail, create_ticket, update_ticket_status, ticket_update
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('ticket_list/', ticket_list, name='ticket_list'),
    path('ticket/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('ticket/create/', create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/update_status/', update_ticket_status, name='update_ticket_status'),
    path('<int:ticket_id>/edit/', ticket_update, name='ticket_update'),
]
