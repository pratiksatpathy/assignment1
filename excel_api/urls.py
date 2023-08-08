from django.urls import path

from excel_api.views import index, show, update, Api

urlpatterns = [
    path('upload', Api.as_view()),
    path('', show),
    path('update',update)
]
