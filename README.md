
# Water Project Datasets

These data packages are part of the [San Diego Water Quality Data
Project](http://water.sandiegodata.org/). The ``source`` directory contains
data packages for original extracts from upstream soruces, and the ``derived``
directory holds processed packages that combine multiple measures and add
features.

## Building the Datasets

First thing is to install the Python modules in requirements.txt, usually: 

    make install

To build all of the datasets, run ``make``. The key targets are: 

* ``make build``: build all of the datasets
* ``make s3``: Build, then upload to s3
* ``make ckan``: Build, upload to s3, then submit to CKAN. 


The S3 target requires S3 credentials to be set for boto for the bucket
``library.metatab.org``, which is usually done with either:

* A credentials file in ~/.aws/credentials
* Environmental variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY

Refer to the [boto
credentials](https://boto3.readthedocs.io/en/latest/guide/configuration.html)
documentataion for details.

The ckan target requires two environmental variable to be set: 

* ``METAKAN_CKAN_URL``, with the base URL to the CKAN repository
* ``METAKAN_API_KEY``, With the API key for an account, which you can get from a user's page in CKAN. 

There are also clean targets for all of the build targets: 

* ``clean-build``
* ``clean-s3``
* ``clean-ckan``

## Using Datasets

These datasets are all published to the [Data Library's CKAN Repo](https://data.sandiegodata.org/dataset?tags=water-project), so it's easiest to get them from there. 

If you are building the datasets for local analysis, you'll probably want to index them and use them through the index. First, build the datasets with make, then index them: 

    make index

Then you can check the index by listing the dataset with:

    mp search -l 

Or search for one with : 

    mp search beachwatch 

Now you can use the names in package names that have an 'index:' prefix, usually also with the version number removed. For instance: 

    mp run index:sandiegodata.org-beachwatch#stations
    
Or, in Python/Jupyter:     

    import metapack as mp
    mp.jupyter.init()
    pkg = mp.open_package('index:sandiegodata.org-beachwatch#stations')
    df = pkg.default_resource.read_csv()
    print(df.head())
