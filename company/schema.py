import graphene
from graphene_django import DjangoObjectType
from company.models import Company
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = ( 'id', 'name', 'address', 'owner_info', 'employee_size')

class Query(graphene.ObjectType):
    all_companies = graphene.List(CompanyType)
    seach_by_id = graphene.List(CompanyType, id=graphene.ID(required=True))
    search_by_name = graphene.List(CompanyType, name=graphene.String(required=True))
    search_by_address = graphene.List(CompanyType, address=graphene.String(required=True))
    search_by_owner_info = graphene.List(CompanyType, owner_info=graphene.String(required=True))
    search_by_employee_size = graphene.List(CompanyType, employee_size=graphene.Int(required=True))
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

class Mutation(graphene.ObjectType):
    add_company = CreateCompanyMutation.Field()
    update_company = UpdateCompanyMutation.Field()
    delete_company = DeleteCompanyMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)