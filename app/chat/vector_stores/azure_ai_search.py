import os
from langchain_community.vectorstores.azuresearch import AzureSearch
from azure.search.documents.indexes.models import (
    SemanticSettings,
    SemanticConfiguration,
    PrioritizedFields,
    SemanticField
)
from app.chat.embeddings.openai import embeddings
from app.chat.models import ChatArgs


vector_store_address: str = os.getenv("AZURE_AI_SEARCH_URL")
vector_store_password: str = os.getenv("AZURE_AI_SECRET_KEY")

index_name: str = "langchain-vector-demo"
vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=vector_store_password,
    index_name=index_name,
    embedding_function=embeddings.embed_query,
    semantic_configuration_name='config',
        semantic_settings=SemanticSettings(
            default_configuration='config',
            configurations=[
                SemanticConfiguration(
                    name='config',
                    prioritized_fields=PrioritizedFields(
                        title_field=SemanticField(field_name='content'),
                        prioritized_content_fields=[SemanticField(field_name='content')],
                        prioritized_keywords_fields=[SemanticField(field_name='metadata')]
                    ))
            ])
    )

def build_retriever(chat_args: ChatArgs):
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}}
    if vector_store:
        return vector_store.as_retriever(search_kwargs=search_kwargs)