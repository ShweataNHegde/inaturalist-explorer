# inaturalist-explorer

## Scoping the scientific literature 
- `pygetpapers` to scrape literature on iNaturalist from EPMC
### Premilinary Data
I used `metadata_analysis.py` script to create a corpus (365 papers which mention "iNaturalist") and generate JSON file which contains PMCID, abstract, keywords, extracted keywords(unsupervised), and so on. 



You can learn more about `metadata_analysis.py` script [here](https://github.com/petermr/crops/tree/main/metadata_analysis#readme)

### Analysis
`keyword_analysis.py` script reads the JSON output and gives you the overall counts for keywords. 

Here's a gist:

|no.   |labels                       |counts|
|------|-----------------------------|------|
|197   |Citizen Science              |59    |
|92    |Biodiversity                 |25    |
|598   |Inaturalist                  |14    |
|633   |Invasive species             |12    |
|763   |Natural History Collections  |10    |
|207   |Climate change               |10    |
|322   |Deep Learning                |9     |
|59    |Artificial intelligence      |8     |
|766   |Natural history              |8     |
|351   |Distribution                 |7     |
|242   |Community Science            |7     |
|253   |Conservation                 |6     |
|691   |Machine Learning             |6     |
|1175  |Urban ecology                |6     |
|1065  |Species Distribution Modeling|6     |
|250   |Computer vision              |5     |
|783   |New records                  |5     |


Here's the [full result](https://github.com/ShweataNHegde/inaturalist-explorer/blob/main/counts.csv)


## Exploring iNaturalist Data

Check out this [discussion thread](https://forum.inaturalist.org/t/how-can-i-download-occurrence-data-of-a-species-it-is-for-a-project/20786) to know how to download data from iNaturalist.

I downloaded data on common dragonfly observations in India and plotted it on a world map. Here's the [map](https://github.com/ShweataNHegde/inaturalist-explorer/blob/main/dragon_fly_india.html) in HTML. 

## Future Directions
_I'll add more_


