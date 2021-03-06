import pandas as pd

def put_file(filename, good, bad):
    good_df = pd.DataFrame()
    bad_df = pd.DataFrame()
    columns = ['Time', 'ID', 'Latitude', 'Longitude', 'Height', 'Code', 'Name']
    df = pd.read_csv(filename, sep=" ", header=None)
    df.columns = columns 
    for name in good:
        good_df = good_df.append(df[df.ID == name])
    for name in bad: 
        bad_df = bad_df.append(df[df.ID == name])
    good_df.to_csv('GoodTrack.txt', sep=' ', header=False, index=False)
    bad_df.to_csv('BadTrack.txt', sep=' ', header=False, index=False)