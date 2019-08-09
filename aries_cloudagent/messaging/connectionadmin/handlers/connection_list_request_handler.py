"""Connection request handler."""
from aries_cloudagent.messaging.connections.models.connection_record import ConnectionRecord
from ...base_handler import BaseHandler, BaseResponder, RequestContext

from ..messages.connection_list_request import ConnectionListRequest
from ..messages.connection_list import ConnectionList


class ConnectionRequestHandler(BaseHandler):
    """Handler class for connection requests."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Handle list request.

        Args:
            context: Request context
            responder: Responder callback
        """

        self._logger.debug(f"ConnectionRequestHandler called with context {context}")
        assert isinstance(context.message, ConnectionListRequest)

        context = request.app["request_context"]
        tag_filter = {}
        # for param_name in (
        #         "initiator",
        #         "invitation_id",
        #         "my_did",
        #         "state",
        #         "their_did",
        #         "their_role",
        # ):
        #     if param_name in request.query and request.query[param_name] != "":
        #         tag_filter[param_name] = request.query[param_name]
        records = await ConnectionRecord.query(context, tag_filter)
        results = []
        for record in records:
            row = record.serialize()
            row["activity"] = await record.fetch_activity(context)
            results.append(row)
        #results.sort(key=connection_sort_key)



        await responder.send_reply(
            ConnectionList(results),
            target=target,
        )
