from mongoengine import Document, fields


class DocumentModel(Document):
    text = fields.StringField(required=True)
    embedding = fields.ListField(fields.FloatField(), required=True)

    meta = {
        "collection": "documents",
        "indexes": [
            {
                "fields": ["embedding"],
                "name": "embedding_index",
            }
        ],
    }
