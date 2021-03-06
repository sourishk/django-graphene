# This file contains all graphene mutations.
import graphene
from django.core.exceptions import ObjectDoesNotExist
from company.models import Company
from .types import CompanyType

'''
Graphene mutation class to create a company.
'''
class CreateCompanyMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(default_value="Lane 1")
        owner_info = graphene.String(default_value="The true owner")
        employee_size = graphene.Int(default_value=0)

    company = graphene.Field(CompanyType)

    @classmethod
    def mutate(cls, root, info, name, address, owner_info, employee_size):
        company = Company()
        company.name = name
        company.address = address
        company.owner_info = owner_info
        company.employee_size = employee_size
        company.save()
        return CreateCompanyMutation(company=company)

'''
Graphene mutation class to update a company.
'''
class UpdateCompanyMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()
        owner_info = graphene.String()
        employee_size = graphene.Int()
        id = graphene.ID(required=True)

    company = graphene.Field(CompanyType)
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        address = kwargs.get('address')
        owner_info = kwargs.get('owner_info')
        employee_size = kwargs.get('employee_size')

        if all(v is None for v in [name, address, owner_info, employee_size]):
            return UpdateCompanyMutation(message="Update atleast one field")

        try:
            company = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            return UpdateCompanyMutation(message="Invalid 'id' passed")
        if name is not None:
            company.name = name

        if address is not None:
            company.address = address
        
        if owner_info is not None:
            company.owner_info = owner_info
        
        if employee_size is not None:
            company.employee_size = employee_size

        company.save()
        return UpdateCompanyMutation(company=company)


'''
Graphene mutation class to delete a company.
'''
class DeleteCompanyMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            company = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            return UpdateCompanyMutation(message="Invalid 'id' passed")

        Company.delete(company)
        # Notice we return an instance of this mutation
        return DeleteCompanyMutation(message='deleted')


'''
This class defines all graphene mutations.
'''
class Mutation(graphene.ObjectType):
    add_company = CreateCompanyMutation.Field()
    update_company = UpdateCompanyMutation.Field()
    delete_company = DeleteCompanyMutation.Field()