
from anvil.util import WrappedObject, WrappedList
from anvil.server import serializable_type


@serializable_type
class Tickfont(WrappedObject):
    _name = "Tickfont"
    _module = "plotly.graph_objs.layout.ternary.aaxis"

@serializable_type
class Tickformatstop(WrappedObject):
    _name = "Tickformatstop"
    _module = "plotly.graph_objs.layout.ternary.aaxis"

@serializable_type
class Title(WrappedObject):
    _name = "Title"
    _module = "plotly.graph_objs.layout.ternary.aaxis"


__all__ = [
    'Tickfont',
    'Tickformatstop',
    'Title',
    'title',
]

from plotly.graph_objs.layout.ternary.aaxis import title
