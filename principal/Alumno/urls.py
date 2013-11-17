from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^alumnoInicio/$' , 'principal.Alumno.views.alumnoInicio'),
	url(r'^alumnoDatosGen/$' , 'principal.Alumno.views.alumnoDatosGen'),
	url(r'^actualizarInfo/$' , 'principal.Alumno.views.actualizarInfo'),
	url(r'^alumnoKardex/$' , 'principal.Alumno.views.alumnoKardex'),
	url(r'^kardexframe/$' , 'principal.Alumno.views.kardexframe'),
	url(r'^alumnoHorario/$' , 'principal.Alumno.views.alumnoHorario'),
	url(r'^horarioframe/$' , 'principal.Alumno.views.horarioframe'),
	url(r'^alumnoCalifsemestre/$' , 'principal.Alumno.views.alumnoCalifsemestre'),
	url(r'^califsemestreframe/$' , 'principal.Alumno.views.califsemestreframe'),
	url(r'^alumnoCalifets/$' , 'principal.Alumno.views.alumnoCalifets'),
	url(r'^califetsframe/$' , 'principal.Alumno.views.califetsframe'),
	url(r'^alumnoCalifsaberes/$' , 'principal.Alumno.views.alumnoCalifsaberes'),
	url(r'^califsaberesframe/$' , 'principal.Alumno.views.califsaberesframe'),

	url(r'^alumnoInscEts/$' , 'principal.Alumno.views.alumnoInscEts'),
	url(r'^inscetsframe/$' , 'principal.Alumno.views.inscetsframe'),
	url(r'^alumnoInscSaberes/$' , 'principal.Alumno.views.alumnoInscSaberes'),
	url(r'^inscsaberesframe/$' , 'principal.Alumno.views.inscsaberesframe'),
	url(r'^procesarSpa/$' , 'principal.Alumno.views.procesarSpa'),

	url(r'^alumnoTutor/$' , 'principal.Alumno.views.alumnoTutor'),
	url(r'^alumnoSolicitardocs/$' , 'principal.Alumno.views.alumnoSolicitardocs'),
	url(r'^solicitardocsframe/$' , 'principal.Alumno.views.solicitardocsframe'),
	url(r'^procesarSolicitud/$' , 'principal.Alumno.views.procesarSolicitud'),
	
	url(r'^alumnoEvaluarprofs/$' , 'principal.Alumno.views.alumnoEvaluarprofs'),
	url(r'^evaluarprofsframe1/$', 'principal.Alumno.views.evaluarprofsframe1'),
	url(r'^evaluarprofsframe2/(?P<idmat>\S+)/$'  , 'principal.Alumno.views.evaluarprofsframe2'),
	url(r'^realizarEvaluacion/(?P<idmat>\S+)/$', 'principal.Alumno.views.realizarEvaluacion'),

	url(r'^alumnoHorariolabs/$' , 'principal.Alumno.views.alumnoHorariolabs'),
	url(r'^horariolabsframe/$' , 'principal.Alumno.views.horariolabsframe'),
	url(r'^alumnoCambiarpass/$' , 'principal.Alumno.views.alumnoCambiarpass'),
	url(r'^cambiarPass/$' , 'principal.Alumno.views.cambiarPass'),
	url(r'^datgenRedirect/$', 'principal.Alumno.views.datgenRedirect'),
	url(r'^Alinscribirsemestre/$' , 'principal.Alumno.views.alumnoinscsem'),
	url(r'^getMateria/$' , 'principal.Alumno.views.getMateria'),
	url(r'^getResult/$' , 'principal.Alumno.views.getResult'),
	url(r'^insertData/$' , 'principal.Alumno.views.insertData'),
	url(r'^delData/$' , 'principal.Alumno.views.delData'),
	url(r'^delallData/$' , 'principal.Alumno.views.delallData'),
	url(r'^addAll/$' , 'principal.Alumno.views.addAll'),
	url(r'^updateAct/$' , 'principal.Alumno.views.updateAct'),
	url(r'^final/$' , 'principal.Alumno.views.final'),
	url(r'^Alcita/$' , 'principal.Alumno.views.cita'),
	url(r'^reporteHorario/$' , 'principal.Alumno.views.reporteHorario'),
	url(r'^reporteKardex/$' , 'principal.Alumno.views.reporteKardex'),
	url(r'^reporteBoleta/$' , 'principal.Alumno.views.reporteBoleta'),
	url(r'^reporteConstancia/$' , 'principal.Alumno.views.reporteConstancia'),
	url(r'^reporteETS/$' , 'principal.Alumno.views.reporteETS'),
)