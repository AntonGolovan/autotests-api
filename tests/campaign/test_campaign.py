from http import HTTPStatus
import pytest
from clients.campaign.campaign_client import CampaignClient
from clients.campaign.models.campaign_schema import (
    CreateCampaignRequestSchema,
    CreateCampaignResponseSchema,
    UpdateCampaignRequestSchema,
    UpdateCampaignResponseSchema,
)
from fixtures.campaign_fixture import CampaignFixture
from tools.assertions.base import assert_status_code
from tools.assertions.campaign import (
    assert_create_campaign,
    assert_update_campaign,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.smoke
@pytest.mark.regression
class TestCampaign:

    def test_create_campaign(self, campaign_client: CampaignClient):
        request = CreateCampaignRequestSchema()
        response = campaign_client.create_campaign_api(request=request)
        response_data = CreateCampaignResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_campaign(request=request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


    def update_campaign(self, campaign: CampaignFixture, campaign_client: CampaignClient):
        request = UpdateCampaignRequestSchema()
        response = campaign_client.update_campaign_api(request=request, campaign_id=campaign.campaign_id)
        response_data = UpdateCampaignResponseSchema.model_validate_json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_campaign(request=campaign.response, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data)