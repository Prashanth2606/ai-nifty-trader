from dhanhq import DhanContext, dhanhq
from config import DHAN_CLIENT_ID, DHAN_ACCESS_TOKEN


def get_dhan_client():
    dhan_context = DhanContext(
        DHAN_CLIENT_ID,
        DHAN_ACCESS_TOKEN
    )

    return dhanhq(dhan_context)