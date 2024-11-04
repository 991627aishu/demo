
import plotly.express as px
import seaborn as sns
import pandas as pd
tips = sns.load_dataset("tips")
fig1 = px.bar(tips,x="day",y="tip")
fig2 = px.scatter(tips,x="total_bill",y="tip")
st.tittle("data visualization with plotly")
st.header("Plot1:bar plot-Tips by Day")
st.plotly_chart(fig1)
st.markdown('''**Insight observed**:(Add your insights here)''')