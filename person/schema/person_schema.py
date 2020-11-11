import graphene
from graphene_django.types import DjangoObjectType
from person.models import Person as PersonModel

class Person(DjangoObjectType):
    class Meta:
        model = PersonModel
        

# To create or insert new entry in person table
class CreatePerson(graphene.Mutation):
    class Arguments:
        # The input arguments for CreatePerson Classes mutation function
        u_name = graphene.String(required=True)
        u_desc = graphene.String(required=True)
        u_phone_no = graphene.String(required=True)
        u_email = graphene.String(required=True)
        u_password = graphene.String(required=True)

    person = graphene.Field(Person)

    def mutate(self, info, u_name, u_desc, u_phone_no, u_email, u_password):
        '''
            mutate : return field object for person table

                Args:
                    u_name : to insert data in name field
                    u_desc : to insert data in description field
                    u_phone_no : to insert data in phone number field
                    u_email : to insert data in email address field
                    u_password : to insert data in password field

        '''
        # Creating objec for Person class
        new_person = PersonModel(
            u_name=u_name,
            u_desc=u_desc,
            u_phone_no=u_phone_no,
            u_email=u_email,
            u_password=u_password
        )
        new_person.save()
        return CreatePerson(person=new_person)

# Update selected dat in person Table
class UpdatePerson(graphene.Mutation):
    class Arguments:
        # The input arguments for UpdatePerson Classes mutation function
        u_email = graphene.String(required=True)
        id = graphene.Int(required=True)
    
    message = graphene.String()

    def mutate(self,info,u_email,id):
        '''
            mutate : return string message for updated data in person table

                Args:
                    id : to insert data in name field
                    u_email : to insert updated data in email field
        '''
        old_person = PersonModel.objects.get(pk=id)
        old_email = old_person.u_email
        old_person.u_email = u_email
        old_person.save()
        return UpdatePerson(message=f'Old Email:{old_email} New Email:{u_email} For Id:{id}')

# Delete the selected entry from person table
class DeletePerson(graphene.Mutation):
    class Arguments:
        # The input arguments for DeletePerson Classes mutation function
        id = graphene.Int(required=True)

    message = graphene.String()

    def mutate(self,info,id):
        '''
            mutate : return string message for deleted data in person table

                Args:
                    id : to delete all fields of id
        '''
        old_person = PersonModel.objects.get(pk=id)
        old_person.delete()
        return DeletePerson(message=f'Deleted Data For Id:{id}')


# ==============================Create Blog===================================
# mutation{
#   createPerson(
#     uDesc:"Regular",
#     uEmail:"Rudu@gmail.com",
#     uName:"Rudula",
#     uPassword:"RKSA@!1212",
#     uPhoneNo:"9325485753"
#   )
#   {
#     person{
#       id
#       uName
#       uDesc
#       uPhoneNo
#       uEmail
#       uPassword
#     }
#   }
# }

# ==============================Update Blog===================================
# mutation{
#   updatePerson(id:2, uEmail:"Sanjanakgodse@gmail.com"){
#     message
#   }
# }


# ==============================Delete Blog===================================
# mutation{
#   deletePerson(id:3)
#   {
#     message
#   }
# }