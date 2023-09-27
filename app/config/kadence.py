from pydantic import (
    AliasChoices,
    Field
)
from pydantic_settings import BaseSettings

class KadenceSettings(BaseSettings):
    identifier: str = Field(
        None,
        alias="kadence_identifier",
        validation_alias=AliasChoices(
            "kadence_api_key", "kadence_key", "kadence_id", "kadence_identifier"
        ),
    )
    secret: str = Field(
        None,
        alias="kadence_secret",
        validation_alias=AliasChoices("kadence_secret", "kadence_auth"),
    )
    username: str = Field(
        None,
        alias="kadence_username",
        validation_alias=AliasChoices("kadence_username", "kadence_user"),
    )
    password: str = Field(
        None,
        alias="kadence_password",
        validation_alias=AliasChoices("kadence_password", "kadence_pass"),
    )

    base_uri: str = Field(
        "https://api.onkadence.co",
        alias="kadence_base_uri",
        validation_alias=AliasChoices("kadence_base_uri", "kadence_base_url"),
    )

    api_version: str = Field(
        "/v1/public",
        alias="kadence_api_version",
        validation_alias=AliasChoices("kadence_api_version", "kadence_version"),
    )

    login_endpoint: str = Field(
        "https://login.onkadence.co/oauth2/token",
        alias="kadence_login_endpoint",
        validation_alias=AliasChoices("kadence_login_endpoint",
                                      "kadence_login_uri",
                                      "kadence_login_url")
    )


