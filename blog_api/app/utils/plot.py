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
  def score_plot(data, level):
        type_of_chart = 'no_transactions'

        plot_score = go.Pie(
            name="Risk Score",
            hole=0.8,
            sort=False,
            textinfo='none',
            direction='clockwise',
            domain={"column": 0},
            values=[data['score'], 100-data['score']],
            labels=["Trust", "Risk"],
            textposition='inside',
            hoverinfo="label+percent+name",
            marker=dict(colors=colors, line=dict(color=text_color, width=pie_width_space))
        )

        layout_score = go.Layout(
            title="Risk Score",
            grid={"rows": 1, "columns": 1},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            font=dict(size=font_size, color=text_color),
            annotations=[
                {
                    "font": {"size": 90, 'color': text_color},
                    "showarrow": False,
                    "text":  100-data['score'],
                    "x": 0.5,
                    "y": 0.5
                }
            ]
        )
        fig_score = go.Figure(data=[plot_score], layout=layout_score)
        graph_score = json.dumps(fig_score, cls=plotly.utils.PlotlyJSONEncoder)

        fig_out = go.Figure(data=plots_out, layout=layout_in_out)
        graph_out = json.dumps(fig_out, cls=plotly.utils.PlotlyJSONEncoder)
        score_perc = 100-data['score']
        if score_perc < 25:
            text =  "Trusted"
        elif score_perc < 50:
            text = "Low risk"
        elif score_perc < 75:
            text = "Needs investigation"
        else:
            text = "High Risk"
        log.info({'score': score_perc, 'Text': text, 'in': graph_in, 'out': graph_out})
        return {'score': score_perc, 'Text': text, 'in': graph_in, 'out': graph_out}
        # return {'score': graph_score, 'in_out': graph_in_out}
