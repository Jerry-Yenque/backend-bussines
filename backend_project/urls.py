from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls # new
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Tu API",
        default_version='v1',
        description="Descripción de la API",
        contact=openapi.Contact(email="contacto@tuapi.com"),
        license=openapi.License(name="Licencia BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



#schema_view = get_schema_view(title='Blog API') # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),  # updated]+
    path('api/v1/rest-auth/registration/',include('dj_rest_auth.registration.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),  # Ruta para la documentación    path('schema/', schema_view), # new
   
]