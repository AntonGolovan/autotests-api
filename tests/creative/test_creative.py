import pytest
from http import HTTPStatus
from clients.creative.creative_client import CreativeClient
from clients.creative.models.creative_schema import (
    CreateCreativeMapRequestSchema,
    CreateCreativeMapResponseSchema,
    GetCreativeMapListResponseSchema,
    CreateCreativeCmsRequestSchema,
    CreateCreativeCmsResponseSchema,
)
from fixtures.campaign_fixture import CampaignFixture
from fixtures.creative_fixture import CreativeMapFixture
from tools.assertions.base import assert_status_code
from tools.assertions.creative import (
    assert_creative_map,
    assert_relation_creative_map_with_creative_cms,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.test_creative
class TestCreative:

    def test_create_creative_map(self, creative_client: CreativeClient, campaign: CampaignFixture):
        request = CreateCreativeMapRequestSchema()
        response = creative_client.create_creative_map_api(campaign_id=campaign.campaign_id, request=request)
        response_data = CreateCreativeMapResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_creative_map(
            self,
            creative_map: CreativeMapFixture,
            creative_client: CreativeClient,
            campaign: CampaignFixture
    ):
        response = creative_client.get_creative_maps_api(campaign_id=campaign.campaign_id)
        response_data = GetCreativeMapListResponseSchema.model_validate_json(response.text)[0]
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_creative_map(request=creative_map.request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_create_creative_cms(self, creative_client: CreativeClient, creative_map: CreativeMapFixture):
        request = CreateCreativeCmsRequestSchema()
        response = creative_client.create_creative_cms_api(request=request)
        response_data = CreateCreativeCmsResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_relation_creative_map_with_creative_cms(response_data, creative_map.response)
        validate_json_schema(response.json(), response_data.model_json_schema())