from CommonStrings import GitApi, ProjectTopicsJson, ApacheProjectsData
from DataSources import ApiSource, TinyDbSource
import json


class Service:
    """
        A class used to get data from GitHub, and store it with TinyDB source
        ...
        Attributes
        ----------
        number_of_pages_apache_projects_data : int
            the maximum page in the get_all_apache_projects_data HTTP request
        git_source : ApiSource
            using for get data with REST API of GitHub
        rep_data_access : RepositoriesDB
            repositories data access. using for save, update and delete repositories data
        contributors_data_access : ContributorsDB
            contributors data access. using for save, update and delete contributors data
        """

    def __init__(self):
        self.number_of_pages_apache_projects_data = 78
        self.git_source = ApiSource.ApiSource()
        self.rep_data_access = TinyDbSource.RepositoriesDB()
        self.contributors_data_access = TinyDbSource.ContributorsDB()
        self.topics_data_access = TinyDbSource.TopicsDB()

    def get_all_apache_project_topics(self, project_name):
        """
        :param project_name: str
        :return: list of strings
        """
        url = GitApi.url_get_apache_project_topics.format(project_name=project_name)
        # response = self.git_source.http_get_request(url)
        # list_of_topics = response.json()[ProjectTopicsJson.names]
        list_of_topics = self.git_source.http_get_request(url)[ProjectTopicsJson.names]
        return list_of_topics

    def get_apache_projects_data(self, page_number=None):
        r"""
        :param page_number: int
        :return list_of_projects_data: list of dictionaries (Each dictionary represent repo)
        """
        url = GitApi.url_get_all_apache_projects_data
        params = None
        if page_number is not None:
            params = {GitApi.page_number_url_param: page_number}
        # response = self.git_source.http_get_request(url, params)
        # list_of_projects_data = response.json()
        list_of_projects_data = self.git_source.http_get_request(url, params)
        return list_of_projects_data

    def get_all_apache_projects_data(self):
        list_of_projects_data = []
        for i in range(1, self.number_of_pages_apache_projects_data + 1):
            list_of_projects_data.extend(self.get_apache_projects_data(i))
        return list_of_projects_data

    def get_apache_project_contributors(self, project_name, page_number=None):
        r"""
        :param page_number: int
        :return list_of_contributors: list of dictionaries (Each dictionary represent contributor)
        """
        url = GitApi.url_get_contributors_apache_project.format(project_name=project_name)
        params = None
        if page_number is not None:
            params = {GitApi.page_number_url_param: page_number}
        # response = self.git_source.http_get_request(url, params)
        # list_of_contributors = response.json()
        list_of_contributors = self.git_source.http_get_request(url, params)
        return list_of_contributors

    def get_all_apache_project_contributors(self, project_name):
        # TODO: I was unable to determine the number of pages for each repository.
        list_of_contributors = []
        page = 1
        list_returned = self.get_apache_project_contributors(project_name, page)
        while len(list_returned) > 0:
            list_of_contributors.extend(list_returned)
            page += 1
            list_returned = self.get_apache_project_contributors(project_name, page)
        return list_of_contributors

    def save_all_apache_project_contributors(self, project_name):
        page = 1
        list_returned = self.get_apache_project_contributors(project_name, page)
        while len(list_returned) > 0:
            self.contributors_data_access.insert_new_contributors(list_returned)
            page += 1
            list_returned = self.get_apache_project_contributors(project_name, page)
        return True

    def save_repository(self, rep_data_dict):
        # TODO: consider format validation check
        # b = self.check_repo_data_dict_has_right_format(rep_data_dict)
        # if not b:
        #     m = 'The dictionary not in the right format.\n' \
        #         'To get the right format, go to CommonStrings, an find it inApacheProjectsData'
        #     raise ValueError(m)
        new_id = self.rep_data_access.insert_new_repository(rep_data_dict)
        return new_id

    def save_repositories(self, lst_reps_data_dicts):
        # TODO: consider format validation check
        # b = self.check_repo_data_dict_has_right_format(rep_data_dict)
        # if not b:
        #     m = 'The dictionary not in the right format.\n' \
        #         'To get the right format, go to CommonStrings, an find it inApacheProjectsData'
        #     raise ValueError(m)
        new_ids = self.rep_data_access.insert_new_repositories(lst_reps_data_dicts)
        return new_ids

    def save_contributors(self, lst_contributors_data_dicts):
        new_ids = self.contributors_data_access.insert_new_contributors(lst_contributors_data_dicts)
        return new_ids

    def add_repository_id_to_topic(self, topic_label, repo_id):
        if self.topics_data_access.db.contains(self.topics_data_access.Topic.name == topic_label):
            # topic is already in db
            self.topics_data_access.add_rep_id_to_topic(topic_label, repo_id)
        else:
            # topic isn't existing in db
            self.topics_data_access.insert_topic(topic_label, repo_id)
