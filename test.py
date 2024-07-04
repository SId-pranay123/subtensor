import substrateinterface

node = substrateinterface.SubstrateInterface(url="ws://localhost:9944")

node.rpc_request("subtensor_epoch", [18])

print(node.rpc_request("subtensor_epoch", [18], True))