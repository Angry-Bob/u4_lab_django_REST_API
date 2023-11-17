from rest_framework import serializers
from .models import Team, Player, Conference

class ConferenceSerializer(serializers.ModelSerializer):
    conference = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )
    conference_id = serializers.PrimaryKeyRelatedField(
        queryset=Conference.objects.all(),
        source='conference'
    )
    
    class Meta:
        model = Conference
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )

    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(
        many=True,
        read_only=True
    )

    team_url = serializers.HyperlinkedIdentityField(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = '__all__'




