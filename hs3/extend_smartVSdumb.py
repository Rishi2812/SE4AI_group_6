import sys
import random
import argparse
from ezr import *  # import everything from ezr 

# Data lists
Low_dim_data_list = [
    "data/optimize/misc/auto93.csv", 
    "data/optimize/config/SS-H.csv", 
    "data/optimize/config/SS-B.csv",
    "data/optimize/config/SS-G.csv",
    "data/optimize/config/SS-F.csv",
    "data/optimize/config/SS-D.csv",
    "data/optimize/config/wc+wc-3d-c4-obj1.csv",
    "data/optimize/config/wc+sol-3d-c4-obj1.csv",
    "data/optimize/config/wc+rs-3d-c4-obj1.csv",
    "data/optimize/config/SS-I.csv",
    "data/optimize/config/SS-C.csv",
    "data/optimize/config/SS-A.csv",
    "data/optimize/config/SS-E.csv",
    "data/optimize/hpo/healthCloseIsses12mths0011-easy.csv",
    "data/optimize/hpo/healthCloseIsses12mths0001-hard.csv"
]

High_dim_data_list = [
    "data/optimize/config/Apache_AllMeasurements.csv",
    "data/optimize/config/SS-P.csv",
    "data/optimize/config/SS-L.csv",
    "data/optimize/config/SS-O.csv",
    "data/optimize/misc/Wine_quality.csv",
    "data/optimize/process/pom3d.csv",
    "data/optimize/config/SS-S.csv",
    "data/optimize/config/SS-J.csv",
    "data/optimize/config/SS-K.csv",
    "data/optimize/config/rs-6d-c3_obj2.csv",
    "data/optimize/config/rs-6d-c3_obj1.csv",
    "data/optimize/config/wc-6d-c1-obj1.csv",
    "data/optimize/config/sol-6d-c2-obj1.csv",
    "data/optimize/config/SS-X.csv",
    "data/optimize/process/pom3c.csv",
    "data/optimize/process/pom3b.csv",
    "data/optimize/process/pom3a.csv",
    "data/optimize/process/nasa93dem.csv",
    "data/optimize/config/SQL_AllMeasurements.csv",
    "data/optimize/config/SS-U.csv",
    "data/optimize/process/coc1000.csv",
    "data/optimize/config/SS-M.csv",
    "data/optimize/config/X264_AllMeasurements.csv",
    "data/optimize/config/SS-R.csv",
    "data/optimize/config/HSMGP_num.csv",
    "data/optimize/config/SS-Q.csv",
    "data/optimize/process/xomo_osp2.csv",
    "data/optimize/process/xomo_osp.csv",
    "data/optimize/process/xomo_ground.csv",
    "data/optimize/process/xomo_flight.csv",
    "data/optimize/config/SS-N.csv",
    "data/optimize/config/SS-W.csv",
    "data/optimize/config/SS-V.csv",
    "data/optimize/config/SS-T.csv"
]

def report(option='high'):
    if option == 'low':
        data_list = Low_dim_data_list
    elif option == 'high':
        data_list = High_dim_data_list
    else:
        raise ValueError("Invalid option. Choose 'low' or 'high'.")

    for data in data_list:
        print(f"THE DATA {data} ----")
        for N in (20, 30, 40, 50):
            somes = []
            d = DATA().adds(csv(data))
            dumb = [guess(N, d) for _ in range(20)]
            dumb = [d.chebyshev(lst[0]) for lst in dumb]
            dumb.sort()
            
            the.Last = N
            smart = [d.shuffle().activeLearning() for _ in range(20)]
            smart = [d.chebyshev(lst[0]) for lst in smart]
            smart.sort()
            somes += [stats.SOME(dumb, f"dumb,{N}")]
            somes += [stats.SOME(smart, f"smart,{N}")]
            stats.report(somes)
        print("------")

def guess(N, d):
    some = random.choices(d.rows, k=N)
    return d.clone().adds(some).chebyshevs().rows

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Choose dataset type for analysis.")
    parser.add_argument('option', choices=['low', 'high'], help="Specify 'low' for low-dimensional datasets or 'high' for high-dimensional datasets")
    args = parser.parse_args()
    
    report(args.option)
