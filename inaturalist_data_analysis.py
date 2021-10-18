import pandas as pd
import folium
from folium.plugins import MarkerCluster

def read_csv(path):
    df = pd.read_csv(path)
    return df

def grab_relevant_columns_make_new_df(df, required_columns = ['latitude', 'longitude', 'scientific_name', 'place_guess']):
    filtered_df = df.filter(required_columns)
    print(filtered_df.head())
    return filtered_df

def make_plot(filtered_df):
        
    #empty map
    locations = filtered_df[['latitude', 'longitude']]
    # droping NaNs
    locations=locations.dropna()

    locationlist = locations.values.tolist()
    world_map= folium.Map(tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(world_map)

    df_with_info_other_than_lat_long=filtered_df.drop(['latitude','longitude'], axis=1)

    #for each coordinate, create circlemarker 
    for i in range(0, len(locationlist)):
            df1=df_with_info_other_than_lat_long.iloc[i].to_frame()
            folium.Marker(locationlist[i],popup= df1.to_html(),icon=folium.Icon(color='darkblue',icon= 'default',prefix='fa')).add_to(world_map)
            #folium.CircleMarker(locationlist[i], radius=radius, popup= df1.to_html(), fill =True, ).add_to(marker_cluster)

    world_map.save('dragon_fly_india.html')

def main():
    df = read_csv('inaturalist_data/observations-191982.csv')
    df_relevant_columns = grab_relevant_columns_make_new_df(df)
    make_plot(df_relevant_columns)

main()