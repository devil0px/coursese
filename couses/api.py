# -*- coding: utf-8 -*-
from .models import Course
from .serializers import coursesSerilizers
from django_filters.rest_framework import DjangoFilterBackend
#from starterkit.drf.permissions import IsAuthenticatedAndIsActivePermission
from django.conf.urls import url, include
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import filters
from rest_framework import generics
from rest_framework import authentication, viewsets, permissions, status
from rest_framework.response import Response
# from tenant_api.pagination import StandardResultsSetPagination
# from tenant_api.permissions.course import (
#    CanListCreateCoursePermission,
#    CanRetrieveUpdateDestroyCoursePermission
# )
#from tenant_api.serializers.course_serializers import (
   # CourseListCreateSerializer,
    #CourseRetrieveUpdateDestroySerializer
#)
#from tenant_foundation.models import Course


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseListCreateSerializer
    # pagination_class = StandardResultsSetPagination
    permission_classes = (
        permissions.IsAuthenticated,
        #TODO: IsOwner Permission
        # IsAuthenticatedAndIsActivePermission,
        # CanListCreateCoursePermission
    )
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'sub_title', 'category_text', 'description',)

    def get_queryset(self):
        """
        List
        """
        queryset = Course.objects.all().order_by('-created_at')
        return queryset

    def post(self, request, format=None):
        """
        Create
        """
        serializer = CourseListCreateSerializer(data=request.data, context={
            'created_by': request.user,
            'academy': request.tenant
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class coursesView(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = coursesSerilizers