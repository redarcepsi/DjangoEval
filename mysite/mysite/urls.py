from django.contrib import admin
from django.urls import path
from firstapp.views import index,login,detail,inscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("detail/<int:event_id>", detail, name="detail"),
    path("inscription/<int:event_id>",inscription,name="inscrption_event")
]
