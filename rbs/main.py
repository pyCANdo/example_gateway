from pyrbs import PyRbs, CanMessage

rbs = PyRbs(dashboard=False)

@rbs.can_message.on("CAN1.*")
def gateway_can1_can2(self: CanMessage):
    self.send(channel=2)