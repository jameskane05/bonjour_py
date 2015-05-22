from django.conf.urls import url

from . import views

urlpatterns = [
    # routes things past the /greetings root path
    url(r'^$', views.index, name="index")
    # r means regular exp, ' indicates the string, ^ means start of line, $ means end of line
]

