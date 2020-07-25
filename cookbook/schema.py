import graphene

from ingredients.schema import Query as Qry


class Query(Qry, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)