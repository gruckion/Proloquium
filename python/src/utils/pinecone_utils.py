"""Pinecone utility class for creating and connecting to Pinecone indexes."""

import pinecone

from common.config import settings


class PineconeUtils:
    """
    Pinecone utility class for creating and connecting to Pinecone indexes.
    """

    def __init__(self, table_name: str, objective: str):
        print("Initializing Pinecone utils...")
        self.table_name = table_name
        self.objective = objective
        self._init_pinecone()

    def _init_pinecone(self):
        pinecone.init(
            api_key=settings.PINECONE_API_KEY,
            environment=settings.PINECONE_ENVIRONMENT,
        )

        # Create Pinecone index
        dimension = 1536
        metric = "cosine"
        pod_type = "p1"
        if self.table_name not in pinecone.list_indexes():
            pinecone.create_index(
                self.table_name,
                dimension=dimension,
                metric=metric,
                pod_type=pod_type,
            )

        # Connect to the index
        self.index = pinecone.Index(self.table_name)

    # Add other Pinecone utility methods here
