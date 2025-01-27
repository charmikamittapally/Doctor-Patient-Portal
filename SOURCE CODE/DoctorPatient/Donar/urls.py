from django.urls import path
from Donar import views
urlpatterns=[
  path('donarlogin/',views.donarlogin),
  path('donarreg/',views.donarreg),
  path('DonarRegAction',views.PRegAction),
  path('DLogAction',views.LogAction),
  path('donateorgan',views.donateorgan),
  path('donateorganaction',views.donateorganaction),
  path('viewmydonation',views.viewmydonation)
  ]
