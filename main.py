from Service import Service
from CommonStrings import ApacheProjectsData, ClusterSise
from Log.Logger import LoggerInstance


def handle_page_repositories(repositories_list, s, log):
    r"""This function get a list of repositories data, save it, and extract and save the topics and contributors of each
    :param repositories_list: list of dictionaries.
    :param s: service instance
    """
    for repo in repositories_list:
        # evaluate topics and contributors for each repository
        repo_name = repo[ApacheProjectsData.name]  # repository name
        repo_id = repo[ApacheProjectsData.id]  # repository id
        log.info(f'***** Start handling repository: NAME-{repo_name} , GitHub ID-{repo_id}')
        for topic in repo[ApacheProjectsData.topics]:
            # handle all repository's topics
            log.info(f'Append repo id to topic - {topic}')
            s.add_repository_id_to_topic(topic, repo_id)  # save topic and append repository id
        log.info(f'Saving contributors.')
        s.save_all_apache_project_contributors(repo_name)  # save repository's contributors
        log.info(f'Saving repository.')
        rep_inner_id = s.save_repository(repo)
        log.info(f'Repository was saved with inner ID - {rep_inner_id}')


if __name__ == '__main__':
    log_location = f'{ClusterSise.project_domain}Log/main_logger.log'
    logger = LoggerInstance().get_logger('main', log_location)
    service = Service()
    page = 1  # initial page number for apache projects http requests
    logger.info(f'Get repositories of page number - {page}')
    try:
        repositories_data_list = service.get_apache_projects_data(page)  # get repositories
        while page <= service.number_of_pages_apache_projects_data: # len(repositories_data_list) > 0:
            # while current page number contain at least 1 repository.
            logger.info(f'Start handling repositories of page number - {page}')
            handle_page_repositories(repositories_data_list, service, logger)
            page += 1
            logger.info(f'Get repositories of page number - {page}')
            repositories_data_list = service.get_apache_projects_data(page)  # get repositories
    except Exception as err:
        logger.error(f'Error message - {err}')

