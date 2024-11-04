import pandas as pd

def GetSyntheticData():
    df = pd.DataFrame({
    'cloudy':   [1,1,1,0,0,0,0,0,1,0,0,1,0],
    'sprinkler':[0,0,0,1,1,1,0,1,0,0,0,0,0],
    'rain':     [1,1,0,0,0,0,1,0,1,0,0,0,0],
    'wet':      [1,1,0,1,1,0,0,0,1,0,1,0,0]
    })
    return df

def GetParentNames(bn, variable):
    parent_ids = bn.parents(variable)
    parent_names = [bn.variable(p).name() for p in parent_ids]
    return parent_names

def LearnParameters(bn, df):
    for name in bn.names():
        if len(bn.parents(name)) == 0: # Handle base case for variables with no parents
            frequency_count_negatives = len(df[df[name] == 0])
            frequency_count_positives = len(df[df[name] == 1])
            false_frequency = frequency_count_negatives / (frequency_count_negatives + frequency_count_positives)
            true_frequency = 1 - false_frequency
            bn.cpt(name)[:] = [false_frequency,true_frequency] 

        else:
            parents = GetParentNames(bn,name)
            frequency_count = df[parents + [name]].value_counts().to_frame().reset_index()
            frequency_count_positives = frequency_count[frequency_count[name]==1]
            frequency_count_negatives = frequency_count[frequency_count[name]==0]
            for row in frequency_count_positives.iterrows():
                dict = row[1].to_dict()
                parent_config = {p: dict[p] for p in parents}
                mask = (frequency_count_negatives[list(parent_config)] == pd.Series(parent_config)).all(axis=1)
                negative_occurences = frequency_count_negatives[mask].squeeze()
                n_negative_occurences = 0
                if(len(negative_occurences) != 0):
                    n_negative_occurences = negative_occurences['count']
                true_frequency = dict['count']/(dict['count'] + n_negative_occurences)
                false_frequency = 1 - true_frequency
                bn.cpt(name)[parent_config] = [false_frequency, true_frequency] 
    return bn