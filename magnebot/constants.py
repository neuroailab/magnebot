# The radius of the Magnebot as defined by its longer axis.
MAGNEBOT_RADIUS: float = 0.22
# The cell size on the occupancy map. This is slightly bigger than diameter of the Magnebot.
OCCUPANCY_CELL_SIZE: float = (MAGNEBOT_RADIUS * 2) + 0.05
# A "magic number" used to set the spin speed while turning.
TURN_MAGIC_NUMBER: float = 3.12
