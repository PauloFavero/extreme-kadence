from pydantic import BaseModel


class WebhookSubscritionData(BaseModel):
    """Webhook Subscription Data Model"""

    application: str
    url: str
    secret: str
    message_type: str
