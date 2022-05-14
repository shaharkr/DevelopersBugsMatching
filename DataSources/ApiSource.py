import requests as requests


class ApiSource:

    def http_get_request(self, url, params=None):
        r"""
        :param url: URL for the http request.
        :param params: (optional) Dictionary.
        :return: requests.Response object.
        :raise: requests.exceptions.RequestException (, , times out or )
        """
        try:
            response = requests.get(url=url, params=params)
            if response.status_code not in range(200, 300):
                pass  # TODO: decide what to do with fail status code
            return response
        except requests.exceptions.RequestException as err:
            # ConnectionError - network problem
            # HTTPError - invalid http response
            # TooManyRedirects -If a request exceeds the configured number of maximum redirections (URL was bad)
            # Timeout
            raise SystemExit(err)



