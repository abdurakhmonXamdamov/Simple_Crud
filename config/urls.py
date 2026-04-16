from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('apps.accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('auth/register', RegisterView.as_view(), name="register"),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Api Doc
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
