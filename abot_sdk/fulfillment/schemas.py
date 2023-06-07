
from fastapi import APIRouter
from pydantic import BaseModel

from typing import List, NamedTuple


FulfillmentRouter = NamedTuple("FulfillmentRouter", service_name=str, router=APIRouter)


class AbotAPIProtocol(BaseModel):
    version: str


class AbotAPIEndpoint(BaseModel):
    name: str
    path: str
    methods: List[str]

    class Config:
        orm_mode = True


class AbotAPIProvider(BaseModel):
    service_name: str
    capabilities: List[AbotAPIEndpoint] = []


class AbotFulfillmentQuery(BaseModel):
    protocol: AbotAPIProtocol
    app_class: str
    friendly_name: str
    description: str
    version: str
    services: List[AbotAPIProvider]

    class Config:
        orm_mode = True


__all__ = [
    'FulfillmentRouter',
    'AbotAPIProtocol',
    'AbotAPIEndpoint',
    'AbotAPIProvider',
    'AbotFulfillmentQuery'
]
