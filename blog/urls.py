from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("blog/",views.blog,name="blog"),
    path("search/",views.blogSearch,name="search"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.Login,name="login"),
    path("logout/",views.Logout,name="logout"),
    path("postcomment/",views.Postcomment,name="postcomment"),
    path("<str:slug>",views.blogContent,name="blog content")

]