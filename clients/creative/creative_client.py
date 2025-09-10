from typing import List

from httpx import Response
from clients.api_client import APIClient
from clients.client_builder import get_http_client_builder
from clients.creative.models.creative_schema import (
    CreateCreativeMapRequestSchema,
    CreateCreativeMapResponseSchema,
    CreateCreativeCmsRequestSchema,
    GetCreativeMapListResponseSchema,
)


class CreativeClient(APIClient):
    """
    Клиент для работы с API креативов.
    Предоставляет методы для создания и управления креативами и картами креативов.
    """

    def get_creatives_maps_api(self, campaign_id: int) -> Response:
        """
        Получает список карт креативов для кампании через API.

        :param campaign_id: Идентификатор кампании.
        :return: Объект Response с данными карт креативов.
        """
        return self.patch(url=f"/v1/campaigns/{campaign_id}/creative_request")

    def create_creative_cms_api(self, request: CreateCreativeCmsRequestSchema) -> Response:
        """
        Создаёт новый креатив в CMS через API.

        :param request: Данные для создания креатива.
        :return: Объект Response с данными созданного креатива.
        """
        return self.post(url=f"/v3/creatives/create", json=request.model_dump())

    def create_creative_map_api(self, campaign_id: int, request: CreateCreativeMapRequestSchema) -> Response:
        """
        Создаёт новую карту креативов для кампании через API.

        :param campaign_id: Идентификатор кампании.
        :param request: Данные для создания карты креативов.
        :return: Объект Response с данными созданной карты.
        """
        return self.post(url=f"/v1/campaigns/{campaign_id}/creative_request", json=request.model_dump())

    def get_creative_maps_api(self, campaign_id: int) -> Response:
        """
        Получает список карт креативов для кампании через API.

        :param campaign_id: Идентификатор кампании.
        :return: Объект Response с данными карт креативов.
        """
        return self.get(url=f"/v1/campaigns/{campaign_id}/creative_request")

    def get_creative_maps(self, campaign_id: int) -> GetCreativeMapListResponseSchema:
        """
        Получает список карт креативов для кампании и преобразует их в модель Pydantic.

        :param campaign_id: Идентификатор кампании.
        :return: Объект GetCreativeMapListResponseSchema со списком карт креативов.
        """
        response = self.get_creative_maps_api(campaign_id=campaign_id)
        return GetCreativeMapListResponseSchema.model_validate_json(response.text)

    def create_creative_map(self, campaign_id: int, request: CreateCreativeMapRequestSchema) -> CreateCreativeMapResponseSchema:
        """
        Создаёт новую карту креативов для кампании и возвращает её данные в виде модели Pydantic.

        :param campaign_id: Идентификатор кампании.
        :param request: Данные для создания карты креативов.
        :return: Объект CreateCreativeMapResponseSchema с данными созданной карты.
        """
        response = self.create_creative_map_api(campaign_id=campaign_id, request=request)
        return CreateCreativeMapResponseSchema.model_validate_json(response.text)

    def create_creative_cms(self, request: CreateCreativeCmsRequestSchema) -> CreateCreativeCmsRequestSchema:
        """
        Создаёт новый креатив в CMS и возвращает его данные в виде модели Pydantic.

        :param request: Данные для создания креатива.
        :return: Объект CreateCreativeCmsRequestSchema с данными созданного креатива.
        """
        response = self.create_creative_cms_api(request=request)
        return CreateCreativeCmsRequestSchema.model_validate_json(response.text)


def get_creative_client() -> CreativeClient:
    return CreativeClient(client=get_http_client_builder())
