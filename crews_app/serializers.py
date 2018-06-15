from rest_framework import serializers
from airplanes_app.models import Lot, Zaloga
from time import strftime

class ZalogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zaloga
        fields = ('id', 'imie_i_nazwisko_kapitana')
        read_only_fields = ('id', 'imie_i_nazwisko_kapitana')

class LotSerializer(serializers.ModelSerializer):
    czas_startu = serializers.DateTimeField('%d-%m-%Y %H:%M')
    czas_ladowania = serializers.DateTimeField('%d-%m-%Y %H:%M')
    
    class Meta:
        model = Lot
        fields = ('id', 'lotnisko_startowe', 'czas_startu', 'lotnisko_docelowe', 'czas_ladowania', 'zaloga')
        read_only_fields = ('id', 'lotnisko_startowe', 'czas_startu', 'lotnisko_docelowe', 'czas_ladowania')
        depth = 1
