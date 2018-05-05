from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^home$',views.model_form_upload, name = 'upload'),
]
