from django.urls import path
from .views import (
    InspectionListView, InspectionCreateView,
    InspectionUpdateView, InspectionDeleteView
)

urlpatterns = [
    path('', InspectionListView.as_view(), name='inspection_list'),
    path('create/', InspectionCreateView.as_view(), name='inspection_create'),
    path('<int:pk>/edit/', InspectionUpdateView.as_view(), name='inspection_edit'),
    path('<int:pk>/delete/', InspectionDeleteView.as_view(), name='inspection_delete'),
]