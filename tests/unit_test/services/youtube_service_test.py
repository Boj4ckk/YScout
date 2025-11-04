import os
import pytest
from unittest.mock import patch
from services.youtube_service import YoutubeService

@patch("google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file")
@patch("googleapiclient.discovery.build")
def test_youtube_service_init_success(mock_build,mock_flow):

    mock_build.return_value = "mock_youtube_client"
    mock_flow.return_value.run_local_server.return_value = "mock_credentials"

    os.environ["API_SERVICE_NAME"] = "mocked_service"
    os.environ["SCOPES"] = "scope1,scope2"
    os.environ["CLIENT_SECRET_FILE"] = "mocked file"
    os.environ["API_VERSION"] ="mocked version"

    y_service = YoutubeService()
    assert y_service.youtube_client == "mock_youtube_client"

@patch("google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file")
@patch("googleapiclient.discovery.build")
def test_youtube_service_missing_scopes(mock_build,mock_flow):
    
    mock_build.return_value = "mock_youtube_client"
    mock_flow.return_value.run_local_server.return_value = "mock_credentials"

    os.environ.pop("SCOPES",None)
    os.environ["API_SERVICE_NAME"] = "mocked_service"
    os.environ["CLIENT_SECRET_FILE"] = "mocked file"
    os.environ["API_VERSION"] ="mocked version"

   

    with pytest.raises(Exception):
        YoutubeService()

@patch("google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file")
@patch("googleapiclient.discovery.build")
def test_youtube_service_missing_service_name(mock_build,mock_flow):
    
    mock_build.return_value = "mock_youtube_client"
    mock_flow.return_value.run_local_server.return_value = "mock_credentials"

    os.environ["SCOPES"] = "scope1,scope2"
    os.environ.pop("API_SERVICE_NAME",None)
    os.environ["CLIENT_SECRET_FILE"] = "mocked file"
    os.environ["API_VERSION"] ="mocked version"

   

    with pytest.raises(Exception):
        YoutubeService()

@patch("google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file")
@patch("googleapiclient.discovery.build")
def test_youtube_service_missing_secret_file(mock_build,mock_flow):
    
    mock_build.return_value = "mock_youtube_client"
    mock_flow.return_value.run_local_server.return_value = "mock_credentials"

    os.environ["SCOPES"] = "scope1,scope2"
    os.environ["API_SERVICE_NAME"] = "mocked_service"
    os.environ.pop("CLIENT_SECRET_FILE",None)
    os.environ["API_VERSION"] ="mocked version"

   

    with pytest.raises(Exception):
        YoutubeService()


@patch("google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file")
@patch("googleapiclient.discovery.build")
def test_youtube_service_missing_api_version(mock_build,mock_flow):
    
    mock_build.return_value = "mock_youtube_client"
    mock_flow.return_value.run_local_server.return_value = "mock_credentials"

    os.environ["SCOPES"] = "scope1,scope2"
    os.environ["API_SERVICE_NAME"] = "mocked_service"
    os.environ["CLIENT_SECRET_FILE"] = "mocked file"
    os.environ.pop("API_VERSION",None)

   

    with pytest.raises(Exception):
        YoutubeService()





