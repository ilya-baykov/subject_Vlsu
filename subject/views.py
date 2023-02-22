from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

dict_subject = {
    "system_analysis": "Лексин А.Ю.",
    "spoken_foreign_language": " Зимакова Е.С.",
    "political_science": "Ефимова С.А",
    "fuzzy_sets": "Абрахин С.И.",
}
list_subject = list(dict_subject)


def choice_of_discipline_str(request, current_subject_str):
    if dict_subject.get(current_subject_str):
        return HttpResponse(f"<h2>Преподователь по {current_subject_str}  - {dict_subject[current_subject_str]}</h2>")
    return HttpResponseNotFound(f"Нам очень жаль , но мы не знаем такую дисцилину ;с  {current_subject_str}")


def choice_of_discipline_int(request, current_subject_int):
    if len(list_subject) >= current_subject_int > 0:
        url_link = reverse('subject_url', args=(list_subject[current_subject_int - 1],))
        return HttpResponseRedirect(url_link)
    return HttpResponseNotFound(f"Введите число от 1 до 4 , вы ввели - {current_subject_int}")


def menu(request):
    response = "<ol>"
    for subject in list_subject:
        url_link = reverse('subject_url', args=(subject,))
        response += f"<li> <a href = '{url_link}'> {subject.title().replace('_', ' ')} </a> </li>"
    response += "</ol>"
    return HttpResponse(response)
