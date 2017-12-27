"""
Contains the definition of Path.
"""

from point import Point

class Path:
    """
    A Path.

    === Attributes ===
    name - The name of this Path as it appears in the Layers panel.
	uid - The unique id of this Path.
	position - The position of this Path.

	=== Operations ===
	"""

    def __init__(self, uid, path_data, name='Path', x=0, y=0):
        """Instantiate a new Path."""
        self.uid = uid
        self.path_data = path_data
        self.name = name
        self.position = Point(x, y)

    def __str__(self):
        """Return a string representation of this Path."""
        return str.format(
            "Path(uid=\'{}\', name=\'{}\', path_data=\'{}\', position={})",
            self.uid, self.name, self.path_data, self.position)