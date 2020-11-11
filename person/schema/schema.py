import graphene
from person.schema.person_schema import PersonModel, Person, CreatePerson, DeletePerson, UpdatePerson


class Query(graphene.ObjectType):
    allPersons = graphene.List(Person)
    person = graphene.Field(Person, id=graphene.Int(required=True))

    def resolve_allPersons(self, info):
        '''
            resolve_allPersons : returns all person's data as a List
        '''
        return PersonModel.objects.all()

    def resolve_person(self, info, id):
        '''
            resolve_person : returns data of id passed as argument
                Args:
                    id : int
        '''
        return PersonModel.objects.get(pk=id)


class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()