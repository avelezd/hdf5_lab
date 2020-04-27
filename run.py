#------------------------------------------------------------------------------
# Script name: run.py
# Description: Script to read HDF5 files and testing.
# Creation date: 28/03/2020
# Author: avelezd
#------------------------------------------------------------------------------

# import pdb
# import torch
import numpy as np
# import h5py
# import datetime
import sys, getopt
import logging
from os import walk, path

from experimental.mylogsetup import logfilesetup
from utils.constants import _source_path_, _output_path_
from exp001 import write_random_output_files, write_scalar_output_files, write_zeros_output_files
from exp001_2 import write_golden_dataset
from t4ctools.utils.eval import load_test_file, work_out_score
from t4ctools.benchmarks.naive_moving_average.naive_baseline_mavg import write_submission_files
# t4ctools.benchmarks.naive_moving_average.naive_baseline_mavg
# import HDF5Reader as h5r
# from t4ctools.utils.create_submissiontest_like import dummy_funk, write_output_files
# from t4ctools.utils.h5shape import load_test_file, print_shape                      

filename = __file__
logger = logfilesetup(filename.replace('.py',''))


def experiment001(inpath, outpath, inputvalue):
    
    logger.info('Inicia experimento 1')

    if inputvalue == '0':
        write_zeros_output_files(inpath, outpath)
    elif inputvalue =='random':
        write_random_output_files(inpath, outpath)
    else:
        write_scalar_output_files(inpath, outpath, inputvalue)
    
    logger.info('Fin experimento 1')

def experimento001_2(utcPlus2, utcPlus3, inpath, outpath):

    logger.info('Inicia experimento1_2')

    write_golden_dataset(utcPlus2, utcPlus3, inpath, outpath)

    logger.info('Fin experimento1_2')


def mse_filebyfile(goldenfile_path, submitfile_path):
    
    data_sub = load_test_file(goldenfile_path)
    data_golden = load_test_file(submitfile_path)

    mse = (np.square(np.subtract(data_sub,data_golden))).mean(axis=None)
    print('MSE: %s'%mse)

if __name__ == "__main__":
    
    #--------------------------------------------------------
    # Experimento Nro. 1 : Creacion de conjuntos de datos
    #--------------------------------------------------------
    
    # inpath = "datasets/input/experiments/databenchmark/reduce"
    # inpath = "datasets/output/golden"
    # outpath = "datasets/output/golden127/"
    # experiment001(inpath, outpath, '0')
    # experiment001(inpath, outpath, '127')
    # experiment001(inpath, outpath, 'random')

    #--------------------------------------------------------
    # Experimento Nro. 1 parte 2 : Crear conjnto de datos golden
    #--------------------------------------------------------
    # The following indicies are the start indicies of the 3 images to predict in the 288 time bins (0 to 287)
    # in each daily test file. These are time zone dependent. Berlin lies in UTC+2 whereas Istanbul and Moscow
    # lie in UTC+3.
    # utcPlus2 = [30, 69, 126, 186, 234]
    # utcPlus3 = [57, 114, 174,222, 258]
    
    # outpath_golden = "datasets/output/golden/"
    # experimento001_2(utcPlus2, utcPlus3, inpath, outpath_golden)
    
    #--------------------------------------------------------
    # Experimento Nro. 1 parte 3 : Ver la forma de todos los archivos en un directorio
    #--------------------------------------------------------

    # giet_dataset_shape(outpath_golden)
    
    #--------------------------------------------------------
    # Experimento Nro. 1 parte 4 : Evaluación de los modelos
    #--------------------------------------------------------
    # goldenfile_path = 'datasets/output/golden/Moscow/Moscow_test/20181209_100m_bins.h5'
    # submitfile_path = 'datasets/output/golden/Moscow/Moscow_test/20180303_100m_bins.h5'

    # mse_filebyfile(goldenfile_path, submitfile_path)

    #--------------------------------------------------------
    # Experimento Nro. 1 parte 5: generación y evaluación de varios  modelos
    #--------------------------------------------------------
    # inpath = "datasets/output/golden"
    # outpath = "datasets/output/datasets0to254/"
    # outpath_score = "datasets/score"
    # 
    # # conjunto de datos solo 127 (golden para prueba, valor medio para medir cambios en MSE)
    # inpath_golden = "datasets/output/golden127"

    # for idx in range(0,255):
    #     write_scalar_output_files(inpath, outpath, idx)
    #     outpath_submit = "%sscript_scalar_%s"%(outpath,idx)
    #     print(outpath_submit) 
    #     # breakpoint()
    #     work_out_score(outpath_submit, inpath_golden, outpath_score, 'script%s'%idx)
    #     # print(idx)
    # 

    #--------------------------------------------------------
    # Experimento Nro. 2: Evaluacion de modelos básicos contra realidad
    #--------------------------------------------------------
    # models = {}
    # 
    # # Models path
    # dsgolden = 'datasets/output/golden/'
    # 
    # models['zeros'] = 'datasets/output/200413143547_script_zeros'
    # models['random'] = 'datasets/output/200413143548_script_random'
    # models['scalar4'] = 'datasets/output/200413143548_script_scalar_4'
    # # Naive moving average model creation
    # # input_path = 'datasets/input/experiments/databenchmark/reduce/'
    # # output_path = 'datasets/output/naive_mavg'
    # # write_submission_files(input_path,output_path)

    # # Naive moving average model
    # models['naive_mavg2'] = 'datasets/output/naive_mavg2'
    # outpath_score = 'datasets/score/simplemodelsgolden2'

    # for model_name,model_path, in models.items():
    #     work_out_score(model_path, dsgolden, outpath_score, model_name)
    
    # Models performance
    # random = 0.3214129192961587
    # zeros = 0.02138380514871743
    # scalar4 = 0.02056545469289025
    # naive_mvag = 0.018106694281515144

    # -------------------------------------------------------
    # Experimento Nro. 2 parte 2: validando resultados del modelo
    # naive moving average
    # -------------------------------------------------------
    # dsgolden = 'datasets/output/golden/'
    # dsmavg = 'datasets/output/naive_mavg2'
    # outpath_score = 'datasets/score/naivemavg_golden2'
    # work_out_score(dsmavg, dsgolden, outpath_score, 'nmavg2')
    # 
    # goldenfile_path = 'datasets/output/golden/Berlin/Berlin_test/20180102_100m_bins.h5'
    # submitfile_path = 'datasets/output/naive_mavg2/Berlin/Berlin_test/20180102_100m_bins.h5'
    # mse_filebyfile(goldenfile_path, submitfile_path)

    # -------------------------------------------------------
    # Experimento Nro. 3: Ilustrar el comportamiento del MSE
    # -------------------------------------------------------
   
    # y = [11,20,19,17,10]
    y = [0,0,0,0,0]
    # y_bar = [12,18,19.5,18,9]
    y_bar = [0,18,19,18,0]
    summation = 0  #variable to store the summation of differences
    n = len(y) #finding total number of items in list
    for i in range (0,n):  #looping through each element of the list
      difference = y[i] - y_bar[i]  #finding the difference between observed and predicted value
      squared_difference = difference**2  #taking square of the differene
      summation = summation + squared_difference  #taking a sum of all the differences
    MSE = summation/n  #dividing summation by total values to obtain average
    print("The Mean Square Error is: ", MSE)
