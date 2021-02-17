# -*- coding: utf-8 -*-
# @Author: Claire-Eleuthèriane Gerrer
# @Date:   2020-02-14 16:26:56
# @Last Modified by:   Claire-Eleuthèriane Gerrer
# @Last Modified time: 2020-07-30 15:13:14

from __future__ import division
import numpy as np
import fmpy
# import homemade_fmpy as fmpy # TRICKY: REPLACE OFFICIAL LIBRARY BY MINE
import pandas as pd


def get_recommended_dict():
    dic = {
        "validate": False, "fmi_type": "ModelExchange", "solver": "CVode",
        "relative_tolerance": 1e-6}
    return dic


def instantiate(path_fmu, **kwargs):
    unzipdir = fmpy.extract(path_fmu)
    model_description = fmpy.read_model_description(unzipdir)
    fmu_instance = fmpy.instantiate_fmu(
        unzipdir, model_description, kwargs["fmi_type"])
    return fmu_instance


def simulate_on_doe(list_input, doe_data, path_fmu, **kwargs):
    """ Simulate the model on a design of experiment.
    Return a list of trajectories for several outputs..
    Inputs:
        list_input -- list of strings (name of inputs),
        doe_data -- list of list of floats (the design of experiment),
        final time -- float,
        output_interval -- float.
    Output:
        list_result -- list pd Dataframes.
    """
    list_result = []
    sample_size = doe_data.shape[0]
    # fmu_instance = instantiate(path_fmu, **kwargs)
    for ii in range(sample_size):
        # fmu_instance.reset()
        point = doe_data[ii]
        dic = dict(zip(list_input, point))
        try:
            kwargs["start_values"].update(dic)
        except KeyError:
            kwargs["start_values"] = dic
        print(ii)
        try:
            result = fmpy.simulate_fmu(path_fmu, **kwargs)
            result = pd.DataFrame(result)
            result = result.set_index("time")
        except TypeError as typ:
            print(typ)
        except Exception as exc:
            print(exc)
            result = pd.DataFrame([np.NaN])
        list_result.append(result)
    # fmu_instance.freeInstance()
    return list_result


def simulate_trajectory(list_input, doe_data, path_fmu, **kwargs):
    """ Simulate the model on a design of experiment.
    Return the trajectory of each simulation.
    Inputs:
        list_input -- list of strings (name of inputs),
        doe_data -- array of floats (the design of experiment),
        final time -- float,
        output_interval -- float.
    Output:
        .df_trajectory -- dataframe of single output's trajectory
    """

    list_result = simulate_on_doe(
        list_input, doe_data, path_fmu, **kwargs)
    # assert there is only one output
    df = list_result[0]
    if len(df.columns) > 1:
        raise AssertionError("Trajectory of one output only.")
    else:
        pass
    # gather the trajectories
    df_trajectory = pd.DataFrame(columns=df.index)
    for df in list_result:
        df_trajectory = df_trajectory.append(df.transpose())
    df_trajectory.index = list(range(len(list_result)))
    return df_trajectory


def simulate_final(
        list_input, doe_data, path_fmu, rename_final=False, **kwargs):
    """ Simulate the model on a design of experiment.
    Return the final values of all outputs fors each simulation.
    Inputs:
        list_input -- list of strings (name of inputs),
        doe_data -- array of floats (the design of experiment),
        final time -- float,
        output_interval -- float.
    Output:
        .df_final -- dataframe of several output's final values
    """

    list_result = simulate_on_doe(list_input, doe_data, path_fmu, **kwargs)
    # gather the final values
    list_index = []
    list_df = []
    for ii in range(len(list_result)):
        df = list_result[ii]
        if type(df) == float:
            print("Simu {} failed".format(ii))
        else:
            list_index.append(ii)
            list_df.append(df.iloc[-1])
    list_output = df.columns
    df_final = pd.DataFrame(list_df, columns=list_output, index=list_index)
    if rename_final:
        df_final.columns = [string + "-final" for string in list_output]
    # concatenate with input data
    df_input = pd.DataFrame(doe_data, columns=list_input)
    df_return = pd.concat([df_input, df_final], axis="columns")
    return df_return
