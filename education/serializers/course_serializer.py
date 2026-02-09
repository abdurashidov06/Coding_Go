from django.shortcuts import render
from rest_framework import serializers

from education.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',
                  'image',
                  'title',
                  'description',
                  'price')
        read_only_fields = ('id',)

class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('image',
                  'title',
                  'description',
                  'price')

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('image',
                  'title',
                  'description',
                  'price')

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Narx noldan past bo'lmasin")
        return value




class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('image',
                  'title',
                  'description',
                  'price')

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance





# class CourseDeleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('id',)



