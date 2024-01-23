import time

import requests
import numpy as np

offices = np.array([])
# The API endpoint
response = {}
n = 1
while response != None:

    url = "https://api.fbi.gov/wanted/v1/list?page=" + str(n)


    # A GET request to the API
    response = requests.get(url)

    if (response):

        print(f'Buscando en la página {n}')
        print(n)
        n += 1
        raw_response_json = response.json()


        suspects = raw_response_json["items"]

        for n, s in enumerate(suspects):
            suspect_offices = suspects[n]['field_offices']

            # Check if suspect_offices is not None before iteration
            if suspect_offices is not None:
                suspect_offices = ['none' if office is None else office for office in suspect_offices]

                for office in suspect_offices:
                    offices = np.append(offices, office)
            else:
                offices = np.append(offices, 'ninguna oficina')

        result = np.column_stack(np.unique(offices, return_counts=True))

        sorted_result = result[result[:, 1].astype(int).argsort()[::-1]]

        print(sorted_result)


    else:
        print(response)
        exit()

    time.sleep(120)