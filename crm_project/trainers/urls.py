from django.urls import path

from . import views

urlpatterns = [

    path("trainers-list/",views.TrainersListView.as_view(),name="trainers-list"),
    path("trainer-register/",views.RegisterView.as_view(),name="trainer-register"),
    path("trainer-detail/<str:uuid>/",views.TrainerDetailView.as_view(),name="trainer-detail"),
    path("trainer-update/<str:uuid>/",views.TrainerUpdateView.as_view(),name="trainer-update"),
    path("trainer-delete/<str:uuid>/",views.TrainerDeleteView.as_view(),name="trainer-delete"),
]