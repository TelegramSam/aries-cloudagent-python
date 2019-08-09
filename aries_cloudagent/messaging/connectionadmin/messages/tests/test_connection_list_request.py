from ..connection_list_request import ConnectionListRequest
from ...message_types import CONNECTION_LIST_REQUEST

from unittest import mock, TestCase


class TestConnectionListRequest(TestCase):

    def test_init(self):
        connection_list_request = ConnectionListRequest(

        )
        #assert connection_invitation.label == self.label

    def test_type(self):
        connection_invitation = ConnectionListRequest(

        )

        assert connection_invitation._type == CONNECTION_LIST_REQUEST

    @mock.patch(
        "aries_cloudagent.messaging.connectionadmin.messages."
        + "connection_list_request.ConnectionListRequestSchema.load"
    )
    def test_deserialize(self, mock_connection_list_request_schema_load):
        obj = {"obj": "obj"}

        connection_list_request = ConnectionListRequest.deserialize(obj)
        mock_connection_list_request_schema_load.assert_called_once_with(obj)

        assert (
            connection_list_request is mock_connection_list_request_schema_load.return_value
        )

    @mock.patch(
        "aries_cloudagent.messaging.connectionadmin.messages."
        + "connection_list_request.ConnectionListRequestSchema.dump"
    )
    def test_serialize(self, mock_connection_list_request_schema_dump):
        connection_list_request = ConnectionListRequest(

        )

        connection_list_request_dict = connection_list_request.serialize()
        mock_connection_list_request_schema_dump.assert_called_once_with(
            connection_list_request
        )

        assert (
            connection_list_request_dict
            is mock_connection_list_request_schema_dump.return_value
        )


class TestConnectionListRequestSchema(TestCase):

    connection_list_request = TestConnectionListRequest()

    def test_make_model(self):
        data = self.connection_list_request.serialize()
        model_instance = TestConnectionListRequest.deserialize(data)
        assert isinstance(model_instance, TestConnectionListRequest)
