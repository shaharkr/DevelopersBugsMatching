from Service import Service

if __name__ == '__main__':
    service = Service()
    data_page_1 = service.get_apache_projects_data(1)
    ids = service.save_repositories(data_page_1)
    print(ids)
    data_page_2 = service.get_apache_projects_data(2)
    ids.extend(service.save_repositories(data_page_2))
    print(ids)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
