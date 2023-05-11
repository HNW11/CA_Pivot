import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())
print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

print(clicks_by_source)

clicks_pivot = clicks_by_source\
    .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
    .reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())
#Group A and B are equal

clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

print(clicks_by_group)

groups_pivot = clicks_by_group\
    .pivot(index='experimental_group',
          columns='is_click',
          values='user_id')\
    .reset_index()

groups_pivot['percent_clicked'] = groups_pivot[True] / (groups_pivot[True] + groups_pivot[False])

print(groups_pivot)

#Group A had a higher percentage of clicks but only about 7 percent.  

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

print(a_clicks.head())
print(b_clicks.head())

a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()\
    .pivot(index='day',
          columns='is_click',
          values='user_id')\
    .reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()\
    .pivot(index='day',
          columns='is_click',
          values='user_id')\
    .reset_index()

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

print(b_clicks_pivot)

print('With the exception of Tuesday ad A performed better according to clicks across the board. Therefore I would reccomend using ad A')