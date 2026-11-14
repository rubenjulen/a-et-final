import sys
from AnyQt.QtWidgets import QApplication
app=QApplication([])
from orangecanvas.registry import WidgetRegistry
from orangecanvas.registry.discovery import WidgetDiscovery
from orangewidget.workflow.discovery import WidgetDiscovery as OWD
from Orange.canvas.config import Config
cfg=Config(); reg=WidgetRegistry(); d=OWD(reg); d.run(cfg.widgets_entry_points())
from orangecanvas.scheme import readwrite, Scheme
from orangewidget.workflow.widgetsscheme import WidgetsScheme
s=WidgetsScheme()
with open(sys.argv[1],'rb') as f: readwrite.scheme_load(s,f,registry=reg)
print(len(s.nodes),'nodes',len(s.links),'links',len(s.annotations),'notes')
for l in s.links: print(' ',l.source_node.title,'->',l.sink_node.title, l.source_channel.name,'->',l.sink_channel.name)
