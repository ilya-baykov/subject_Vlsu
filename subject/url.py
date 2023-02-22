from django.urls import path
from subject import views as data_subject

urlpatterns = [
    path('menu',data_subject.menu),
    path('<int:current_subject_int>', data_subject.choice_of_discipline_int),
    path('<str:current_subject_str>', data_subject.choice_of_discipline_str, name="subject_url"),
]
