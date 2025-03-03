# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckView(APIView):
    """Health check endpoint for CapRover monitoring"""
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        return Response(
            {"status": "healthy", "service": "django-api"},
            status=status.HTTP_200_OK
        )

class IndexView(APIView):
    """Root endpoint that provides API information"""
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        api_info = {
            "name": "Django API",
            "version": "1.0.0",
            "description": "A simple Django REST API",
            "endpoints": {
                "health_check": "/api/health/"
            }
        }
        return Response(api_info)
