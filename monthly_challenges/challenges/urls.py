from django.urls import path
from . import views


urlpatterns = [
    # string describe URL we wanna supoort // pointer at the view function that should be executed // 
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge),
]