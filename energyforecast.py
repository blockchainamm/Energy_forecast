# import required libraries
import plotly.graph_objects as go
import urllib.request, json
import streamlit as st

page_title = "Energy forecast in USA for 2050"

def main():
    st.set_page_config(page_title = page_title)
    st.title(page_title)

if __name__ == '__main__':
    main() 

# --- Hide Streamlit Style ---
hide_st_style = """
                <style>
                #MainMenu {Visibility: hidden;}
                footer {Visibility: hidden;}
                header {Visibility: hidden;}
                </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

#print ('Value of data is: ', data)
# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
  ))])

fig.update_layout(
    hovermode = 'x',
    title="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell",
    font=dict(size = 10, color = 'white'),
    plot_bgcolor='black',
    paper_bgcolor='black',
    width=1000,
    height=600 
)

st.write(' ')
fig.update_layout(margin=dict(t=100, b=50))
st.plotly_chart(fig, use_container_width=True)