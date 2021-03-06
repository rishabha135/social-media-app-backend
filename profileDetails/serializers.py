from rest_framework import serializers
from .models import AccountDetail
from authentication.serializers import AccountSerializer


class AccountDetailSerializer(serializers.ModelSerializer):
    # account key commented out for now
    class Meta:
        model = AccountDetail
        fields = ['id', 'fname', 'lname', 'bio',
                  'score', 'created', 'Account_foreignkey']
