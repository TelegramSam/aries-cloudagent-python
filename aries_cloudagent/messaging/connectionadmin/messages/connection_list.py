"""Represents an invitation message for establishing connection."""

from typing import Sequence
from urllib.parse import parse_qs, urljoin, urlparse

from marshmallow import ValidationError, fields, validates_schema, Schema

from ...agent_message import AgentMessage, AgentMessageSchema
from ..message_types import CONNECTION_LIST_REQUEST
from ....wallet.util import b64_to_bytes, bytes_to_b64

from ...connections.models.connection_record import ConnectionRecord, ConnectionRecordSchema

HANDLER_CLASS = (
    "aries_cloudagent.messaging.connectionadmin.handlers."
    + "connection_list_request_handler.ConnectionListHandler"
)


class ConnectionListSchema(Schema):
    """Result schema for connection list."""

    results = fields.List(fields.Nested(ConnectionRecordSchema()))

class ConnectionList(AgentMessage):
    """Class representing a connection invitation."""

    class Meta:
        """Metadata for a connection invitation."""

        handler_class = HANDLER_CLASS
        message_type = CONNECTION_LIST_REQUEST
        schema_class = "ConnectionListRequestSchema"

    def __init__(
        self,
        *,
        connections,
        **kwargs,
    ):
        """
        Initialize connection list request object.

        Args:

        """
        self.connections = connections
        super(ConnectionList, self).__init__(**kwargs)


class ConnectionListSchema(AgentMessageSchema):
    """Connection list request schema class."""

    class Meta:
        """Connection invitation schema metadata."""

        model_class = ConnectionList


    @validates_schema
    def validate_fields(self, data):
        """
        Validate schema fields.

        Args:
            data: The data to validate

        Raises:
            ValidationError: If any of the fields do not validate

        """
