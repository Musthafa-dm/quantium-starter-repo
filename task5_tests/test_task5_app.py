import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task5_app import app
from collections.abc import Iterable

# helper: walk through the layout tree
def _walk(node):
    if node is None:
        return
    yield node
    kids = getattr(node, "children", None)
    if kids is None:
        return
    if isinstance(kids, Iterable) and not isinstance(kids, (str, bytes)):
        for k in kids:
            yield from _walk(k)
    else:
        yield from _walk(kids)

# helper: find by id
def find_by_id(root, wanted_id: str):
    for node in _walk(root):
        if getattr(node, "id", None) == wanted_id:
            return node
    return None

def test_header_is_present():
    node = find_by_id(app.layout, "header")
    assert node is not None
    assert getattr(node, "children", "") == "Sales Dashboard"

def test_graph_is_present():
    node = find_by_id(app.layout, "sales-graph")
    assert node is not None

def test_region_picker_is_present():
    node = find_by_id(app.layout, "region-picker")
    assert node is not None
