import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns
import datetime as dt
from dash import Dash, html, dcc, Input, Output

! git clone https://github.com/adityaparama/intro_to_dashboard_group_project
df = pd.read_csv('/content/intro_to_dashboard_group_project/nsw_adc_dataset.csv', index_col='Case ID')
df.head()

df['Report Date'] = pd.to_datetime(df['Report Date'])
df['Year'] = df['Report Date'].dt.year
df['Year'].head()

app = Dash(__name__)
server=app.server

app.layout = html.Div(
    style={'backgroundColor': '#2F2F2F', 'padding': '0px'},  # Set the page background to grey
    children=[
        # Header and dropdowns in the same row with flexbox
        html.Div([
            # Title on the left
            html.H1("NSW Ageing and Disability Commission",
                    style={'textAlign': 'left', 'fontFamily':'Arial', 'marginTop': '20px', 'backgroundColor': '#FFFFFF', 'padding': '10px'}),

            # Dropdown filters on the right
            html.Div([
                html.Label("Year:", style={'color': 'black'}),
                dcc.Dropdown(id='year-dropdown',
                             options=[{'label': year, 'value': year} for year in sorted(df['Year'].unique())] + [{'label': 'All', 'value': 'All'}],
                             value='All', placeholder="Year",
                             style={'width': '200px', 'backgroundColor': '#D3D3D3', 'color': 'black'}),

                html.Label("Person Status:", style={'color': 'black'}),
                dcc.Dropdown(id='person-status-dropdown',
                             options=[{'label': status, 'value': status} for status in sorted(df['Person Status'].unique())] + [{'label': 'All', 'value': 'All'}],
                             value='All', placeholder="Category",
                             style={'width': '200px', 'backgroundColor': '#D3D3D3', 'color': 'black',})
            ], style={'display': 'flex', 'gap': '20px', 'padding-right':'20px'})  # Align dropdowns with flexbox
        ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'backgroundColor': '#FFFFFF', 'padding': '0px', 'width': '100%'}),

        # Chart Element
      html.Div([
          # Metrics section with two rows
          html.Div([
              # Metric 1
              html.Div([
                  html.H4("Num. of Calls", style={
                      'color': 'white',
                      'marginBottom': '0',
                      'lineHeight':'0',
                      'fontFamily': 'Arial',
                      'fontSize': '15px'
                  }),
                  html.H2(id='calls', style={
                      'color': 'white',
                      'marginBottom': '0',
                      'lineHeight':'0.5',
                      'fontFamily': 'Arial',
                      'fontSize': '35px'
                  }),
                  html.P(id='calls-change', style={
                      'color': 'white',
                      'fontFamily': 'Arial',
                      'fontSize': '12px'
                  })
              ], style={
                  'background': 'linear-gradient(135deg, #009E73 0%, #00FFCC 100%)',
                  'borderRadius': '15px',
                  'padding': '0px',
                  'margin':'5px',
                  'boxSizing': 'border-box',
                  'textAlign': 'center',
                  'display': 'flex',
                  'flexDirection': 'column',
                  'justifyContent': 'center',
                  'alignItems': 'center',
                  'width': '250px',
                  'height': '100px'
              }),

              # Metric 2
              html.Div([
                  html.H4("Num. of Reports", style={
                      'color': 'white',
                      'marginBottom': '0',
                      'lineHeight':'0',
                      'fontFamily': 'Arial',
                      'fontSize': '15px'
                  }),
                  html.H2(id='reports', style={
                      'color': 'white',
                      'marginBottom': '0',
                      'lineHeight':'0.5',
                      'fontFamily': 'Arial',
                      'fontSize': '35px'
                  }),
                  html.P(id='reports-change', style={
                      'color': 'white',
                      'fontFamily': 'Arial',
                      'fontSize': '12px'
                  })
              ], style={
                  'background': 'linear-gradient(135deg, #E69F00 0%, #FFD700 100%)',
                  'borderRadius': '15px',
                  'padding': '0px',
                  'margin':'5px',
                  'boxSizing': 'border-box',
                  'textAlign': 'center',
                  'display': 'flex',
                  'flexDirection': 'column',
                  'justifyContent': 'center',
                  'alignItems': 'center',
                  'width': '250px',
                  'height': '100px'
              }),

              # Metric 3
              html.Div([
                  html.H4("Avg. of Response Time", style={
                      'color': 'white',
                      'marginTop': '5px',
                      'lineHeight':'0',
                      'fontFamily': 'Arial',
                      'fontSize': '15px'
                  }),
                  html.H2(id='avg-response-time', style={
                      'color': 'white',
                      'marginTop': '5px',
                      'lineHeight':'0.5',
                      'fontFamily': 'Arial',
                      'fontSize': '35px'
                  }),
              ], style={
                  'background': 'linear-gradient(135deg, #56B4E9 0%, #ADD8E6 100%)',
                  'borderRadius': '15px',
                  'padding': '0px',
                  'margin':'5px',
                  'boxSizing': 'border-box',
                  'textAlign': 'center',
                  'display': 'flex',
                  'flexDirection': 'column',
                  'justifyContent': 'center',
                  'alignItems': 'center',
                  'width': '250px',
                  'height': '100px'
              }),

              # Metric 4
              html.Div([
                  html.H4("Num. of Closed Cases", style={
                      'color': 'white',
                      'marginBottom': '0',
                      'lineHeight':'0',
                      'fontFamily': 'Arial',
                      'fontSize': '15px'
                  }),
                  html.H2(id='closed-cases', style={
                      'color': 'white',
                      'marginBottom': '0',
                      'lineHeight':'0.5',
                      'fontFamily': 'Arial',
                      'fontSize': '35px'
                  }),
                  html.P(id='closed-cases-change', style={
                      'color': 'white',
                      'fontFamily': 'Arial',
                      'fontSize': '12px'
                  })
              ], style={
                  'background': 'linear-gradient(135deg, #A65A14 0%, #FF8C00 100%)',
                  'borderRadius': '15px',
                  'padding': '0px',
                  'margin':'5px',
                  'boxSizing': 'border-box',
                  'textAlign': 'center',
                  'display': 'flex',
                  'flexDirection': 'column',
                  'justifyContent': 'center',
                  'alignItems': 'center',
                  'width': '250px',
                  'height': '100px'
              }),

          ], style={'display': 'grid',
                    'gridTemplateColumns':
                    'repeat(2, 1fr)',
                    'gap': '0px',
                    'rowGap':'0px',
                    'marginBottom': '0px',
                    'marginTop':'0px',
                    'borderCollapse':'collapse',
                    'width':'fit-content',
                    }),  # Two rows of metrics

          # Chart Element on the right side of metrics
          html.Div(dcc.Graph(id='age-histogram'),
             style={'padding': '8px', 'backgroundColor': '#fff',
                    'border': '1px solid #ccc', 'borderRadius': '15px',
                    'margin': '0px','margin-left':'5px','marginTop':'5px', 'width': '810px', 'height': '190px',})

], style={'display': 'grid',
          'gridTemplateColumns': '1fr auto',
          'gap': '0px',
          'padding':'0px',
          'margin':'5px',
          'boxSizing':'border-box',
          'flexDirection':'column',
          'width':'fit-content',
          'alignItems':'flex-start'
          }),

    html.Div([
        html.Div(dcc.Graph(id='report-line-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '557px', 'height': '314px'}),

        html.Div(dcc.Graph(id='abuse-type-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '329px', 'height': '314px'}),

        html.Div(dcc.Graph(id='reporter-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '380px', 'height': '314px'})
    ], style={'display': 'flex', 'gap': '10px', 'marginBottom': '10px'}),

    html.Div([
        html.Div(dcc.Graph(id='gender-pie-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '160px', 'height': '240px'}),

        html.Div(dcc.Graph(id='culture-pie-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '160px', 'height': '240px'}),

        html.Div(dcc.Graph(id='language-pie-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '160px', 'height': '240px'}),

        html.Div(dcc.Graph(id='language-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '329px', 'height': '240px'}),

        html.Div(dcc.Graph(id='action-taken-chart'),
                 style={'display': 'flex', 'padding': '8px', 'backgroundColor': '#fff',
                        'border': '1px solid #ccc', 'borderRadius': '15px', 'margin': '5px',
                        'width': '380px', 'height': '240px'})
    ], style={'display': 'flex', 'gap': '10px', 'marginBottom': '10px'}),

])

# Functions to create charts
def create_line_chart(df, y_col, title, height, width):
    counts = df.groupby(['Year', y_col]).size().reset_index(name='Count')
    fig = px.line(counts, x='Year', y='Count', color=y_col,
                  title=title,
                  color_discrete_map={
                      'Call': '#009E73',   # Green
                      'Report': '#E69F00'  # Orange
                  })
    fig.update_layout(xaxis_title='', yaxis_title='', height=height, width=width, paper_bgcolor='rgba(0,0,0,0)',
                      margin={
                          't':50,
                          'b':10,
                          'l':5,
                          'r':10
                      })
    return fig

def create_horizontal_bar_chart(df, x_col, y_col, title, height, width):
    counts = df.groupby(x_col)[x_col].count().reset_index(name='Count')
    counts = counts.sort_values('Count', ascending=True)
    fig = px.bar(counts, x='Count', y=x_col, orientation='h', title=title, color_discrete_sequence=['#009E73'])
    fig.update_layout(xaxis_title='', yaxis_title='', height=height, width=width, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      margin={
                          't':50,
                          'b':10,
                          'l':5,
                          'r':10
                      })
    return fig

def create_pie_chart(df, x_col, title, height, width):
    counts = df.groupby(x_col)[x_col].count().reset_index(name='Count')
    fig = px.pie(counts, values='Count', names=x_col, title=title,
                 color=x_col,  # Ensure this is the column used to differentiate slices
                 color_discrete_map={
                     'Female': '#E69F00',  # Orange
                     'Aboriginal': '#E69F00',
                     'Non-English':'#E69F00',
                     'Male': '#009E73',    # Green
                     'Non-Aboriginal': '#009E73',
                     'English':'#009E73'
                 }                )

    # Update layout to move legend and control pie chart size
    fig.update_layout(
        xaxis_title='', yaxis_title='',
        height=height, width=width,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',
        margin={'t': 50,
                'b': 75,
                'l': 5,
                'r': 10
                },

        # Move the legend to the top
        legend=dict(
            orientation="h",  # Horizontal legend
            yanchor="top",  # Align legend to the bottom of its box
            y=0.01,  # Move legend above the chart (1.1 is slightly above)
            xanchor="center",  # Align horizontally in the center
            x=0.5  # Center the legend
        )
    )

    # Control the pie chart size
    fig.update_traces(
        hole=0.3,  # Adjust this for a donut chart; remove if you want a full pie
        marker=dict(
            line=dict(color='#fff', width=2)  # Add a border around pie slices
        )
    )

    return fig


def create_histogram(df, x_col, title, height, width):
    age_category_order = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                          '50-54', '55-59', '60-64', '65-69', '70-74', '75-79',
                          '80-84', '85-89', '90-94', '95-99', '100+', 'Unknown']
    fig = px.histogram(df, x=x_col, category_orders={x_col: age_category_order}, title=title, color_discrete_sequence=['#009E73'])
    fig.update_layout(xaxis_title='', yaxis_title='', height=height, width=width, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      margin={
                          't':50,
                          'b':10,
                          'l':5,
                          'r':10
                      })
    # plt.tight_layout()
    return fig

@app.callback(
    Output('calls', 'children'),
    Output('calls-change', 'children'),
    Output('reports', 'children'),
    Output('reports-change', 'children'),
    Output('avg-response-time', 'children'),
    Output('closed-cases', 'children'),
    Output('closed-cases-change', 'children'),
    Output('report-line-chart', 'figure'),
    Output('gender-pie-chart', 'figure'),
    Output('culture-pie-chart', 'figure'),
    Output('language-pie-chart', 'figure'),
    Output('age-histogram', 'figure'),
    Output('abuse-type-chart', 'figure'),
    Output('reporter-chart', 'figure'),
    Output('action-taken-chart', 'figure'),
    Output('language-chart', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('person-status-dropdown', 'value')]
)

def update_metrics_and_charts(selected_year, selected_person_status):
    filtered_df = df.copy()
    filtered_df['Year'] = filtered_df['Year'].astype(int)

    if selected_person_status != 'All':
        filtered_df = filtered_df[filtered_df['Person Status'] == selected_person_status]

    if selected_year != 'All':
        current_year_df = filtered_df[filtered_df['Year'] == selected_year]
    else:
        current_year_df = filtered_df

    if selected_year != 'All':
        line_chart_df = filtered_df[filtered_df['Year'] <= selected_year]  # Include all data up to the selected year
    else:
        line_chart_df = filtered_df

    # Calculate metrics
    num_calls = current_year_df[current_year_df['Type of Report'] == 'Call'].shape[0]
    num_reports = current_year_df[current_year_df['Type of Report'] == 'Report'].shape[0]
    num_closed_cases = current_year_df[current_year_df['Case Status'] == 'Closed'].shape[0]

    if 'Response Date' in filtered_df.columns and 'Report Date' in filtered_df.columns:
        filtered_df['Response Date'] = pd.to_datetime(filtered_df['Response Date'], errors='coerce')
        filtered_df['Report Date'] = pd.to_datetime(filtered_df['Report Date'], errors='coerce')
        filtered_df['Response Time'] = (filtered_df['Response Date'] - filtered_df['Report Date']).dt.days
        average_response_time = filtered_df['Response Time'].mean().round()
    else:
        average_response_time = None

    # Metrics from previous year
    if selected_year != 'All':
        previous_year = selected_year - 1
        previous_year_df = df[df['Year'] == previous_year]
        prev_num_calls = previous_year_df[previous_year_df['Type of Report'] == 'Call'].shape[0]
        prev_num_reports = previous_year_df[previous_year_df['Type of Report'] == 'Report'].shape[0]
        prev_num_closed_cases = previous_year_df[previous_year_df['Case Status'] == 'Closed'].shape[0]

        # Calculate percentage change from previous year
        calls_change = ((num_calls - prev_num_calls) / prev_num_calls * 100) if prev_num_calls > 0 else None
        reports_change = ((num_reports - prev_num_reports) / prev_num_reports * 100) if prev_num_reports > 0 else None
        closed_cases_change = ((num_closed_cases - prev_num_closed_cases) / prev_num_closed_cases * 100) if prev_num_closed_cases > 0 else None
    else:
        calls_change = reports_change = closed_cases_change = None

    # Generate Charts
    fig_report = create_line_chart(line_chart_df, 'Type of Report', 'Number of Calls and Reports Over Time', height=339, width=557)
    fig_gender = create_pie_chart(filtered_df, 'Gender', 'Gender', height=265, width=160)
    fig_culture = create_pie_chart(filtered_df, 'Cultural Background', 'First Nation', height=265, width=160)
    filtered_df['Language Category'] = filtered_df['Language'].apply(lambda x: 'English' if x == 'English' else 'Non-English')
    fig_language_pie = create_pie_chart(filtered_df, 'Language Category', 'Language', height=265, width=160)
    fig_age = create_histogram(filtered_df, 'Age Category', 'Age Distribution', height=225, width=810)
    fig_abuse = create_horizontal_bar_chart(filtered_df, 'Type of Alleged Abuse', 'Count', 'Type of Alleged Abuse', height=339, width=329)
    fig_reporter = create_horizontal_bar_chart(filtered_df, 'Reporters', 'Count', 'Relationship with the Reporters', height=339, width=380)
    fig_action = create_horizontal_bar_chart(filtered_df, 'Primary Action Taken', 'Count', 'Primary Action Taken', height=265, width=380)
    non_english_df = filtered_df[filtered_df['Language'] != 'English']
    fig_language = create_horizontal_bar_chart(non_english_df, 'Language', 'Count', 'Non-English Languages', height=265, width=329)

    return (f"{num_calls:,}", f"{calls_change:.2f}% from prev. year" if calls_change else "-",
            f"{num_reports:,}", f"{reports_change:.2f}% from prev. year" if reports_change else "-",
            f"{average_response_time:.2f}",
            f"{num_closed_cases:,}", f"{closed_cases_change:.2f}% from prev. year" if closed_cases_change else "-",
            fig_report, fig_gender, fig_culture, fig_language_pie,
            fig_age, fig_abuse, fig_reporter, fig_action, fig_language)

if __name__ == '__main__':
    app.run_server(debug=True)
