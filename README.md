# loniapi

loniapi is a Python package to make calls to the LONI API. It can list all files associated with a group-id and download specific files.

## Installation

1. Download loniapi-0.1.tar.gz from [https://github.com/hndo-SageBionetworks/loni-api-source-distribution.git](https://github.com/hndo-SageBionetworks/loni-api-source-distribution.git)
2. Navigate to the file's location and unzip
```bash
tar xvzf loniapi-0.1.tar.gz 
``` 
3. Navigate to the unzipped directory
```bash
cd loniapi-0.1
```
4. Install package
```bash
python3 setup.py install
```
5. Install pandas if it is not already installed. and requests. or upgrade
```bash
pip3 install pandas
```

6. Create a config file in your home directory
```bash
cd ~
vim .loniApiConfig
```

7. Specify your group-id and loni log-in credentials
```bash
[<your-group-id>]
email = <your-email>
password = <your-password
```

## Usage

```python
from loniapi import LoniAPI
myAPI = LoniAPI.LoniAPI()

# Log-in using a group ID acquired from IDA/LONI
myAPI.login('ampad')

# get list of files associated with the group id
loniAPI.get_LONI_files()

# test download a few file types 
myAPI.download_LONI_file('1')   #is a pdf
myAPI.download_LONI_file('3')   #is a csv

# to download a specific file version
myAPI.download_LONI_file(file_id = '2', version = '2015-11-13') #is a pdf

# log out

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
