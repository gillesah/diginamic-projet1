from pydantic import BaseModel

class ClientSchema(BaseModel):
    nom_client: str
    prenom_client: str
    email_client: str
    telephone_client: str | None = None
    preferences_client: str | None = None
    adresse_livraison_client: str | None = None
    adresse_facturation_client: str | None = None
    
    class Config:
        # orm_mode = True
        from_attributes = True

class ClientSchemaIn(ClientSchema):
    pass

class ClientSchemaOut(ClientSchema):
    id_client: int