import strawberry

from strawberry.fastapi import GraphQLRouter


from .schemas import BookSchemagql, DeleteBookResponse, Usergql

from .resolver import QueryResolver, MutationResolver

from typing import List, Sequence



@strawberry.type
class Query:
    books: List[BookSchemagql] | None = strawberry.field(resolver=QueryResolver.get_books)
    users: List[Usergql] | None = strawberry.field(resolver=QueryResolver.get_all_users)
    book:  BookSchemagql | None = strawberry.field(resolver=QueryResolver.get_book)


@strawberry.type
class Mutation:
    add_book: BookSchemagql|None = strawberry.field(resolver=MutationResolver.add_book)
    update_book: BookSchemagql|None  = strawberry.field(resolver=MutationResolver.update_book)
    delete_book: DeleteBookResponse = strawberry.field(resolver=MutationResolver.delete_book)
    add_user: Usergql|None = strawberry.field(resolver=MutationResolver.add_user)



# addition
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)