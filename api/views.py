from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from .serializers import KBEntrySerializer
from django.db.models import Q
from django.db.models import Count
from .permissions import IsAdminUser
from .models import Company, KBEntry, QueryLog
from django.contrib.auth import authenticate

class RegisterView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        company_name = request.data.get("company_name")

        if not username:
            return Response(
                {"error": "Username is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not password:
            return Response(
                {"error": "Password is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not company_name:
            return Response(
                {"error": "Company name is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        company = user.company

        company.company_name = company_name
        company.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "username": user.username,
                "company_name": company.company_name,
                "api_key": company.api_key,
                "access": str(refresh.access_token)
            },
            status=status.HTTP_201_CREATED
        )
    
class QueryKBView(APIView):

    def post(self, request):

        search = request.data.get("search")

        if not search:
            return Response(
                {"error": "search required"},
                status=400
            )

        company = request.user.company

        with transaction.atomic():

            entries = KBEntry.objects.filter(
                Q(question__icontains=search)
                |
                Q(answer__icontains=search)
            )

            count = entries.count()

            QueryLog.objects.create(
                company=company,
                search_term=search,
                results_count=count
            )

        serializer = KBEntrySerializer(
            entries,
            many=True
        )

        return Response(
            {
                "search": search,
                "count": count,
                "results": serializer.data
            }
        )
    
class UsageSummaryView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        total_queries = QueryLog.objects.aggregate(
            total=Count("id")
        )

        active_companies = (
            QueryLog.objects
            .values("company")
            .distinct()
            .count()
        )

        top_search_terms = (
            QueryLog.objects
            .values("search_term")
            .annotate(count=Count("id"))
            .order_by("-count")[:5]
        )

        return Response(
            {
                "total_queries": total_queries["total"],
                "active_companies": active_companies,
                "top_search_terms": list(top_search_terms)
            }
        )

class LoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "company_name": user.company.company_name,
                "api_key": user.company.api_key
            }
        )