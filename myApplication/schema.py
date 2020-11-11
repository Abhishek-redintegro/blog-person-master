import graphene
import blog.schema.schema as Blog
import person.schema.schema as Person


class Query(Blog.Query, Person.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Mutations(Blog.Mutations,Person.Mutations,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
