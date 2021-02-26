from django.urls import path
from resumesite.views import homepage, blog, about, advice

urlpatterns = [
	path('', homepage, name='home'),
	path('blogs/', blog, name='blog'),
	path('blogs/about/', about, name='about'),
	path('blogs/about/advice', advice, name='advice'),
]
