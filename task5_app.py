import dash
from dash import html, dcc

# Create the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Sales Dashboard", id="header"),
    dcc.Dropdown(
        id="region-picker",
        options=[
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"}
        ],
        value="north"
    ),
    dcc.Graph(id="sales-graph")
])

if __name__ == "__main__":
    app.run(debug=True)
