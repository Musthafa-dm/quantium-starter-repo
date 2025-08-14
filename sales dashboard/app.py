from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the sales data
df = pd.read_csv("formatted_data.csv")

# Format date and month
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Create app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsels Sales Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold"}),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            inline=True
        )
    ], className="radio-container"),

    dcc.Graph(id="region-sales"),

    html.Hr(),

    html.H3("Monthly Sales by Region", style={"textAlign": "center"}),
    dcc.Graph(id="all-regions")
])


# Callback to update graphs
@app.callback(
    Output("region-sales", "figure"),
    Output("all-regions", "figure"),
    Input("region-filter", "value")
)
def update_graphs(selected_region):
    # Filter for selected region
    if selected_region == "all":
        region_data = df
    else:
        region_data = df[df["Region"] == selected_region]

    # Monthly sales for selected region
    monthly_sales = region_data.groupby("Month", as_index=False)["Sales"].sum()

    fig1 = px.bar(
        monthly_sales,
        x="Month",
        y="Sales",
        title=f"Monthly Sales - {selected_region.capitalize() if selected_region != 'all' else 'All Regions'}",
        color_discrete_sequence=["#4C78A8"]
    )

    # Monthly sales for all regions (stacked bar)
    monthly_region_sales = df.groupby(["Month", "Region"], as_index=False)["Sales"].sum()
    fig2 = px.bar(
        monthly_region_sales,
        x="Month",
        y="Sales",
        color="Region",
        barmode="stack",
        title="Monthly Sales by Region",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    return fig1, fig2


if __name__ == "__main__":
    app.run(debug=True)
