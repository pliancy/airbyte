#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

from unittest.mock import MagicMock

from pytest import fixture
from source_sentinel_one.source import SourceSentinelOne

@fixture()
def config(request):
    args = {
            "api_token": "Xoiwx",
            "your_management_url": "//example.sentinelone.net"
        }
    return args

def test_check_connection(mocker, config):
    source = SourceSentinelOne()
    logger_mock = MagicMock()
    (connection_status, error) = source.check_connection(logger_mock, config)
    expected_status = False
    assert connection_status == expected_status


def test_streams(mocker, config):
    source = SourceSentinelOne()
    streams = source.streams(config)

    # TODO: replace this with your streams number
    expected_streams_number = 23
    assert len(streams) == expected_streams_number
