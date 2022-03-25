# Delivery 1 
# Celina Hansen

##### Imports #####

# Dash
import dash
from dash import html
from dash import dcc

# Plotly
import plotly.express as px

# Henter dataen fra delivery_1.py
import delivery_1 
order = delivery_1.get_data()

##### Diagrammer #####

# Diagram for employee sales 
fig_employee = px.bar(order, 
    x='emp_name', y='total', 
    color='type', text='total', title='Sales by Employee',
    hover_data=[],
    labels={'total':'Total sales', 'emp_name':'Employee', 'type':'Product Type'})
fig_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

# Diagram for product sales
fig_product = px.bar(order,
    x='prod_name', y='total',
    color='type', text='total', title='Sales by Product',
    hover_data=[],
    labels={'total':'Total sales', 'prod_name':'Product Name', 'type':'Product Type'})
fig_product.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_product.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)



##### Aktivering af app #####

dash_app = dash.Dash(__name__)
app = dash_app.server

##### Layout af app #####

dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                children=[
                    html.Div(className='four columns div-user-controls',
                            children=[html.H2('Sales dashboard')]),
                            
                    html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee),
                                dcc.Graph(id="sales_product", figure=fig_product)
                            ]
                    ),
                ]
            )
        ]
)


# Run the app
if __name__ == '__main__':
    dash_app.run_server(debug=True)
