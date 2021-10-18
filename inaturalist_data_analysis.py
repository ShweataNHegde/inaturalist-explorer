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
    """Map code as per: https://github.com/petermr/dictionary/blob/main/interactive_map/geotext_geopy_map_oil186.ipynb

    Args:
        filtered_df (dataframe): a new dataframe with information relevant to plotting on worldmap
    """
    locations = filtered_df[['latitude', 'longitude']]
    locations=locations.dropna()
    locationlist = locations.values.tolist()
    world_map= folium.Map(tiles="cartodbpositron")
    df_with_info_other_than_lat_long=filtered_df.drop(['latitude','longitude'], axis=1)
    for i in range(0, len(locationlist)):
            df1=df_with_info_other_than_lat_long.iloc[i].to_frame()
            folium.Marker(locationlist[i],popup= df1.to_html(),icon=folium.Icon(color='darkblue',icon= 'default',prefix='fa')).add_to(world_map)
    world_map.save('dragon_fly_india.html')

def main():
    df = read_csv('inaturalist_data/observations-191982.csv')
    df_relevant_columns = grab_relevant_columns_make_new_df(df)
    make_plot(df_relevant_columns)

main()