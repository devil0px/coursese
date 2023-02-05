
from rest_framework import serializers
from .models import Courses


class coursesSerilizers(serializers.ModelSerializer):

    class Meta:
        model =Courses
        fields ='__all__'

