# File contains URL definitions
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from company import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
