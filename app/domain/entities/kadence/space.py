
from pydantic import BaseModel


class Neighborhood(BaseModel):
    id: str
    name: str
    # "@id": "/v1/public/neighborhoods/01H9TG9Z73XS6YZCC1CGTSDQFK",
    # "@type": "Neighborhood",
    # "id": "01H9TG9Z73XS6YZCC1CGTSDQFK",
    # "name": "Engineering"
        

class Floor(BaseModel):
        id: str
        name: str
        #   "@id": "/v1/public/floors/01H9TG9Z6K07RY2S5NSPZ6R37Y",
        #   "@type": "Floor",
        #   "id": "01H9TG9Z6K07RY2S5NSPZ6R37Y",
        #   "name": "Ground floor"


class Space(BaseModel):
    id: str
    name: str
    type: str
    floor: Floor
    neighborhood: Neighborhood