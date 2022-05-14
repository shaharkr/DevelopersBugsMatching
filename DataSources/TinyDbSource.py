from tinydb import TinyDB, Query


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
    location = 'DB/repositories_db.json'

    def __init__(self):
        self.db = get_tiny_db(self.location)
        self.Repo = Query()

    def get_repository_data_by_repo_name(self, repo_name):
        return self.db.get(self.Repo.name == repo_name)

    def get_repository_data_by_doc_id(self, id):
        return self.db.get(doc_id=id)

    def insert_new_repository(self, new_rep_data):
        return add_doc(self.db, new_rep_data)

    def insert_new_repositories(self, lst_of_new_reps_data):
        return add_multiple_docs(self.db, lst_of_new_reps_data)
