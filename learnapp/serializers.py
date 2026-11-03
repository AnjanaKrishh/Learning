from rest_framework import serializers
from learnapp.models import CourseDb, EnrollmentDb
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDb
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentDb
        fields = '__all__'

    def validate(self, validated_data):
        course_id = validated_data.get('course_id')

        if not CourseDb.objects.filter(
            id=course_id, is_active=True
        ).exists():
            raise serializers.ValidationError(
                "Course does not exist or is inactive.")

        email = validated_data.get('student_email')

        if EnrollmentDb.objects.filter(
            course_id=course_id,
            student_email=email
        ).exists():
            raise serializers.ValidationError(
                "Student already enrolled in this course.")
            return validated_data