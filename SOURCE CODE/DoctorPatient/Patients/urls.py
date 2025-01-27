from django.urls import path
from Patients import views
urlpatterns=[
  path('',views.index),
  path('plogin/',views.login),
  path('patientreg/',views.patientreg),
  path('PRegAction',views.PRegAction),
  path('PLogAction',views.LogAction),
  path('bookslot',views.bookslot),
  path('BookAction',views.BookAction),
  path('pviewslotstatus',views.pviewslotstatus),
  path('viewDonation',views.viewDonation)
  ]
