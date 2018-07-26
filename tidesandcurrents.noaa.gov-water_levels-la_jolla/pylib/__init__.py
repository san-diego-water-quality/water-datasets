""" Example pylib functions"""


def row_generator(resource, doc, env, *args, **kwargs):
    """ An example row generator function.

    Reference this function in a Metatab file as the value of a Datafile:

            Datafile: python:pylib#row_generator

    The function must yield rows, with the first being headers, and subsequenct rows being data.

    :param resource: The Datafile term being processed
    :param doc: The Metatab document that contains the term being processed
    :param args: Positional arguments passed to the generator
    :param kwargs: Keyword arguments passed to the generator
    :return:


    The env argument is a dict with these environmental keys:

    * CACHE_DIR
    * RESOURCE_NAME
    * RESOLVED_URL
    * WORKING_DIR
    * METATAB_DOC
    * METATAB_WORKING_DIR
    * METATAB_PACKAGE

    It also contains key/valu pairs for all of the properties of the resource.

    """

    import requests
    from io import StringIO
    import csv
    from metapack.cli.core import prt

    ref = doc.reference('url_template')
    
    for i, year in enumerate(range(2000,2019)):
        url = ref.resolved_url.interpolate({'year':year})
   
        prt(url)
   
        r = requests.get(url)
        r.raise_for_status()
        
        f = StringIO(r.text)
        reader = csv.reader(f, delimiter=',')
        for j, row in enumerate(reader):
            
            if j == 0: # first row
                if i == 0: # first file
                    yield row # yield the header
                    continue
                else:
                    continue
        
            yield row
           
