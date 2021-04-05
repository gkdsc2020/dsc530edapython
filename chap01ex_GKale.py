"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

# import numpy as np
import sys

import nsfg
import thinkstats2


def read_fem_resp(dict_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz', nrows=None):
    resp_dict = thinkstats2.ReadStataDct(dict_file)
    df_resp = resp_dict.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    clean_fem_resp(df_resp)
    return df_resp


def clean_fem_resp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass


def validate_preg_num(resp):

    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)

    # iterate through the respondent pregnum series
    for idx, pregnum in resp.pregnum.items():
        caseid = resp.caseid[idx]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = read_fem_resp()
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(validate_preg_num(resp))
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
