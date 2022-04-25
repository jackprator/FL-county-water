# FL-county-water
imports needed:
```pip install flask```
```pip install requests```
```pip install flask_sqlalchemy```
```pip install flask_wtf```

## What this app does
This reporting project aims to make public and private drinking water data available to Floridians. It allows users to see where nitrates are contaminating Florida's private wells, aa well as a county-by-county breakdown of public drinking water health. 

## How it works
This app uses flask templates to generate county water pages with information pulled from a SQLite database. Because water quality is updated annually in Florida, this database structure makes it easy to go in and update quality measures as new reports come are submitted to the state. The homepage prominently features a Plot.ly map which shows hotspots for unhealthy wells in Florida.

## Data
Well water data was downloaded directly from the [Florida Department of Environmental Protection](https://geodata.dep.state.fl.us/datasets/FDEP::water-supply-restoration-wsrp-wells/explore?location=27.724105%2C-83.732250%2C6.76&showTable=true). Special thanks to [Marlowe Starling](https://www.wuft.org/news/author/marlowestarling/), who cleaned the data using R and the filtered the results to look specifically for nitrate concentrations.

Averages for nitrate concentrations are based on the total number of wells sampled in a given county, as the total number of private water wells in each county was not available. Thus, averages are standardized for each county. Averages were filtered for counties with at least 5 sampled wells for places with at least one contaminated well (at least one well with more than 10 mg/L). The number of wells sampled varies from one to nearly 8,000 in a single county. Owners of private water wells are not required to get their well water tested, but are encouraged to do so by the state DEP. Concentrations of nitrate are measured in mg/L. 

More information on the private well data can be found [here](https://rpubs.com/marlowe_starling/nitrogen-pollution).

Drinking water nitrates data by county was sourced from each county's most recent [Consumer Confidence Report](https://www.epa.gov/ccr/ccr-information-consumers), required by the EPA. Some counties did not report nitrates in their CRRs, and others reported no detectable nitrates in drinking water supplies. In some districts where water quality was measured by cities, instead of by counties, each city's reported nitrates count was averaged to calculate the aproximate county level.

County groundwater nitrates trends were calculated by the Florida DEP in its [2020 Integrated Water Quality Assessment](https://floridadep.gov/sites/default/files/2020_IR_Master_FINAL%20-%20ADA.pdf). The table where these findings are mentioned is available as a PDF in the ```static``` folder.
