import pytest
from pydantic import BaseModel
from clients.creative.creative_client import get_creative_client, CreativeClient
from clients.creative.models.creative_schema import (
    CreateCreativeMapRequestSchema,
    CreateCreativeMapResponseSchema,
    CreateCreativeCmsRequestSchema,
)
from fixtures.campaign_fixture import CampaignFixture


class CreativeMapFixture(BaseModel):
    """
    Фикстура для работы с картами креативов в тестах.
    Содержит данные запроса и ответа при создании карты креативов.
    """
    request: CreateCreativeMapRequestSchema  # Данные запроса на создание карты креативов
    response: CreateCreativeMapResponseSchema  # Данные ответа с созданной картой креативов

# class CreativeFixture(BaseModel):
#     """
#     Фикстура для работы с креативами в тестах.
#     Содержит данные запроса и ответа при создании креатива.
#     """
#     request: CreateCreativeRequestSchema  # Данные запроса на создание креатива
#     response: CreateCreativeResponseSchema  # Данные ответа с созданным креативом

@pytest.fixture()
def creative_client() -> CreativeClient:
    """
    Фикстура, создающая клиент для работы с API креативов.

    :return: Инициализированный клиент CreativeClient.
    """
    return get_creative_client()

# @pytest.fixture()
# def creative(campaign_client) -> CreativeFixture:
#     """
#     Фикстура, создающая тестовый креатив.
#
#     :param campaign_client: Клиент для работы с API кампаний.
#     :return: Объект CreativeFixture с данными созданного креатива.
#     """
#     request = CreateCreativeRequestSchema()
#     response = campaign_client.create_creative(request)
#     return CreativeFixture(request=request, response=response)

@pytest.fixture()
def creative_map(campaign: CampaignFixture, creative_client: CreativeClient) -> CreativeMapFixture:
    """
    Фикстура, создающая тестовую карту креативов.

    :param campaign: Фикстура с данными кампании.
    :param creative_client: Клиент для работы с API креативов.
    :return: Объект CreativeMapFixture с данными созданной карты креативов.
    """
    request = CreateCreativeMapRequestSchema(
        communication_channel=campaign.planned_channel
    )
    response = creative_client.create_creative_map(campaign_id=campaign.campaign_id, request=request)
    return CreativeMapFixture(request=request, response=response)

def create_creative_cms():
    """
    Создаёт креатив в CMS.
    Примечание: функция не реализована.
    """
    request = CreateCreativeCmsRequestSchema()
    pass
