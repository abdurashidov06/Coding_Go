from rest_framework import serializers

from education.models import Group


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'image','title','course','student','teacher','start_date','end_date')


class GroupRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('image','title','course','student','teacher','start_date','end_date')

class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('image','title','course','student','teacher','start_date','end_date')


class GroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('image','title','course','student','teacher','start_date','end_date')

    def update(self,instance,validated_data):
        instance.image = validated_data.get('image',instance.image)
        instance.title = validated_data.get('title',instance.title)
        instance.student = validated_data.get('student',instance.student)
        instance.teacher = validated_data.get('teacher',instance.teacher)
        instance.end_date = validated_data.get('end_date',instance.end_date)
        instance.save()
        return instance



