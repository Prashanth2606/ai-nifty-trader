from broker.dhan_client import get_dhan_client

dhan = get_dhan_client()

print(type(dhan))

response = dhan.get_fund_limits()

print(response)