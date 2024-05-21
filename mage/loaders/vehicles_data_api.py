import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.cityofnewyork.us/api/views/bm4k-52h4/rows.csv?accessType=DOWNLOAD'

    sel_vh = [
        "UNIQUE_ID" ,
        "COLLISION_ID" ,
        "CRASH_DATE" ,
        "CRASH_TIME" ,
        "VEHICLE_TYPE", 
        "VEHICLE_DAMAGE" ,
        "DRIVER_SEX" ,
        "DRIVER_LICENSE_STATUS" ,
        "VEHICLE_YEAR" ,
        "VEHICLE_OCCUPANTS" ,  
        "STATE_REGISTRATION" , 
        "CONTRIBUTING_FACTOR_1"
    ]
    sel_vh_rename = {
        "UNIQUE_ID" : "unique_id",
        "COLLISION_ID" : "collision_id",
        "CRASH_DATE" : "crash_date",
        "CRASH_TIME" : "crash_time",
        "STATE_REGISTRATION" : "state_reg",
        "VEHICLE_TYPE" : "vhc_type",
        "VEHICLE_YEAR" : "vhc_year",
        "VEHICLE_OCCUPANTS" : "vhc_occupants",
        "DRIVER_SEX" : "dr_sex",
        "DRIVER_LICENSE_STATUS" : "dr_lic_status",
        "VEHICLE_DAMAGE" : "vhc_dmg",
        "CONTRIBUTING_FACTOR_1" : "contr_f"
    }
    sel_vh_types = {
        "unique_id" : pd.Int64Dtype(),
        "collision_id" : pd.Int64Dtype(),
        "vhc_type" : str,
        "vhc_dmg" : str,
        "dr_sex" : str,
        "dr_lic_status" : str,
        "vhc_year"  : pd.Int64Dtype(),
        "vhc_occupants"  : pd.Int64Dtype(),
        "state_reg" : str,
        "contr_f" : str
    }

    df = pd.read_csv(url, sep=',', dtype=sel_vh_types)
    df = df[sel_vh]
    df.rename(columns=sel_vh_rename, inplace=True)
    
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
