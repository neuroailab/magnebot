from magnebot import TestController, Arm
from magnebot.action_status import ActionStatus

"""
Test arm movement symmetry.
"""


if __name__ == "__main__":
    m = TestController()
    m.init_scene()
    # Bend both arms to mirrored targets.
    for direction, arm in zip([1, -1], [Arm.left, Arm.right]):
        target = {"x": 0.2 * direction, "y": 0.5, "z": 0.5}
        m._next_frame_commands.append({"$type": "add_position_marker",
                                       "position": target})
        status = m.reach_for(target=target, arm=arm, absolute=False)
        assert status == ActionStatus.success, f"{arm}, {status}"
        m.reset_arm(arm=arm)
    m.end()
