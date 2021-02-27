import json
from graphene_django.utils.testing import GraphQLTestCase

class QueryTests(GraphQLTestCase):

    def setUp(self):
        response = self.query(
            '''
            mutation {
                addCompany(name:"Flipkart", address:"Bangalore", ownerInfo:"Walmart", employeeSize:1000) {
                    company {
                        name
                        address
                        ownerInfo
                        employeeSize
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)

        response = self.query(
            '''
            mutation {
                addCompany(name:"Swisscom", address:"Switzerland", ownerInfo:"Swiss", employeeSize:10000) {
                    company {
                        name
                        address
                        ownerInfo
                        employeeSize
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)

    def test_search_by_name(self):
        response = self.query(
            '''
            query {
                searchByName(name:"Flipkart") {
                    name
                    address
                    ownerInfo
                    employeeSize
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Flipkart", "address":"Bangalore", "ownerInfo":"Walmart", "employeeSize":1000 },
            content['data']['searchByName'][0])

    def test_search_by_address(self):
        response = self.query(
            '''
            query {
                searchByAddress(address:"Switzerland") {
                    name
                    address
                    ownerInfo
                    employeeSize
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Swisscom", "address":"Switzerland", "ownerInfo":"Swiss", "employeeSize":10000 },
            content['data']['searchByAddress'][0])

    def test_search_by_onwer_info(self):
        response = self.query(
            '''
            query {
                searchByOwnerInfo(ownerInfo:"Swiss") {
                    name
                    address
                    ownerInfo
                    employeeSize
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Swisscom", "address":"Switzerland", "ownerInfo":"Swiss", "employeeSize":10000 },
            content['data']['searchByOwnerInfo'][0])

    def test_search_by_employee_size(self):
        response = self.query(
            '''
            query {
                searchByEmployeeSize(employeeSize:1000) {
                    name
                    address
                    ownerInfo
                    employeeSize
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Flipkart", "address":"Bangalore", "ownerInfo":"Walmart", "employeeSize":1000 },
            content['data']['searchByEmployeeSize'][0])

    
    def test_search_by_text(self):
        response = self.query(
            '''
            query {
                searchByText(text:"Bangal") {
                    name
                    address
                    ownerInfo
                    employeeSize
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Flipkart", "address":"Bangalore", "ownerInfo":"Walmart", "employeeSize":1000 },
            content['data']['searchByText'][0])

class MutationTests(GraphQLTestCase):

    def setUp(self):
        response = self.query(
            '''
            mutation {
                addCompany(name:"Flipkart", address:"Bangalore", ownerInfo:"Walmart", employeeSize:1000) {
                    company {
                        name
                        address
                        ownerInfo
                        employeeSize
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)

        response = self.query(
            '''
            mutation {
                addCompany(name:"Swisscom", address:"Switzerland", ownerInfo:"Swiss", employeeSize:10000) {
                    company {
                        name
                        address
                        ownerInfo
                        employeeSize
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)
    
    def test_add_company(self):
        response = self.query(
            '''
            mutation {
                addCompany(name:"Google", address:"US", ownerInfo:"Alphabet", employeeSize:50000) {
                    company {
                        name
                        address
                        ownerInfo
                        employeeSize
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Google", "address":"US", "ownerInfo":"Alphabet", "employeeSize":50000 },
            content['data']['addCompany']['company'])

    def test_update_company(self):
        response = self.query(
            '''
            mutation {
                updateCompany(id:1, name:"Zomato", ownerInfo:"Zomato") {
                    company {
                        name
                        address
                        ownerInfo
                        employeeSize
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {"name": "Zomato", "address":"Bangalore", "ownerInfo":"Zomato", "employeeSize":1000 },
            content['data']['updateCompany']['company'])

    def test_delete_company(self):
        response = self.query(
            '''
            mutation {
                deleteCompany(id:1) {
                    message
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(
            "deleted",
            content['data']['deleteCompany']['message'])


    