
import pytest
from unittest.mock import patch
from utils.youtube_utils import YoutubeUtils

@patch("utils.youtube_utils.requests.get")
def test_get_youtube_suggestions_list(mock_get):
    mock_get.return_value.json.return_value = ["keyword", ["suggestion1", "suggestion2"]]
    mock_get.return_value.raise_for_status = lambda: None
    result = YoutubeUtils.get_youtube_suggestions_list("test")
    assert result == ["suggestion1", "suggestion2"]

@patch.object(YoutubeUtils, "get_youtube_suggestions_list")
@patch("os.getenv")
def test_get_youtube_suggestions_by_keywords(mock_getenv, mock_suggestions):
    mock_getenv.side_effect = lambda k, d=None: "foo,bar" if k == "KEYWORD_LIST" else d
    mock_suggestions.side_effect = lambda k: [k, f"{k}_1", f"{k}_2"]
    result = YoutubeUtils.get_youtube_suggestions_by_keywords()
    assert result == {
        "foo": ["foo_1", "foo_2"],
        "bar": ["bar_1", "bar_2"]
    }

@patch("utils.youtube_utils.requests.get")
def test_get_youtube_suggestions_list_empty(mock_get):
    mock_get.return_value.json.return_value = ["keyword"]
    mock_get.return_value.raise_for_status = lambda: None
    result = YoutubeUtils.get_youtube_suggestions_list("test")
    assert result == []