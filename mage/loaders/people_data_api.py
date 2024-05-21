import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    url_P = "https://data.cityofnewyork.us/api/views/f55k-p6yu/rows.csv?accessType=DOWNLOAD"

    sel_P = [
    "UNIQUE_ID" ,
    "COLLISION_ID",
    "CRASH_DATE" ,
    "CRASH_TIME" ,
    "EJECTION" ,
    "BODILY_INJURY" ,
    "PERSON_INJURY" ,
    "POSITION_IN_VEHICLE" ,
    "SAFETY_EQUIPMENT" ,
    "PERSON_TYPE" ,
    "PERSON_AGE" ,
    "PERSON_SEX",
    "EMOTIONAL_STATUS" ,
    "CONTRIBUTING_FACTOR_1" 
    
    ]

    sel_rename_P = {
    "UNIQUE_ID" : "unique_id",
    "COLLISION_ID" : "collision_id",
    "CRASH_DATE" : "crash_date",
    "CRASH_TIME" : "crash_time",
    "EJECTION" : "ejection",
    "BODILY_INJURY" : "body_inj",
    "PERSON_INJURY" : "person_inj",
    "POSITION_IN_VEHICLE" : "pos_in_vhc",
    "SAFETY_EQUIPMENT" : "safety_equip",
    "PERSON_TYPE" : "person_type",
    "PERSON_AGE" : "age",
    "PERSON_SEX" : "sex",
    "EMOTIONAL_STATUS" : "emot_status",
    "CONTRIBUTING_FACTOR_1" : "contr_f"
    }

    sel_types_P = {
    "unique_id" : pd.Int64Dtype(),
    "collision_id" : pd.Int64Dtype(),
    "ejection" : str,
    "body_inj" : str,
    "person_inj" : str,
    "pos_in_vhc" : str,
    "safety_equip" : str,
    "person_type" : str,
    "age" : pd.Int64Dtype(),
    "sex" :  str,
    "emot_status" : str,
    "contr_f" :  str
    }
    df = pd.read_csv(url_P, sep=',', dtype=sel_types_P)
    df = df[sel_P]
    df.rename(columns=sel_rename_P, inplace=True)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
