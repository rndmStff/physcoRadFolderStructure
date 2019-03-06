# physcoRadFolderStructure

#### This repository contains the folder structure for arranging files meant for Radiance based PhySCo calcualtions.

### Notes
1. Each sample folder represents a different case study. So, there should be as many folders as the fenestration systems being analyzed.
2. Currently this top level folder contains two sample folders: **withGeo** refers to an example-case for those instances where the fenestration system is combination of glass and physical geometry .e.g blinds with glazing. **withNoGeo** refers to an example-case where the fenestration system is just glass.  
3. The irradiance and physco results for the simulations will be stored as per the name of the top folder. For example, the 3Phase climate-data based PhysCo results for 'withGeo' will be stored as  withGeo/resultsPhysCo3Ph/climate.csv and the 3 Phase clear-sky-only results will be stored as withGeo/resultsPhysCo3Ph/clearSky.csv and so on. **So the name of the folders is important and must not contain any spacing**
4. Further notes can be found inside the readme of the sample folders.
5. The irradiance calculations will be provided for at Equinox (20 Mar, 23 Sep) and Solstice dates (21 Jun, 22 Dec) for the year 2019. The hours considered are from 8AM to 6PM, both inclusive.