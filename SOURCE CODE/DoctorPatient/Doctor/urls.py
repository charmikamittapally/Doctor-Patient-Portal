from django.urls import path
from Doctor import views
urlpatterns=[
  path('doctorlogin/',views.doctorlogin),
  path('doctorreg/',views.doctorreg),
  path('DoctorRegAction',views.DoctorRegAction),
  path('LogAction',views.LogAction),
  path('viewrequest',views.viewrequest),
  path('confirm',views.confirm),
  path('viewdonation',views.viewdonation),
  ]
