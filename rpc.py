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
            LongField("xid", 1),
            LongField("msg_type", 0),
            LongField("rpcvers", 2),
            LongField("prog", 100000),
            LongField("vers", 2),
            LongField("proc", 4),
            LongField("cred_flavor", 0),
            LongField("cred_len", 0),
            LongField("verifier_flavor", 0),
            LongField("verifier_len", 0)]

