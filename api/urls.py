from django.urls import path

from .views import (
    RegisterView,
    QueryKBView,
    UsageSummaryView,
    LoginView
)

urlpatterns = [
    # Register
    path(
        "auth/register/",
        RegisterView.as_view(),
        name="register"
    ),

    # Knowledge Base Query
    path(
        "kb/query/",
        QueryKBView.as_view(),
        name="kb-query"
    ),

    # Admin Usage Summary
    path(
        "admin/usage-summary/",
        UsageSummaryView.as_view(),
        name="usage-summary"
    ),

    path(
    "auth/login/",
    LoginView.as_view(),
    name="login"
),
]