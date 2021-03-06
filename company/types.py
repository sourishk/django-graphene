# This file contains all Graphene Type definitions.
from company.models import Company
from graphene_django import DjangoObjectType


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = ( 'id', 'name', 'address', 'owner_info', 'employee_size')