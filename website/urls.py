
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('blog-single.html', views.blogsingle, name="blog-single"),
    path('blog.html', views.blog, name="blog"),
    path('index-2.html', views.index2, name="index-2"),
    path('portfolio-details.html', views.portfoliodetails, name="portfolio-details"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('services.html', views.services, name="services"),
    path('team.html', views.team, name="team"),

]
