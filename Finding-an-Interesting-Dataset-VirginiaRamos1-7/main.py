import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data = pandas.read_csv("heart_failure_clinical_.csv")