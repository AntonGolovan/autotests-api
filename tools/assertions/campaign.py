from clients.campaign.models.campaign_schema import (
    CreateCampaignRequestSchema,
    CreateCampaignResponseSchema,
    UpdateCampaignResponseSchema,
)
from tools.assertions.base import assert_equal


def assert_create_campaign(request: CreateCampaignRequestSchema, response: CreateCampaignResponseSchema):
    """
    Проверяет соответствие данных между запросом на создание кампании и ответом.

    :param request: Объект запроса на создание кампании.
    :param response: Объект ответа с данными созданной кампании.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.campaign_type, response.campaign_type, "campaign_type")
    assert_equal(request.planned_channels, response.planned_channels, "planned_channels")
    assert_equal(request.kind, response.kind, "kind")
    assert_equal(request.subkind, response.subkind, "subkind")

def assert_update_campaign(request: CreateCampaignResponseSchema, response: UpdateCampaignResponseSchema):
    """
    Проверяет соответствие данных между запросом на обновление кампании и ответом.

    :param request: Объект запроса на обновление кампании.
    :param response: Объект ответа с данными обновлённой кампании.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.campaign_type, response.campaign_type, "campaign_type")
    assert_equal(request.planned_channels, response.planned_channels, "planned_channels")
    assert_equal(request.kind, response.kind, "kind")
    assert_equal(request.subkind, response.subkind, "subkind")