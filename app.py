import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the data
df = pd.read_csv("formatted_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Group by date to get total sales
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Create the line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Daily Sales",
    labels={"Sales": "Total Sales ($)", "Date": "Date"},
)

# Add a vertical line for the price change date
price_change_date = "2021-01-15"
fig.add_vline(
    x=price_change_date,
    line_width=2,
    line_dash="dash",
    line_color="red"
)

# Add annotation manually
fig.add_annotation(
    x=price_change_date,
    y=daily_sales["Sales"].max(),
    text="Price Change",
    showarrow=True,
    arrowhead=2,
    ax=0,
    ay=-40,
    font=dict(color="red")
)

# Make chart layout simple and clean
fig.update_layout(
    title_x=0.5,
    plot_bgcolor="white",
    xaxis=dict(showgrid=True, gridcolor="lightgrey"),
    yaxis=dict(showgrid=True, gridcolor="lightgrey")
)

# Create Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Pink Morsel Sales Trend", style={"textAlign": "center"}),
    html.P("The red dashed line shows the price change on 15 Jan 2021.", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
