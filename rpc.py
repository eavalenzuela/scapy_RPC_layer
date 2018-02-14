from scapy.fields import *
from scapy.packet import *
from scapy.layers.inet import UDP

"""
RPC (Remote Procedure Call)

[RFC5531]
"""

#############################################################################
###                            RPC  (RFC5531)                             ###
#############################################################################
# The RPC protocol can be implemented on several different transport protocols.
#   The scope of the definition of the RPC protocol excludes
#   how a message is passed from one process to another, and includes
#   only the specification and interpretation of messages.

class RPCCall(Packet):
    name = "Remote Procedure Call"
    fields_desc = [
            IntField("xid", 1),
            IntField("msg_type", 0),
            IntField("rpcvers", 2),
            IntField("prog", 100000),
            IntField("vers", 2),
            IntField("proc", 4),
            IntField("cred_flavor", 0),
            IntField("cred_len", 0),
            IntField("verifier_flavor", 0),
            IntField("verifier_len", 0)]

