# parser

Stores Python code to take our existing data dump and parse it into an array of dictionaries. Each dictionary contains two keys: the `url` of the sample, and the `result`, which is how the data was classified: `malicious`, `clean`, or `error`.

# data-sets

Stores Python code to take our data file and a `size` parameter and parse it into two sets of data: training and testing. Each will have exactly `size` malicious and clean results. Currently, these are created as arrays of dictionaries (soon to be written to files).
