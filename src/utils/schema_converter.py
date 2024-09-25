
from src.schemas import book_schema
from src.graphql import schemas


def to_BookSchemagql(from_schema):

    # i used mode_dump to reduce to too many lines of mapping incase you are looking at this code
    # and you dont understand what is going on here
    # you can use mode_dump to reduce the number of lines of mapping
    # but model_dump is a pydantic function not available for strawberry schema
    # it works oh no scatter my code oh
    temp : dict= from_schema.model_dump()

    return  schemas.BookSchemagql(
                    **temp
                ) 


def to_BookSchema(from_schemagql):
    return book_schema.BookSchema(
            title=str(from_schemagql.title),
            author=str(from_schemagql.author),
            publisher=str(from_schemagql.publisher),
            published_date=str(from_schemagql.published_date),
            page_count=int(from_schemagql.page_count), # type: ignore
            language=str(from_schemagql.language)
    )

def to_UpdateSchema(from_schemagql):

    return book_schema.BookUpdateSchema(
            title=from_schemagql.title,
            author=from_schemagql.author,
            publisher=from_schemagql.publisher,
            page_count=from_schemagql.page_count,
            language=from_schemagql.language
    )