import pytest
from pydantic import BaseModel
from clients.campaign.campaign_client import get_campaign_client, CampaignClient
from clients.campaign.models.campaign_schema import (
    CreateCampaignRequestSchema,
    CreateCampaignResponseSchema,
)


class CampaignFixture(BaseModel):
    """
    Фикстура для работы с кампаниями в тестах.
    Содержит данные запроса и ответа при создании кампании.
    """
    request: CreateCampaignRequestSchema  # Данные запроса на создание кампании
    response: CreateCampaignResponseSchema  # Данные ответа с созданной кампанией

    @property
    def campaign_id(self) -> int:
        """
        Получает ID созданной кампании.

        :return: Идентификатор кампании.
        """
        return self.response.id

    @property
    def planned_channel(self) -> list[str]:
        """
        Получает список запланированных каналов коммуникации.

        :return: Список каналов коммуникации.
        """
        return self.request.planned_channels


@pytest.fixture()
def campaign_client() -> CampaignClient:
    """
    Фикстура, создающая клиент для работы с API кампаний.

    :return: Инициализированный клиент CampaignClient.
    """
    return get_campaign_client()

@pytest.fixture()
def campaign(campaign_client) -> CampaignFixture:
    """
    Фикстура, создающая тестовую кампанию.

    :param campaign_client: Клиент для работы с API кампаний.
    :return: Объект CampaignFixture с данными созданной кампании.
    """
    request = CreateCampaignRequestSchema()
    response = campaign_client.create_campaign(request)
    return CampaignFixture(request=request, response=response)
