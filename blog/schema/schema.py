import graphene
from blog.schema.blog_schema import BlogModel, Blog, CreateBlog, UpdateBlog, DeleteBlog


class Query(graphene.ObjectType):
    allBlogs = graphene.List(Blog)
    blog = graphene.Field(Blog, id=graphene.Int(required=True))

    def resolve_allBlogs(self, info):
        '''
            resolve_allBlogs : returns all blog's data as a List
        '''
        return BlogModel.objects.all()

    def resolve_blog(self,info,id):
        '''
            resolve_blog : returns data of id passed as argument
                Args:
                    id : int
        '''
        return BlogModel.objects.get(pk=id)
    

class Mutations(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()
    delete_blog = DeleteBlog.Field()