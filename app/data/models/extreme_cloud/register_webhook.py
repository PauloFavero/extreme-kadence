from pydantic import BaseModel

class WebhookSubscritionData(BaseModel):
    application: str
    url: str
    secret: str
    message_type: str