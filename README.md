![Python application](https://github.com/multicloud-ops/operator-csv-libs/workflows/Python%20application/badge.svg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=multicloud-ops_operator-csv-libs&metric=alert_status)](https://sonarcloud.io/dashboard?id=multicloud-ops_operator-csv-libs)
# Operator CSV libs

## Usage

Place `git+git://github.com/multicloud-ops/operator-csv-libs.git@master` in your requirements.txt file or run `pip install git+git://github.com/multicloud-ops/operator-csv-libs.git@master`. 
  
Then import the library into your scrips using some form of an import statement:
```
from operator-csv-libs.csv import ClusterServiceVersion
import operator-csv-libs.package as package
```