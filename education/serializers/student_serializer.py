from rest_framework import serializers

from education.models import Student


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('image','first_name','last_name','phone','email','id_card')