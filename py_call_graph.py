import pytest
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph.config import Config
from pycallgraph.globbing_filter import GlobbingFilter


@pytest.fixture(autouse=True)
def record_call_graph(request):
    import time
    current_millis = int(round(time.time() * 1000))
    with PyCallGraph(output=GraphvizOutput(output_file='./dotFiles/images/%s_%s.png' % (request._pyfuncitem.name,
                                                                                        current_millis),
                                           dot_file='./dotFiles/%s_%s.dot' % (request._pyfuncitem.name,
                                                                              current_millis)),
                     config=Config(debug=True,
                                   trace_filter=GlobbingFilter(
                                       exclude=['pycallgraph.*', 'tests.*', '*.yml', "_pytest.*", "pluggy.*"],
                                       include=['patterns.*']
                                   )
                                   )):
        yield
