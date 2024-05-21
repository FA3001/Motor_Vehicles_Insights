import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD'
    
    sel_crashes = [
        "COLLISION_ID",
        "CRASH DATE",
        "CRASH TIME",
        "BOROUGH",
        "NUMBER OF PERSONS INJURED",
        "NUMBER OF PERSONS KILLED",
        "VEHICLE TYPE CODE 1",
        "CONTRIBUTING FACTOR VEHICLE 1",
        "VEHICLE TYPE CODE 2",
        "CONTRIBUTING FACTOR VEHICLE 2",
        "VEHICLE TYPE CODE 3",
        "CONTRIBUTING FACTOR VEHICLE 3",
        "VEHICLE TYPE CODE 4",
        "CONTRIBUTING FACTOR VEHICLE 4" 
    ]
    sel_crashes_rename = {
        "COLLISION_ID" : "collision_id",
        "CRASH DATE" : "crash_date",
        "CRASH TIME" : "crash_time",
        "BOROUGH" : "borough",
        "NUMBER OF PERSONS INJURED" : "injured" ,
        "NUMBER OF PERSONS KILLED" : "killed" ,
        "CONTRIBUTING FACTOR VEHICLE 1" : "contr_f_vhc_1",
        "CONTRIBUTING FACTOR VEHICLE 2" : "contr_f_vhc_2",
        "CONTRIBUTING FACTOR VEHICLE 3" : "contr_f_vhc_3",
        "CONTRIBUTING FACTOR VEHICLE 4" : "contr_f_vhc_4",
        "VEHICLE TYPE CODE 1" : "vhc_1_code",
        "VEHICLE TYPE CODE 2" : "vhc_2_code",
        "VEHICLE TYPE CODE 3" : "vhc_3_code",
        "VEHICLE TYPE CODE 4" : "vhc_4_code"
    }
    sel_crashes_types = {
        "collision_id" : pd.Int64Dtype(),
        "borough" : str,
        "injured" : pd.Int64Dtype(),
        "killed" : pd.Int64Dtype(),
        "vhc_1_code" : str,
        "contr_f_vhc_1" : str,
        "vhc_2_code" : str,
        "contr_f_vhc_2" : str,
        "vhc_3_code" : str,
        "contr_f_vhc_3" : str,
        "vhc_4_code" : str,
        "contr_f_vhc_4" : str
    }

    df = pd.read_csv(url, sep=',', dtype=sel_crashes_types)
    df = df[sel_crashes]
    df.rename(columns=sel_crashes_rename, inplace=True)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
