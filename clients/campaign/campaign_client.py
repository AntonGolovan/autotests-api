from httpx import Response
from clients.api_client import APIClient
from clients.campaign.models.campaign_schema import (
    CreateCampaignRequestSchema,
    UpdateCampaignResponseSchema,
    CreateCampaignResponseSchema,
    UpdateCampaignRequestSchema,
)
from clients.client_builder import get_http_client_builder


class CampaignClient(APIClient):
    """
    Клиент для работы с API кампаний.
    Предоставляет методы для создания, получения и обновления кампаний.
    """

    def get_campaign_api(self, campaign_id: str) -> Response:
        """
        Получает информацию о кампании по её ID.

        :param campaign_id: Идентификатор кампании.
        :return: Объект Response с данными кампании.
        """
        return self.get(url=f"/v1/campaigns/item?id={campaign_id}")

    def create_campaign_api(self, request: CreateCampaignRequestSchema) -> Response:
        """
        Создаёт новую кампанию.

        :param request: Данные для создания кампании.
        :return: Объект Response с данными созданной кампании.
        """
        return self.post(url=f"/v1/campaigns/item", json=request.model_dump())

    def update_campaign_api(self, campaign_id: str, request: UpdateCampaignRequestSchema) -> Response:
        """
        Обновляет существующую кампанию.

        :param campaign_id: Идентификатор кампании.
        :param request: Данные для обновления кампании.
        :return: Объект Response с данными обновлённой кампании.
        """
        return self.patch(url=f"v1/campaigns/{campaign_id}", json=request.model_dump())

    def create_campaign(self, request: CreateCampaignRequestSchema) -> CreateCampaignResponseSchema:
        """
        Создаёт новую кампанию и возвращает её данные в виде модели Pydantic.

        :param request: Данные для создания кампании.
        :return: Объект CreateCampaignResponseSchema с данными созданной кампании.
        """
        response = self.create_campaign_api(request=request)
        return CreateCampaignResponseSchema.model_validate_json(response.text)

def get_campaign_client() -> CampaignClient:
    return CampaignClient(client=get_http_client_builder())
