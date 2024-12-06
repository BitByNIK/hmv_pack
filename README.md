# HANDLING MISSING DATA

```
PROJECT 3, UCS633 - Data Analysis and Visualization
Nikhil Gupta  
COE17
Roll number: 101703371
```
Output is the dataset which contains no missing values and this dataset is streamed to a new csv file whose name is provided by the user.

## Installation
`pip install hmvpack_NG`

*Note the name has an underscore not a hyphen. If installation gives error or package is not found after installing, install as sudo.*

*Recommended - test it out in a virtual environment.* 

## To use via command line
The package contains two functions i.e there are two ways of handling missing data. First two arguments are same for accessing both functions. 

1) Deleting the row with missing values.

`HMVcli infile.csv outfile.csv D`

2) Replacing the missing values by mean of the values of that particular feature

`HMVcli infile.csv outfile.csv R`

## To use in .py script

For Deletion function -> 

```
from hmvlib.models import delete_record
delete_record('infile.csv', 'oufile.csv')
```

For Replacement function -> 

```
from hmvlib.models import replace_record
replace_record('infile.csv', 'oufile.csv')
```

*Can email me for any issues or suggestions*
