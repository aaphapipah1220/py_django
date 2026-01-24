from django.contrib import admin
from django.urls import path, include
from members import views
from django.conf import settings
from django.conf.urls.static import static
from core.views import leads_create, trial_create, get_lead_detail

urlpatterns = [
    path("", views.main, name="main"),
    path('members/', include('members.urls')),
    path('testing/', views.testing, name="testing"),
    path('admin/', admin.site.urls),
    path('leads/new/', leads_create, name='leads_create'),
    path('trial/new/', trial_create, name='trial_create'),
    path('api/leads/<int:lead_id>/', get_lead_detail, name="get_lead_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
