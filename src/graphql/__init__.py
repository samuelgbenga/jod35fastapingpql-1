from fastapi import Depends
import strawberry

from strawberry.fastapi import GraphQLRouter

from src.auth.dependencies import IsAuthenticated




from .schemas import BookSchemagql, DeleteBookResponse, LoginResponsegql, Usergql

from .resolver import QueryResolver, MutationResolver

from typing import List, Sequence




@strawberry.type
class Query:
    books: List[BookSchemagql] | None = strawberry.field(resolver=QueryResolver.get_books, permission_classes=[IsAuthenticated])
    users: List[Usergql] | None = strawberry.field(resolver=QueryResolver.get_all_users)
    book:  BookSchemagql | None = strawberry.field(resolver=QueryResolver.get_book, permission_classes=[IsAuthenticated])


@strawberry.type
class Mutation:
    add_book: BookSchemagql|None = strawberry.field(resolver=MutationResolver.add_book, permission_classes=[IsAuthenticated])
    update_book: BookSchemagql|None  = strawberry.field(resolver=MutationResolver.update_book, permission_classes=[IsAuthenticated])
    delete_book: DeleteBookResponse = strawberry.field(resolver=MutationResolver.delete_book, permission_classes=[IsAuthenticated])
    add_user: Usergql|None = strawberry.field(resolver=MutationResolver.add_user)
    login_user: LoginResponsegql | None = strawberry.field(resolver=MutationResolver.login_user)


schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQLRouter(schema)
