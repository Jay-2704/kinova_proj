# kortex_control.py

from kortex_api.autogen.client_stubs import BaseClient
from kortex_api.autogen.messages import Base_pb2

def move_arm_upwards(base):
    """
    Sends a command to the Kinova robotic arm to move upwards.
    """
    try:
        command = Base_pb2.TwistCommand()
        command.reference_frame = Base_pb2.CARTESIAN_REFERENCE_FRAME_BASE
        command.duration = 0
        command.twist.linear_z = 0.1  # Positive value for upward movement
        base.SendTwistCommand(command)
        print("Command sent: Moving arm upwards")
    except Exception as e:
        print(f"Failed to move arm upwards: {e}")

def move_arm_downwards(base):
    """
    Sends a command to the Kinova robotic arm to move downwards.
    """
    try:
        command = Base_pb2.TwistCommand()
        command.reference_frame = Base_pb2.CARTESIAN_REFERENCE_FRAME_BASE
        command.duration = 0
        command.twist.linear_z = -0.1  # Negative value for downward movement
        base.SendTwistCommand(command)
        print("Command sent: Moving arm downwards")
    except Exception as e:
        print(f"Failed to move arm downwards: {e}")

def move_arm_left(base):
    """
    Sends a command to the Kinova robotic arm to move left.
    """
    try:
        command = Base_pb2.TwistCommand()
        command.reference_frame = Base_pb2.CARTESIAN_REFERENCE_FRAME_BASE
        command.duration = 0
        command.twist.linear_y = 0.1  # Positive value for left movement
        base.SendTwistCommand(command)
        print("Command sent: Moving arm left")
    except Exception as e:
        print(f"Failed to move arm left: {e}")

def move_arm_right(base):
    """
    Sends a command to the Kinova robotic arm to move right.
    """
    try:
        command = Base_pb2.TwistCommand()
        command.reference_frame = Base_pb2.CARTESIAN_REFERENCE_FRAME_BASE
        command.duration = 0
        command.twist.linear_y = -0.1  # Negative value for right movement
        base.SendTwistCommand(command)
        print("Command sent: Moving arm right")
    except Exception as e:
        print(f"Failed to move arm right: {e}")