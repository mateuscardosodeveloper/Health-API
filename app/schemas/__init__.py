from pydantic import BaseModel, Extra


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        extra = Extra.allow
