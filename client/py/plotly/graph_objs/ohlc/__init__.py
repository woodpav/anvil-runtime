
from anvil.util import WrappedObject, WrappedList
from anvil.server import serializable_type


@serializable_type
class Decreasing(WrappedObject):
    _name = "Decreasing"
    _module = "plotly.graph_objs.ohlc"

@serializable_type
class Hoverlabel(WrappedObject):
    _name = "Hoverlabel"
    _module = "plotly.graph_objs.ohlc"

@serializable_type
class Increasing(WrappedObject):
    _name = "Increasing"
    _module = "plotly.graph_objs.ohlc"

@serializable_type
class Line(WrappedObject):
    _name = "Line"
    _module = "plotly.graph_objs.ohlc"

@serializable_type
class Stream(WrappedObject):
    _name = "Stream"
    _module = "plotly.graph_objs.ohlc"


__all__ = [
    'Decreasing',
    'Hoverlabel',
    'Increasing',
    'Line',
    'Stream',
    'decreasing',
    'hoverlabel',
    'increasing',
]

from plotly.graph_objs.ohlc import decreasing
from plotly.graph_objs.ohlc import hoverlabel
from plotly.graph_objs.ohlc import increasing
