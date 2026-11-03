from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from learnapp.models import CourseDb, EnrollmentDb
from learnapp.serializers import CourseSerializer, EnrollmentSerializer

# Course List and Create

class CourseListCreateView(APIView):

    def get(self, request):
        qs = CourseDb.objects.all()
        serializer_instance = CourseSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = CourseSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            CourseDb.objects.create(**actual_data)

            return Response({
                'message': 'Course created successfully'
            })

        else:
            return Response({
                'errors': serializer_instance.errors
            })
class CourseRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(CourseDb, id=pk)
        serializer_instance = CourseSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        qs = get_object_or_404(CourseDb, id=pk)

        form_data = request.data
        serializer_instance = CourseSerializer(
            qs, data=form_data
        )

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            serializer_instance.save()

            return Response({
                'message': 'Course updated successfully'
            })

        else:
            return Response({
                'errors': serializer_instance.errors
            })

    def delete(self, request, pk):
        qs = get_object_or_404(CourseDb, id=pk)
        qs.delete()

        return Response({
            'message': 'Course deleted successfully'
        })
class EnrollmentListCreateView(APIView):
    def get(self, request):
        qs = EnrollmentDb.objects.all()
        serializer_instance = EnrollmentSerializer(
            qs, many=True)
        return Response(data=serializer_instance.data)
    def post(self, request):
        form_data = request.data
        serializer_instance = EnrollmentSerializer(
            data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            EnrollmentDb.objects.create(**actual_data)
            return Response({
                'message': 'Enrollment created successfully'
            })

        else:
            return Response({
                'errors': serializer_instance.errors
            })


# Enrollment Retrieve, Update and Delete

class EnrollmentRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(EnrollmentDb, id=pk)
        serializer_instance = EnrollmentSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        qs = get_object_or_404(EnrollmentDb, id=pk)

        form_data = request.data
        serializer_instance = EnrollmentSerializer(
            qs, data=form_data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                'message': 'Enrollment updated successfully'
            })

        else:
            return Response({
                'errors': serializer_instance.errors
            })

    def delete(self, request, pk):
        qs = get_object_or_404(EnrollmentDb, id=pk)
        qs.delete()

        return Response({
            'message': 'Enrollment deleted successfully'
        })
