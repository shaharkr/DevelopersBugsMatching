import requests as requests
from Log.Logger import LoggerInstance
import http.client
from CommonStrings import GitApi, ClusterSise
import json


class ApiSource:
    log_location = f'{ClusterSise.project_domain}Log/api_source_logger.log'

    def __init__(self):
        self.logger = LoggerInstance().get_logger(self.__class__.__name__, self.log_location)

    def http_get_request_old(self, url, params=None):
        r"""
        :param url: URL for the http request.
        :param params: (optional) Dictionary.
        :return: requests.Response object.
        :raise: requests.exceptions.RequestException (, , times out or )
        """
        try:
            self.logger.info(f'Handle request - URL:{url} , PARAMS:{params}')
            response = requests.get(url=url, params=params)
            if response.status_code not in range(200, 300):
                self.logger.warning(f'Status response: {response.status_code}. URL: {url} , PARAMS: {params}')
                pass  # TODO: decide what to do with fail status code
            return response
        except requests.exceptions.RequestException as err:
            # ConnectionError - network problem
            # HTTPError - invalid http response
            # TooManyRedirects -If a request exceeds the configured number of maximum redirections (URL was bad)
            # Timeout
            self.logger.error(f'Failed handled get request. URL: {url} , PARAMS: {params}, MESSAGE: {err}')

    def http_get_request(self, url, params=None):
        r"""
        :param url: URL for the http request.
        :param params: (optional) Dictionary.
        :return: requests.Response object.
        :raise: requests.exceptions.RequestException (, , times out or )
        """
        try:
            self.logger.info(f'Handle request - URL:{GitApi.domain}{url} , PARAMS:{params}')
            conn = http.client.HTTPSConnection(GitApi.domain)
            headers = {
                'content-type': "application/json",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
                'authorization': f'Bearer {GitApi.tok}'
            }
            if params is not None:
                # add params to url
                suffix = '?'
                for param_name, param_val in params.items():
                    url += f'{suffix}{param_name}={param_val}'
                    suffix = '&'
            conn.request("GET", url, headers=headers)
            response = conn.getresponse()
            if response.code not in range(200, 300):
                self.logger.warning(f'Status response: {response.code}. URL: {GitApi.domain}{url} , PARAMS: {params}.'
                                    f'{response.read().decode("utf-8")}')
                pass  # TODO: decide what to do with fail status code
            data = response.read().decode("utf-8")
            if data is None or len(data) == 0:
                self.logger.error( f'Data is None or len = 0. URL: {GitApi.domain}{url} , PARAMS: {params}')
            to_ret = []
            try:
                to_ret = json.loads(data.replace("'", '"'))
            except Exception as err:
                self.logger.error(f'Failed handled get request. URL: {GitApi.domain}{url} , PARAMS: {params}, MESSAGE: {err}')
            finally:
                return to_ret
        except Exception as err:
            # ConnectionError - network problem
            # HTTPError - invalid http response
            # TooManyRedirects -If a request exceeds the configured number of maximum redirections (URL was bad)
            # Timeout
            self.logger.error(f'Failed handled get request. URL: {GitApi.domain}{url} , PARAMS: {params}, MESSAGE: {err}')



