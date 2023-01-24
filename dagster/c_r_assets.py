from osgeo import ogr
import geopandas as gpd
import glob, os
from dagster import Output, asset, get_dagster_logger

@asset
def extract_adm():
    dataSrc = gpd.read_file("E:\\AutoGIS\\adm\\admin_level_4.shp")
    dataSrc[dataSrc['ref']=="RU-NVS"].to_file('E:\\AutoGIS\\adm\\nso_dag.shp', mode="w")
    return "text"

@asset
def files_list():
    
    #return [for shpFile in glob.glob(osmDir+"\\*.shp")]
    return ["E:\\AutoGIS\\osm\\gis_osm_railways_free_1.shp"]
    
@asset
def clip(extract_adm, files_list):
    adm_shp = gpd.read_file("E:\\AutoGIS\\adm\\nso_dag.shp")
    for shp_file in files_list:
        shp = gpd.read_file(shp_file)
        gpd.clip(shp, adm_shp, keep_geom_type=True).to_file('E:\\AutoGIS\\osm\\clip5\\'+os.path.basename(shp_file), mode="w")
    return "ready"

@asset
def reproject(clip):
    
    
    return "text"