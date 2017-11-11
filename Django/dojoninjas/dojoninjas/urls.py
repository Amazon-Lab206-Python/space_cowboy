<<<<<<< HEAD
from django.conf.urls import url, include
=======
from django.conf.urls import url
>>>>>>> 144a8482319f5d16d72944556782b98b4e198ad6
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^', include('apps.dojo_ninjas.urls'))
=======
>>>>>>> 144a8482319f5d16d72944556782b98b4e198ad6
]