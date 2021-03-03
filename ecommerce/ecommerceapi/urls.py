from .views import ListCategory,ListHeadphone,ListMobileCharger,DetailHeadphone,DetailCategory,DetailMobileCharger

from django.urls import path

urlpatterns=[


    path('categories/',ListCategory.as_view(),name='category'),
    path('categories/<int:pk>/',DetailCategory.as_view()),
    path('mobilecharger/',ListMobileCharger.as_view()),
    path('mobilecharger/<int:pk>/',DetailMobileCharger.as_view()),
    path('headphone/',ListHeadphone.as_view()),
    path('headphone/<int:pk>/',DetailHeadphone.as_view())


]