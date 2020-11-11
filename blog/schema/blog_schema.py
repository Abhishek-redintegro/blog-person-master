import graphene
from graphene_django.types import DjangoObjectType
from blog.models import Blog as BlogModel
from django.utils import timezone


class Blog(DjangoObjectType):
    class Meta:
        model = BlogModel

# To create or insert new entry in blog table
class CreateBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for CreateBlog Classes mutation function
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        posted_by = graphene.String(required=True)

    blog = graphene.Field(Blog)

    def mutate(self, info, name, description, posted_by):
        '''
            mutate : return field object for blog table

                Args:
                    name : to insert data in name field
                    description : to insert data in description field
                    posted_by : to insert data in posted_by field
        '''
        
        # Creating object for Blog Class
        new_blog = BlogModel(
            name=name,
            description=description,
            posted_by=posted_by,
            posted_on=timezone.now()
        )
        new_blog.save()
        return CreateBlog(blog=new_blog)


# Update selected dat in blog Table
class UpdateBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for UpdateBlog Classes mutation function
        description = graphene.String(required=True)
        id = graphene.Int(required=True)

    message = graphene.String()

    def mutate(self, info, description, id):
        '''
            mutate : return string message for updated data in blog table

                Args:
                    id : to insert data in name field
                    description : to insert updated data in description field
        '''
        old_blog = BlogModel.objects.get(pk=id)
        old_desc = old_blog.description
        old_blog.description = description
        old_blog.save()
        return UpdateBlog(message=f'Old Description:{old_desc} New Description:{description} For Id:{id}')

# Delete the selected entry from blog table
class DeleteBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for DeleteBlog Classes mutation function
        id = graphene.Int(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        '''
            mutate : return string message for deleted data in blog table

                Args:
                    id : to delete all fields of id
                    
        '''
        old_blog = BlogModel.objects.get(pk=id)
        old_blog.delete()
        return DeleteBlog(message=f'Deleted Data For Id:{id}')

# ==============================Create Blog===================================
# mutation{         
#   createBlog(
#     description:"ReactJS",
#     name:"Learn Web development",
#     postedBy:"Rudula"
#   ){
#     blog{
#       id
#       description
#       postedBy
#       postedOn
#       name
#     }
#   }
# }

# ==============================Update Blog===================================
# mutation{
#   updateBlog(description:"Server Admin",id:3){
#     message
#   }
# }


# ==============================Delete Blog===================================
# mutation{
#   deleteBlog(id:4){
#     message
#   }
# }