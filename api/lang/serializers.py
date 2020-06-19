from rest_framework import serializers
from .models import lang


class langserializer(serializers.ModelSerializer):
    class Meta:
          model=lang
          fields=('id','name')
          
    
     
 