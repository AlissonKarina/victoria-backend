"""victoria_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from core.views import UserAPI, AnswerQuestionAPI, PaperAPI, AnswerTextAPI, ParameterAPI, QuestionAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/user/', UserAPI.as_view(), name = "api_create_user"),
    path('api/1.0/question/', AnswerQuestionAPI.as_view(), name = "api_create_answer_question"),
    path('api/1.0/paper/', PaperAPI.as_view(), name = "api_create_paper"),
    path('api/1.0/paper?processed/', PaperAPI.as_view(), name = "api_get_list_paper"),
    path('api/1.0/answer/', AnswerTextAPI.as_view(), name = "api_create_answer"),
    path('api/1.0/parameter/', QuestionAPI.as_view(), name = "api_create_question"),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)