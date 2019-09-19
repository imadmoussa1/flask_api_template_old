import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
from .logger import Logger

log = Logger.log(__name__)

import pandas as pd
import numpy as np
import json
import base64

text_color = '#F5F8FA'
line_color = '#211E2D'
colors = ['#56d493', '#d46555', '#e5bf69', '#99d79f', '#99D1D7', '#4A6580']
font_size = 16
pie_width_space = 4


class Plot:
