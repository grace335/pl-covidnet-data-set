#!/usr/bin/env python                                            
#
# covidnet_train ds ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp
import subprocess


Gstr_title = """

                _     _            _    _             _        
               (_)   | |          | |  | |           (_)       
  ___ _____   ___  __| |_ __   ___| |_ | |_ _ __ __ _ _ _ __   
 / __/ _ \ \ / / |/ _` | '_ \ / _ \ __|| __| '__/ _` | | '_ \  
| (_| (_) \ V /| | (_| | | | |  __/ |_ | |_| | | (_| | | | | | 
 \___\___/ \_/ |_|\__,_|_| |_|\___|\__| \__|_|  \__,_|_|_| |_| 


"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       covidnet_train.py 

    SYNOPSIS

        python covidnet_train.py                                         \\
            [-h] [--help]                                               \\
            [--man]                                                     \\
            [--mode <MODE>]                                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            mkdir in out && chmod 777 out
            python covidnet_train.py   \\
                                in    out

    DESCRIPTION

        `covidnet_train.py` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--mode <MODE>] 
        If specify the mode to . 
        
        [--version]
        If specified, print version number and exit. 

"""


class Covidnet_train(ChrisApp):
    """
    run a COVID-NET training session.
    """
    AUTHORS                 = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'A ChRIS plugin to run a COVID-NET training session'
    CATEGORY                = ''
    TYPE                    = 'ds'
    DESCRIPTION             = 'run a COVID-NET training session'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--mode', dest='mode', type=str,
                          optional=False, help='running mode')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        if options.mode == "covidx":
            covidnet_dir = os.path.join(os.getcwd(), "COVID-Net") 
            #covidnet_data_dir = os.path.join(covidnet_dir, "data")
            #input_data_path = os.path.join(options.inputdir, "data")
            #input_model_path = os.path.join(options.inputdir, "model")
            print("calling create_COVIDx.py")
            os.chdir(covidnet_dir)
            os.system('python create_COVIDx_v3.py')

        # WIP for this part.
        #if options.mode == "train":
        #    print("Start COVID Net training.")


    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    chris_app = Covidnet_train()
    chris_app.launch()
