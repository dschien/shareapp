# from django.conf.urls.defaults import url, patterns, include
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import viewsets, routers
from api import views

from api.models import Item

admin.autodiscover()


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    model = Group


# ViewSets define the view behavior.
class ItemViewSet(viewsets.ModelViewSet):
    model = Item

# class GroupViewSet(viewsets.ModelViewSet):
# model = Group


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'shareapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^apibrowse/', include(router.urls)),
                       url(r'^api/additem$', views.addItem, name='additem'),
                       url(r'^api/requestitem$', views.requestItem, name='requestitem'),
                       url(r'^$', login_required(TemplateView.as_view(template_name="index.html")), name="home"),
                       url(r'^social_login/', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('registration.backends.default.urls')),
)
