from clients.creative.models.creative_schema import (
    CreateCreativeMapResponseSchema,
    CreateCreativeMapRequestSchema,
    GetCreativeMapListResponseSchema,
    CreateCreativeCmsResponseSchema,
)
from tools.assertions.base import assert_equal


def assert_creative_map(request: CreateCreativeMapRequestSchema, response: GetCreativeMapListResponseSchema):
    """
    Проверяет соответствие данных между запросом на создание карты креативов и ответом.

    :param request: Объект запроса на создание карты креативов.
    :param response: Объект ответа со списком карт креативов.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.creative_map_name, response.creative_map_name, "creative_map_name")
    assert_equal(request.communication_channel, response.communication_channel, "communication_channel")
    assert_equal(request.target_app, response.target_app, "target_app")

def assert_relation_creative_map_with_creative_cms(actual: CreateCreativeCmsResponseSchema, expected: CreateCreativeMapResponseSchema):
    """
    Проверяет связь между картой креативов и креативом в CMS.

    :param actual: Объект ответа на создание креатива в CMS.
    :param expected: Объект ответа на создание карты креативов.
    :raises AssertionError: Если идентификаторы не совпадают.
    """
    assert_equal(actual.creative_map_id_with_version.id, expected.creative_map_id, "id")