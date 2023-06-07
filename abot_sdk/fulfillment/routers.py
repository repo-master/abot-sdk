
from fastapi import APIRouter, Request
from starlette.routing import Router, Route

from abot_sdk.__version__ import __version__ as PROTOCOL_VERSION
from .schemas import FulfillmentRouter, AbotAPIEndpoint, AbotAPIProvider, AbotFulfillmentQuery

from functools import lru_cache
from contextlib import suppress
from typing import List


class AbotFulfillmentAPI(APIRouter):
    def __init__(self,
                 *fulfillments: FulfillmentRouter,
                 app_class: str = "stub",
                 friendly_name: str = "Abot Fulfillment",
                 description: str = "Abot fulfillment stub",
                 version: str = "1.0.0",
                 prefix: str = '/abot', **kwargs):
        super().__init__(prefix=prefix, **kwargs)
        self._fulfillments: List[FulfillmentRouter] = list(fulfillments)

        self._app_class = app_class
        self._friendly_name = friendly_name
        self._description = description
        self._version = version

        self.add_api_route("", self.query_fulfillment_details)

    @staticmethod
    def _generate_provider_list(fulfillments: List[FulfillmentRouter], app_router: Router) -> List[AbotAPIProvider]:
        def find_route_in_app(route: Route) -> Route:
            with suppress(ValueError, IndexError):
                return app_router.routes[app_router.routes.index(route)]
            return route

        return [
            AbotAPIProvider(
                service_name=fulfillment.service_name,
                capabilities=[
                    AbotAPIEndpoint.from_orm(find_route_in_app(route))
                    for route in fulfillment.router.routes
                ]
            )
            for fulfillment in fulfillments
        ]

    async def query_fulfillment_details(self, request: Request) -> AbotFulfillmentQuery:
        '''Abot fulfillment API query'''
        return {
            "protocol": {
                "version": PROTOCOL_VERSION
            },
            "app_class": self._app_class,
            "friendly_name": self._friendly_name,
            "description": self._description,
            "version": self._version,
            "services": self._generate_provider_list(self._fulfillments, request.app.router)
        }
