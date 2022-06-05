
import pandas as pd

!wget https://wals.info/languoid.tab?sEcho=1&iSortingCols=1&iSortCol_0=0&sSortDir_0=asc

lang = pd.read_csv("/content/languoid.tab?sEcho=1", sep="\t")
lang.to_csv("lang_data.csv")
