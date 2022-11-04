library("tidyverse")

# Create dataframe from downloaded dataset, and adding column names from the documentation
corpus <- readLines("medicine.txt")

print(corpus)

# Creating clean file in new subfolder
write_csv(df, "data/clean_flag.csv")