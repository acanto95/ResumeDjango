# api/serializers.py

from rest_framework import serializers
from .models import MainInfo
from .models import ExperienceInfo
from .models import SkillsInfo
from .models import ProyectsInfo
from .models import Comments

class MainInfoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MainInfo
        fields = ('id', 'name', 'birthday', 'adress','phonenum')


class ExperienceInfoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ExperienceInfo
        fields = ('id', 'company','position', 'dates', 'description')

class SkillsInfoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = SkillsInfo
        fields = ('id', 'technology', 'timeskill')


class ProyectsInfoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ProyectsInfo
        fields = ('id', 'proyectname', 'positionproy', 'descriptionproy','techinvolved')


class CommentsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Comments
        fields = ('id', 'commentname', 'comment', 'date_created')