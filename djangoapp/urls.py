from django.conf.urls import include
from django.urls import path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('gitapp/', include('djangoapp.gitapp.urls')),
    path('docs/', include_docs_urls(title='My API title'))
]
