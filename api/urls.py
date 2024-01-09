from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("supervisor/((?P<pk>\d+)/)?", csrf_exempt(SupervisorView.as_view())),
	re_path("sede/((?P<pk>\d+)/)?", csrf_exempt(SedeView.as_view())),
	re_path("programa/((?P<pk>\d+)/)?", csrf_exempt(ProgramaView.as_view())),
	re_path("nte/((?P<pk>\d+)/)?", csrf_exempt(NTEView.as_view())),
	re_path("municipio/((?P<pk>\d+)/)?", csrf_exempt(MunicipioView.as_view())),
	re_path("faculdade/((?P<pk>\d+)/)?", csrf_exempt(FaculdadeView.as_view())),
	re_path("estagiario/((?P<pk>\d+)/)?", csrf_exempt(EstagiarioView.as_view())),
	re_path("edital/((?P<pk>\d+)/)?", csrf_exempt(EditalView.as_view())),
	re_path("curso/((?P<pk>\d+)/)?", csrf_exempt(CursoView.as_view())),
	re_path("sede_supervisor_estagiario/((?P<pk>\d+)/)?", csrf_exempt(EstagiarioView.as_view())),

]