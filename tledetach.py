import pandas as pd

from args import args

# The instructions from https://celestrak.com/columns/v04n03/ were followed to separate the Lines positions

def detach(tle_list):
    df_tle = pd.DataFrame(tle_list, columns=['ObjectName', 'Line1', 'Line2'])

    for item in tle_list:
        line1 = item[1].strip()
        line2 = item[2].strip()

        # Detach Line1
        noradid = line1[2:7]
        classification = line1[7]
        designator = line1[9:17]
        epoch_year = line1[18:20]
        epoch_day = line1[20:32]
        fstder = line1[33:43]
        sndder = line1[44:52]
        bdrag = line1[53:61]
        eltype = line1[62]
        elset = line1[64:68]

        # Detach Line2
        inclination = line2[8:16]
        ascend_mode = line2[17:25]
        eccentricity = line2[26:33]
        perigee = line2[34:42]
        mean_anomaly = line2[43:51]
        mean_motion = line2[52:63]
        revolution = line2[63:68]

        df_tle['NoradID'] = noradid
        df_tle['Classification'] = classification
        df_tle['Designator'] = designator
        df_tle['EpochYear'] = epoch_year
        df_tle['EpochDay'] = epoch_day
        df_tle['1stMeanDer'] = fstder
        df_tle['2ndMeanDer'] = sndder
        df_tle['BDrag'] = bdrag
        df_tle['ElSetTyme'] = eltype
        df_tle['ElementNumber'] = elset
        df_tle['Inclination'] = inclination
        df_tle['RighAscension'] = ascend_mode
        df_tle['Eccentricity'] = eccentricity
        df_tle['Perigee'] = perigee
        df_tle['MeanAnomaly'] = mean_anomaly
        df_tle['MeanMotion'] = mean_motion
        df_tle['Revolution'] = revolution

    print(df_tle)

    #Change output in args.py
    df_tle.to_csv(args['output_csv'])

