# shared_apps/tenants/urls.py
from shared_apps.tenants import views
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("api/", include([
        path("admin/", admin.site.urls),

        path("", include("shared_apps.custom_auth.urls")),
        path("", include("shared_apps.billing.urls")),

        path("tenants/signup/", views.TenantSignupView.as_view(), name="tenant-signup"),
        path("tenants/check-availability/", views.CheckTenantAvailabilityView.as_view(), name="check-availability"),
        path("tenant/validate-tenant-name/", views.validate_tenant_name, name="validate-tenant-name"),
        path("tenants/send-otp/", views.SendOTPView.as_view(), name="send-otp"),
        path("tenants/verify-otp/", views.VerifyOTPView.as_view(), name="verify-otp"),
        path("tenants/find-workspace/", views.FindWorkspaceView.as_view(), name="find-workspace"),
        
        path('super-admin-dashboard/', views.super_admin_dashboard, name='super_admin_dashboard'),
        path('toggle-block/<int:tenant_id>/', views.toggle_block_tenant, name='toggle_block_tenant'),
    ])),
]