from django.urls import path
from . import views


urlpatterns = [
    # string describe URL we wanna supoort // pointer at the view function that should be executed // 
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
]