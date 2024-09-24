
from src.schemas import book_schema
from src.graphql import schemas


def to_BookSchemagql(from_schema):

    return  schemas.BookSchemagql(
                    uid=from_schema.uid,
                    title=from_schema.title,
                    author=from_schema.author,
                    publisher=from_schema.publisher,
                    published_date=from_schema.published_date,
                    page_count=from_schema.page_count,
                    language=from_schema.language,
                    created_at=from_schema.created_at,
                    updated_at=from_schema.updated_at
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