"""Message type identifiers for Connections."""

MESSAGE_FAMILY = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/connectionadmin/1.0"

CONNECTION_LIST = f"{MESSAGE_FAMILY}/list"
CONNECTION_LIST_REQUEST = f"{MESSAGE_FAMILY}/list_request"

MESSAGE_TYPES = {
    CONNECTION_LIST_REQUEST: (
        "aries_cloudagent.messaging.connectionadmin.messages."
        + "connection_list_request.ConnectionListRequest"
    ),

}
