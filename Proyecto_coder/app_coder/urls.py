from django.urls import path
from app_coder.views import alta_curso, curso,  info_familia, integrantes_familia

urlpatterns=[

    path('cursos', curso),
    path('otro_curso/<nombre>', alta_curso),
    path('familia', info_familia),
    path('familias/<numero>/<fecha>/<cadena>', integrantes_familia),

]