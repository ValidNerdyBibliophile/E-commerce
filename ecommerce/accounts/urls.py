from django.urls import path
from .views import UserList, UserListCreate, UserDetail

# urlpatterns = [
#     path('accounts/', UserListCreate.as_view(), name='user-list-create'),
#     path('accounts/<int:user_id>/', UserDetail.as_view(), name='user-detail'),
# ]

urlpatterns = [
    path('accounts/', UserListCreate.as_view(), name='user-list-create'),
    path('accounts/list/', UserList.as_view(), name='user-list'),
    path('accounts/<str:identifier>/', UserDetail.as_view(), name='user-detail')
]
