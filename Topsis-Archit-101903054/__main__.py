import math
import sys
import pandas as pd
from operator import add, truediv

try:
    def topsis(inputFile, weights, impacts, outputFileName):
        df = pd.read_csv(inputFile)
        if len(df.columns) < 3:
            raise Exception("Minimum number of columns in the input file must be 3!")

        for col in df.columns[1:]:
            for x in df[col]:
                if not isinstance(x, int) and not isinstance(x, float):
                    raise Exception("Input file contains non numeric values, please input the correct data!")

        weights = weights.split(",")
        impacts = impacts.split(",")

        if len(weights) != len(df.columns[1:]) or len(impacts) != len(df.columns[1:]):
            raise Exception("Weights and Impacts should be equal to the number of features in the input file!, check for the commas while giving arguments!")

        for impact in impacts:
            if impact not in ['-', '+']:
                raise Exception("Impacts can either be + or -, pls check!")
        idealBest = ["Best"]
        idealWorst = ["Worst"]
        for col, w, i in zip(df.columns[1:], weights, impacts):
            df[col] = (df[col]/math.sqrt(df[col].pow(2).sum())) * int(w)
            if i == '-':
                idealBest.append(df[col].min())
                idealWorst.append(df[col].max())
            else:
                idealBest.append(df[col].max())
                idealWorst.append(df[col].min())
        df.loc[len(df)] = idealBest
        df.loc[len(df)] = idealWorst
        eucBest = []
        eucWorst = []
        for i in range(len(df)):
            eucBest.append(math.sqrt(((df.iloc[i, 1:] - df.iloc[len(df) - 2, 1:]) ** 2).sum()))
            eucWorst.append(math.sqrt(((df.iloc[i, 1:] - df.iloc[len(df) - 1, 1:]) ** 2).sum()))

        eucTotal = list(map(add, eucBest, eucWorst))
        eucTotal.pop()
        eucTotal.pop()
        performanceScore = list(map(truediv, eucWorst, eucTotal))
        df.drop(df.tail(2).index, inplace=True)
        df["Topsis Score"] = performanceScore
        rank = df["Topsis Score"].rank(ascending=0)
        df["Rank"] = rank
        df.to_csv(outputFileName, index=False)

    if __name__ == '__main__':
        if len(sys.argv) < 5:
            raise Exception("Invalid number Arguments!, Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
except Exception as e:
    print(e)

