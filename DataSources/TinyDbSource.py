from tinydb import TinyDB, Query
from Log.Logger import LoggerInstance
from CommonStrings import ProjectContributorsJson, ApacheProjectsData, ClusterSise


def get_tiny_db(path):
    r""" Create\ Open tiny db in the given path, and return it.
    :param path: str
    :return: TinyDB
    """
    return TinyDB(path)


def add_multiple_docs(db, lst_of_dicts):
    r"""
    :param db: TinyDB
    :param lst_of_dicts: list of dictionaries (each dictionary is a document to insert)
    :return: list of ints (each int in index i is the inserted document’s ID in index i)
    """
    return db.insert_multiple(lst_of_dicts)


def add_doc(db, dict_with_data):
    r"""
    :param db: TinyDB
    :param dict_with_data: dictionary (each dictionary is a document to insert)
    :return: int (the inserted document’s ID)
    """
    return db.insert(dict_with_data)


class RepositoriesDB:
    db_location = f'{ClusterSise.project_domain}DB/repositories_db.json'
    log_location = f'{ClusterSise.project_domain}Log/repositories_logger.log'

    def __init__(self):
        self.logger = LoggerInstance().get_logger(self.__class__.__name__, self.log_location)
        self.db = get_tiny_db(self.db_location)
        self.Repo = Query()

    def get_repository_data_by_repo_name(self, repo_name):
        return self.db.get(self.Repo.name == repo_name)

    def get_repository_data_by_doc_id(self, rep_id):
        return self.db.get(doc_id=rep_id)

    def insert_new_repository(self, new_rep_data):
        self.logger.info(f'Starting insertion: GitHub ID:{new_rep_data[ApacheProjectsData.id]},'
                         f' name:{new_rep_data[ApacheProjectsData.name]}')
        id = add_doc(self.db, new_rep_data)
        self.logger.info(f'Insert new repository: inner ID-{id}, GitHub ID:{new_rep_data[ApacheProjectsData.id]},'
                         f' name:{new_rep_data[ApacheProjectsData.name]}')
        return id

    def insert_new_repositories(self, lst_of_new_reps_data):
        self.logger.info(f'Starting multiple repositories insertion.')
        ids = add_multiple_docs(self.db, lst_of_new_reps_data)
        self.logger.info(f'Multiple repositories inserted. Inner IDs list: {ids}.')
        return ids


class ContributorsDB:
    db_location = f'{ClusterSise.project_domain}DB/contributors_db.json'
    log_location = f'{ClusterSise.project_domain}Log/contributors_logger.log'

    def __init__(self):
        self.logger = LoggerInstance().get_logger(self.__class__.__name__, self.log_location)
        self.db = get_tiny_db(self.db_location)
        self.Contributor = Query()

    def get_contributor_data_by_repo_name(self, repo_name):
        return self.db.get(self.Contributor.name == repo_name)

    def search_contributor_data_by_id(self, contributor_id):
        return self.db.search(self.Contributor.id == contributor_id)

    def insert_contributor(self, contributor_data):
        self.logger.info(f'Starting insertion: GitHub ID:{contributor_data[ProjectContributorsJson.id_int]},'
                         f' Username:{contributor_data[ProjectContributorsJson.login]}')
        id = add_doc(self.db, contributor_data)
        self.logger.info(f'New contributor inserted: inner ID-{id},'
                         f' GitHub ID:{contributor_data[ProjectContributorsJson.id_int]},'
                         f' Username:{contributor_data[ProjectContributorsJson.login]}')
        return id

    def insert_new_contributors(self, lst_of_new_contributor_data):
        self.logger.info(f'Starting multiple contributors insertion.')
        ids = add_multiple_docs(self.db, lst_of_new_contributor_data)
        self.logger.info(f'Multiple contributors inserted. Inner IDs list: {ids}.')
        return ids


class TopicsDB:
    db_location = f'{ClusterSise.project_domain}DB/topics_db.json'
    log_location = f'{ClusterSise.project_domain}Log/topics_logger.log'
    NAME = 'name'
    REPOSITORIES_IDS = 'repositories_ids'

    def __init__(self):
        self.logger = LoggerInstance().get_logger(self.__class__.__name__, self.log_location)
        self.db = get_tiny_db(self.db_location)
        self.Topic = Query()

    def get_topic_by_repo_name(self, repo_name):
        return self.db.get(self.Contributor.name == repo_name)

    def get_topic_by_label(self, label):
        return self.db.get(self.Topic.name == label)

    def insert_topic(self, topic_label, rep_id):
        self.logger.info(f'Starting insertion: {self.NAME}-{topic_label} , {self.REPOSITORIES_IDS}-{rep_id}.')
        id = add_doc(self.db, {self.NAME: topic_label, self.REPOSITORIES_IDS: [rep_id]})  # insert new topic
        self.logger.info(f'New topic inserted: Inner ID-{id} , {self.NAME}-{topic_label} , {self.REPOSITORIES_IDS}-{rep_id}.')
        return id

    def add_rep_id_to_topic(self, topic_label, rep_id):
        self.logger.info(f'Append to topic-{topic_label} the repository-{rep_id}.')
        d = self.db.get(self.Topic.name == topic_label)[self.REPOSITORIES_IDS]
        d.append(rep_id)
        self.db.update({self.REPOSITORIES_IDS: d}, self.Topic.name == topic_label)  # add repository id


