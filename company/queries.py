# This file contains all graphene queries.
import graphene
from django.forms.models import model_to_dict
from company.models import Company
from .types import CompanyType


'''
This class defines all graphene queries.
'''
class Query(graphene.ObjectType):
    # A helper query to get a list of all companies.
    all_companies = graphene.List(CompanyType)
    # Query to filter companies by id.
    seach_by_id = graphene.List(CompanyType, id=graphene.ID(required=True))
    # Query to filter companies by name.
    search_by_name = graphene.List(CompanyType, name=graphene.String(required=True))
    # Query to filter companies by address.
    search_by_address = graphene.List(CompanyType, address=graphene.String(required=True))
    # Query to filter companies by owner info.
    search_by_owner_info = graphene.List(CompanyType, owner_info=graphene.String(required=True))
    # Query to filter companies by employee size.
    search_by_employee_size = graphene.List(CompanyType, employee_size=graphene.Int(required=True))
    # Query to do a text search.
    search_by_text = graphene.List(CompanyType, text=graphene.String(required=True))

    def resolve_all_companies(root, info):
        return Company.objects.all()

    def resolve_seach_by_id(root, info, id):
         return Company.objects.filter(id=id)

    def resolve_search_by_name(root, info, name):
        return Company.objects.filter(name=name)

    def resolve_search_by_address(root, info, address):
        return Company.objects.filter(address=address)

    def resolve_search_by_owner_info(root, info, owner_info):
        return Company.objects.filter(owner_info=owner_info)
    
    def resolve_search_by_employee_size(root, info, employee_size):
        return Company.objects.filter(employee_size=employee_size)
    
    def resolve_search_by_text(root, info, text):
        all_companies = Company.objects.all()
        companies = []
        for company in all_companies:
            dic = model_to_dict(company)
            for k,v in dic.items():
                if text in str(v):
                    companies.append(company)
                    break

        return companies