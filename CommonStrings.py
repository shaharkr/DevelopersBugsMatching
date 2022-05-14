
class GitApi:
    url_get_all_apache_projects_data = 'https://api.github.com/orgs/apache/repos'
    url_get_apache_project_topics = 'https://api.github.com/repos/apache/{project_name}/topics'
    url_get_contributors_apache_project = 'https://api.github.com/repos/apache/{project_name}/contributors'  # TODO: handle multiple pages
    page_number_url_param = 'page'  # Params names for url


class ProjectTopicsJson:
    names = 'names'


class ProjectContributorsJson:
    login = "login"
    id_int = "id"
    node_id_str = "node_id"
    avatar_url = "avatar_url"
    gravater_id_str = " gravatar_id"
    url = "url"
    html_url = "html_url"
    followers_url = "followers_url"
    following_url = "following_url"
    gists_url = "gists_url"
    starred_url = "starred_url"
    subscriptions_url = "subscriptions_url"
    organizations_url = "organizations_url"
    repos_url = "repos_url"
    events_url = "events_url"
    received_events_url = "received_events_url"
    type = "type"
    site_admin_boolean = "site_admin"
    contributions_int = "contributions"
    json_response_fields = [login, id_int, node_id_str, avatar_url, gravater_id_str, url, html_url,
                            followers_url, following_url, gists_url, starred_url, subscriptions_url,
                            organizations_url, repos_url, events_url, received_events_url, type,
                            site_admin_boolean, contributions_int]


class ApacheProjectsData:
    # There is much more data fields
    id = 'id'
    node_id_str = 'node_id'
    name = 'name'
    full_name = 'full_name'  # full_name is- apache/{repo_name}
    private_boolean = 'private'
    owner_dict = 'owner'  # dictionary with data like in ProjectContributorsJson
    created_date = 'created_at'
    size_int = 'size'
    topics = 'topics'  # the same list that returned in url_get_apache_project_topics request

    response_schema = {
                      "type": "array",
                      "items": {
                        "title": "Minimal Repository",
                        "description": "Minimal Repository",
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "examples": [
                              1296269
                            ]
                          },
                          "node_id": {
                            "type": "string",
                            "examples": [
                              "MDEwOlJlcG9zaXRvcnkxMjk2MjY5"
                            ]
                          },
                          "name": {
                            "type": "string",
                            "examples": [
                              "Hello-World"
                            ]
                          },
                          "full_name": {
                            "type": "string",
                            "examples": [
                              "octocat/Hello-World"
                            ]
                          },
                          "owner": {
                            "title": "Simple User",
                            "description": "Simple User",
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "email": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "login": {
                                "type": "string",
                                "examples": [
                                  "octocat"
                                ]
                              },
                              "id": {
                                "type": "integer",
                                "examples": [
                                  1
                                ]
                              },
                              "node_id": {
                                "type": "string",
                                "examples": [
                                  "MDQ6VXNlcjE="
                                ]
                              },
                              "avatar_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://github.com/images/error/octocat_happy.gif"
                                ]
                              },
                              "gravatar_id": {
                                "type": [
                                  "string",
                                  "null"
                                ],
                                "examples": [
                                  "41d064eb2195891e12d0413f63227ea7"
                                ]
                              },
                              "url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/users/octocat"
                                ]
                              },
                              "html_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://github.com/octocat"
                                ]
                              },
                              "followers_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/users/octocat/followers"
                                ]
                              },
                              "following_url": {
                                "type": "string",
                                "examples": [
                                  "https://api.github.com/users/octocat/following{/other_user}"
                                ]
                              },
                              "gists_url": {
                                "type": "string",
                                "examples": [
                                  "https://api.github.com/users/octocat/gists{/gist_id}"
                                ]
                              },
                              "starred_url": {
                                "type": "string",
                                "examples": [
                                  "https://api.github.com/users/octocat/starred{/owner}{/repo}"
                                ]
                              },
                              "subscriptions_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/users/octocat/subscriptions"
                                ]
                              },
                              "organizations_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/users/octocat/orgs"
                                ]
                              },
                              "repos_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/users/octocat/repos"
                                ]
                              },
                              "events_url": {
                                "type": "string",
                                "examples": [
                                  "https://api.github.com/users/octocat/events{/privacy}"
                                ]
                              },
                              "received_events_url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/users/octocat/received_events"
                                ]
                              },
                              "type": {
                                "type": "string",
                                "examples": [
                                  "User"
                                ]
                              },
                              "site_admin": {
                                "type": "boolean"
                              },
                              "starred_at": {
                                "type": "string",
                                "examples": [
                                  "\"2020-07-09T00:17:55Z\""
                                ]
                              }
                            },
                            "required": [
                              "avatar_url",
                              "events_url",
                              "followers_url",
                              "following_url",
                              "gists_url",
                              "gravatar_id",
                              "html_url",
                              "id",
                              "node_id",
                              "login",
                              "organizations_url",
                              "received_events_url",
                              "repos_url",
                              "site_admin",
                              "starred_url",
                              "subscriptions_url",
                              "type",
                              "url"
                            ]
                          },
                          "private": {
                            "type": "boolean"
                          },
                          "html_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "https://github.com/octocat/Hello-World"
                            ]
                          },
                          "description": {
                            "type": [
                              "string",
                              "null"
                            ],
                            "examples": [
                              "This your first repo!"
                            ]
                          },
                          "fork": {
                            "type": "boolean"
                          },
                          "url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "https://api.github.com/repos/octocat/Hello-World"
                            ]
                          },
                          "archive_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}"
                            ]
                          },
                          "assignees_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/assignees{/user}"
                            ]
                          },
                          "blobs_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}"
                            ]
                          },
                          "branches_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/branches{/branch}"
                            ]
                          },
                          "collaborators_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}"
                            ]
                          },
                          "comments_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/comments{/number}"
                            ]
                          },
                          "commits_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/commits{/sha}"
                            ]
                          },
                          "compare_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}"
                            ]
                          },
                          "contents_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/contents/{+path}"
                            ]
                          },
                          "contributors_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/contributors"
                            ]
                          },
                          "deployments_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/deployments"
                            ]
                          },
                          "downloads_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/downloads"
                            ]
                          },
                          "events_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/events"
                            ]
                          },
                          "forks_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/forks"
                            ]
                          },
                          "git_commits_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}"
                            ]
                          },
                          "git_refs_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}"
                            ]
                          },
                          "git_tags_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}"
                            ]
                          },
                          "git_url": {
                            "type": "string"
                          },
                          "issue_comment_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}"
                            ]
                          },
                          "issue_events_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}"
                            ]
                          },
                          "issues_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/issues{/number}"
                            ]
                          },
                          "keys_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}"
                            ]
                          },
                          "labels_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/labels{/name}"
                            ]
                          },
                          "languages_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/languages"
                            ]
                          },
                          "merges_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/merges"
                            ]
                          },
                          "milestones_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/milestones{/number}"
                            ]
                          },
                          "notifications_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}"
                            ]
                          },
                          "pulls_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/pulls{/number}"
                            ]
                          },
                          "releases_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/releases{/id}"
                            ]
                          },
                          "ssh_url": {
                            "type": "string"
                          },
                          "stargazers_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/stargazers"
                            ]
                          },
                          "statuses_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}"
                            ]
                          },
                          "subscribers_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/subscribers"
                            ]
                          },
                          "subscription_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/subscription"
                            ]
                          },
                          "tags_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/tags"
                            ]
                          },
                          "teams_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/teams"
                            ]
                          },
                          "trees_url": {
                            "type": "string",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}"
                            ]
                          },
                          "clone_url": {
                            "type": "string"
                          },
                          "mirror_url": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "hooks_url": {
                            "type": "string",
                            "format": "uri",
                            "examples": [
                              "http://api.github.com/repos/octocat/Hello-World/hooks"
                            ]
                          },
                          "svn_url": {
                            "type": "string"
                          },
                          "homepage": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "language": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "forks_count": {
                            "type": "integer"
                          },
                          "stargazers_count": {
                            "type": "integer"
                          },
                          "watchers_count": {
                            "type": "integer"
                          },
                          "size": {
                            "type": "integer"
                          },
                          "default_branch": {
                            "type": "string"
                          },
                          "open_issues_count": {
                            "type": "integer"
                          },
                          "is_template": {
                            "type": "boolean"
                          },
                          "topics": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "has_issues": {
                            "type": "boolean"
                          },
                          "has_projects": {
                            "type": "boolean"
                          },
                          "has_wiki": {
                            "type": "boolean"
                          },
                          "has_pages": {
                            "type": "boolean"
                          },
                          "has_downloads": {
                            "type": "boolean"
                          },
                          "archived": {
                            "type": "boolean"
                          },
                          "disabled": {
                            "type": "boolean"
                          },
                          "visibility": {
                            "type": "string"
                          },
                          "pushed_at": {
                            "type": [
                              "string",
                              "null"
                            ],
                            "format": "date-time",
                            "examples": [
                              "2011-01-26T19:06:43Z"
                            ]
                          },
                          "created_at": {
                            "type": [
                              "string",
                              "null"
                            ],
                            "format": "date-time",
                            "examples": [
                              "2011-01-26T19:01:12Z"
                            ]
                          },
                          "updated_at": {
                            "type": [
                              "string",
                              "null"
                            ],
                            "format": "date-time",
                            "examples": [
                              "2011-01-26T19:14:43Z"
                            ]
                          },
                          "permissions": {
                            "type": "object",
                            "properties": {
                              "admin": {
                                "type": "boolean"
                              },
                              "maintain": {
                                "type": "boolean"
                              },
                              "push": {
                                "type": "boolean"
                              },
                              "triage": {
                                "type": "boolean"
                              },
                              "pull": {
                                "type": "boolean"
                              }
                            }
                          },
                          "role_name": {
                            "type": "string",
                            "examples": [
                              "admin"
                            ]
                          },
                          "template_repository": {
                            "anyOf": [
                              {
                                "type": "null"
                              },
                              {
                                "title": "Repository",
                                "description": "A git repository",
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "description": "Unique identifier of the repository",
                                    "type": "integer",
                                    "examples": [
                                      42
                                    ]
                                  },
                                  "node_id": {
                                    "type": "string",
                                    "examples": [
                                      "MDEwOlJlcG9zaXRvcnkxMjk2MjY5"
                                    ]
                                  },
                                  "name": {
                                    "description": "The name of the repository.",
                                    "type": "string",
                                    "examples": [
                                      "Team Environment"
                                    ]
                                  },
                                  "full_name": {
                                    "type": "string",
                                    "examples": [
                                      "octocat/Hello-World"
                                    ]
                                  },
                                  "license": {
                                    "anyOf": [
                                      {
                                        "type": "null"
                                      },
                                      {
                                        "title": "License Simple",
                                        "description": "License Simple",
                                        "type": "object",
                                        "properties": {
                                          "key": {
                                            "type": "string",
                                            "examples": [
                                              "mit"
                                            ]
                                          },
                                          "name": {
                                            "type": "string",
                                            "examples": [
                                              "MIT License"
                                            ]
                                          },
                                          "url": {
                                            "type": [
                                              "string",
                                              "null"
                                            ],
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/licenses/mit"
                                            ]
                                          },
                                          "spdx_id": {
                                            "type": [
                                              "string",
                                              "null"
                                            ],
                                            "examples": [
                                              "MIT"
                                            ]
                                          },
                                          "node_id": {
                                            "type": "string",
                                            "examples": [
                                              "MDc6TGljZW5zZW1pdA=="
                                            ]
                                          },
                                          "html_url": {
                                            "type": "string",
                                            "format": "uri"
                                          }
                                        },
                                        "required": [
                                          "key",
                                          "name",
                                          "url",
                                          "spdx_id",
                                          "node_id"
                                        ]
                                      }
                                    ]
                                  },
                                  "organization": {
                                    "anyOf": [
                                      {
                                        "type": "null"
                                      },
                                      {
                                        "title": "Simple User",
                                        "description": "Simple User",
                                        "type": "object",
                                        "properties": {
                                          "name": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          },
                                          "email": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          },
                                          "login": {
                                            "type": "string",
                                            "examples": [
                                              "octocat"
                                            ]
                                          },
                                          "id": {
                                            "type": "integer",
                                            "examples": [
                                              1
                                            ]
                                          },
                                          "node_id": {
                                            "type": "string",
                                            "examples": [
                                              "MDQ6VXNlcjE="
                                            ]
                                          },
                                          "avatar_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://github.com/images/error/octocat_happy.gif"
                                            ]
                                          },
                                          "gravatar_id": {
                                            "type": [
                                              "string",
                                              "null"
                                            ],
                                            "examples": [
                                              "41d064eb2195891e12d0413f63227ea7"
                                            ]
                                          },
                                          "url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/users/octocat"
                                            ]
                                          },
                                          "html_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://github.com/octocat"
                                            ]
                                          },
                                          "followers_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/users/octocat/followers"
                                            ]
                                          },
                                          "following_url": {
                                            "type": "string",
                                            "examples": [
                                              "https://api.github.com/users/octocat/following{/other_user}"
                                            ]
                                          },
                                          "gists_url": {
                                            "type": "string",
                                            "examples": [
                                              "https://api.github.com/users/octocat/gists{/gist_id}"
                                            ]
                                          },
                                          "starred_url": {
                                            "type": "string",
                                            "examples": [
                                              "https://api.github.com/users/octocat/starred{/owner}{/repo}"
                                            ]
                                          },
                                          "subscriptions_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/users/octocat/subscriptions"
                                            ]
                                          },
                                          "organizations_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/users/octocat/orgs"
                                            ]
                                          },
                                          "repos_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/users/octocat/repos"
                                            ]
                                          },
                                          "events_url": {
                                            "type": "string",
                                            "examples": [
                                              "https://api.github.com/users/octocat/events{/privacy}"
                                            ]
                                          },
                                          "received_events_url": {
                                            "type": "string",
                                            "format": "uri",
                                            "examples": [
                                              "https://api.github.com/users/octocat/received_events"
                                            ]
                                          },
                                          "type": {
                                            "type": "string",
                                            "examples": [
                                              "User"
                                            ]
                                          },
                                          "site_admin": {
                                            "type": "boolean"
                                          },
                                          "starred_at": {
                                            "type": "string",
                                            "examples": [
                                              "\"2020-07-09T00:17:55Z\""
                                            ]
                                          }
                                        },
                                        "required": [
                                          "avatar_url",
                                          "events_url",
                                          "followers_url",
                                          "following_url",
                                          "gists_url",
                                          "gravatar_id",
                                          "html_url",
                                          "id",
                                          "node_id",
                                          "login",
                                          "organizations_url",
                                          "received_events_url",
                                          "repos_url",
                                          "site_admin",
                                          "starred_url",
                                          "subscriptions_url",
                                          "type",
                                          "url"
                                        ]
                                      }
                                    ]
                                  },
                                  "forks": {
                                    "type": "integer"
                                  },
                                  "permissions": {
                                    "type": "object",
                                    "properties": {
                                      "admin": {
                                        "type": "boolean"
                                      },
                                      "pull": {
                                        "type": "boolean"
                                      },
                                      "triage": {
                                        "type": "boolean"
                                      },
                                      "push": {
                                        "type": "boolean"
                                      },
                                      "maintain": {
                                        "type": "boolean"
                                      }
                                    },
                                    "required": [
                                      "admin",
                                      "pull",
                                      "push"
                                    ]
                                  },
                                  "owner": {
                                    "title": "Simple User",
                                    "description": "Simple User",
                                    "type": "object",
                                    "properties": {
                                      "name": {
                                        "type": [
                                          "string",
                                          "null"
                                        ]
                                      },
                                      "email": {
                                        "type": [
                                          "string",
                                          "null"
                                        ]
                                      },
                                      "login": {
                                        "type": "string",
                                        "examples": [
                                          "octocat"
                                        ]
                                      },
                                      "id": {
                                        "type": "integer",
                                        "examples": [
                                          1
                                        ]
                                      },
                                      "node_id": {
                                        "type": "string",
                                        "examples": [
                                          "MDQ6VXNlcjE="
                                        ]
                                      },
                                      "avatar_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://github.com/images/error/octocat_happy.gif"
                                        ]
                                      },
                                      "gravatar_id": {
                                        "type": [
                                          "string",
                                          "null"
                                        ],
                                        "examples": [
                                          "41d064eb2195891e12d0413f63227ea7"
                                        ]
                                      },
                                      "url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://api.github.com/users/octocat"
                                        ]
                                      },
                                      "html_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://github.com/octocat"
                                        ]
                                      },
                                      "followers_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://api.github.com/users/octocat/followers"
                                        ]
                                      },
                                      "following_url": {
                                        "type": "string",
                                        "examples": [
                                          "https://api.github.com/users/octocat/following{/other_user}"
                                        ]
                                      },
                                      "gists_url": {
                                        "type": "string",
                                        "examples": [
                                          "https://api.github.com/users/octocat/gists{/gist_id}"
                                        ]
                                      },
                                      "starred_url": {
                                        "type": "string",
                                        "examples": [
                                          "https://api.github.com/users/octocat/starred{/owner}{/repo}"
                                        ]
                                      },
                                      "subscriptions_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://api.github.com/users/octocat/subscriptions"
                                        ]
                                      },
                                      "organizations_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://api.github.com/users/octocat/orgs"
                                        ]
                                      },
                                      "repos_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://api.github.com/users/octocat/repos"
                                        ]
                                      },
                                      "events_url": {
                                        "type": "string",
                                        "examples": [
                                          "https://api.github.com/users/octocat/events{/privacy}"
                                        ]
                                      },
                                      "received_events_url": {
                                        "type": "string",
                                        "format": "uri",
                                        "examples": [
                                          "https://api.github.com/users/octocat/received_events"
                                        ]
                                      },
                                      "type": {
                                        "type": "string",
                                        "examples": [
                                          "User"
                                        ]
                                      },
                                      "site_admin": {
                                        "type": "boolean"
                                      },
                                      "starred_at": {
                                        "type": "string",
                                        "examples": [
                                          "\"2020-07-09T00:17:55Z\""
                                        ]
                                      }
                                    },
                                    "required": [
                                      "avatar_url",
                                      "events_url",
                                      "followers_url",
                                      "following_url",
                                      "gists_url",
                                      "gravatar_id",
                                      "html_url",
                                      "id",
                                      "node_id",
                                      "login",
                                      "organizations_url",
                                      "received_events_url",
                                      "repos_url",
                                      "site_admin",
                                      "starred_url",
                                      "subscriptions_url",
                                      "type",
                                      "url"
                                    ]
                                  },
                                  "private": {
                                    "description": "Whether the repository is private or public.",
                                    "default": False,
                                    "type": "boolean"
                                  },
                                  "html_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "https://github.com/octocat/Hello-World"
                                    ]
                                  },
                                  "description": {
                                    "type": [
                                      "string",
                                      "null"
                                    ],
                                    "examples": [
                                      "This your first repo!"
                                    ]
                                  },
                                  "fork": {
                                    "type": "boolean"
                                  },
                                  "url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "https://api.github.com/repos/octocat/Hello-World"
                                    ]
                                  },
                                  "archive_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}"
                                    ]
                                  },
                                  "assignees_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/assignees{/user}"
                                    ]
                                  },
                                  "blobs_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}"
                                    ]
                                  },
                                  "branches_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/branches{/branch}"
                                    ]
                                  },
                                  "collaborators_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}"
                                    ]
                                  },
                                  "comments_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/comments{/number}"
                                    ]
                                  },
                                  "commits_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/commits{/sha}"
                                    ]
                                  },
                                  "compare_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}"
                                    ]
                                  },
                                  "contents_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/contents/{+path}"
                                    ]
                                  },
                                  "contributors_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/contributors"
                                    ]
                                  },
                                  "deployments_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/deployments"
                                    ]
                                  },
                                  "downloads_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/downloads"
                                    ]
                                  },
                                  "events_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/events"
                                    ]
                                  },
                                  "forks_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/forks"
                                    ]
                                  },
                                  "git_commits_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}"
                                    ]
                                  },
                                  "git_refs_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}"
                                    ]
                                  },
                                  "git_tags_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}"
                                    ]
                                  },
                                  "git_url": {
                                    "type": "string",
                                    "examples": [
                                      "git:github.com/octocat/Hello-World.git"
                                    ]
                                  },
                                  "issue_comment_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}"
                                    ]
                                  },
                                  "issue_events_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}"
                                    ]
                                  },
                                  "issues_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/issues{/number}"
                                    ]
                                  },
                                  "keys_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}"
                                    ]
                                  },
                                  "labels_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/labels{/name}"
                                    ]
                                  },
                                  "languages_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/languages"
                                    ]
                                  },
                                  "merges_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/merges"
                                    ]
                                  },
                                  "milestones_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/milestones{/number}"
                                    ]
                                  },
                                  "notifications_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}"
                                    ]
                                  },
                                  "pulls_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/pulls{/number}"
                                    ]
                                  },
                                  "releases_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/releases{/id}"
                                    ]
                                  },
                                  "ssh_url": {
                                    "type": "string",
                                    "examples": [
                                      "git@github.com:octocat/Hello-World.git"
                                    ]
                                  },
                                  "stargazers_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/stargazers"
                                    ]
                                  },
                                  "statuses_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}"
                                    ]
                                  },
                                  "subscribers_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/subscribers"
                                    ]
                                  },
                                  "subscription_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/subscription"
                                    ]
                                  },
                                  "tags_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/tags"
                                    ]
                                  },
                                  "teams_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/teams"
                                    ]
                                  },
                                  "trees_url": {
                                    "type": "string",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}"
                                    ]
                                  },
                                  "clone_url": {
                                    "type": "string",
                                    "examples": [
                                      "https://github.com/octocat/Hello-World.git"
                                    ]
                                  },
                                  "mirror_url": {
                                    "type": [
                                      "string",
                                      "null"
                                    ],
                                    "format": "uri",
                                    "examples": [
                                      "git:git.example.com/octocat/Hello-World"
                                    ]
                                  },
                                  "hooks_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "http://api.github.com/repos/octocat/Hello-World/hooks"
                                    ]
                                  },
                                  "svn_url": {
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                      "https://svn.github.com/octocat/Hello-World"
                                    ]
                                  },
                                  "homepage": {
                                    "type": [
                                      "string",
                                      "null"
                                    ],
                                    "format": "uri",
                                    "examples": [
                                      "https://github.com"
                                    ]
                                  },
                                  "language": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  "forks_count": {
                                    "type": "integer",
                                    "examples": [
                                      9
                                    ]
                                  },
                                  "stargazers_count": {
                                    "type": "integer",
                                    "examples": [
                                      80
                                    ]
                                  },
                                  "watchers_count": {
                                    "type": "integer",
                                    "examples": [
                                      80
                                    ]
                                  },
                                  "size": {
                                    "type": "integer",
                                    "examples": [
                                      108
                                    ]
                                  },
                                  "default_branch": {
                                    "description": "The default branch of the repository.",
                                    "type": "string",
                                    "examples": [
                                      "master"
                                    ]
                                  },
                                  "open_issues_count": {
                                    "type": "integer",
                                    "examples": [
                                      0
                                    ]
                                  },
                                  "is_template": {
                                    "description": "Whether this repository acts as a template that can be used to generate new repositories.",
                                    "default": False,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "topics": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  },
                                  "has_issues": {
                                    "description": "Whether issues are enabled.",
                                    "default": True,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "has_projects": {
                                    "description": "Whether projects are enabled.",
                                    "default": True,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "has_wiki": {
                                    "description": "Whether the wiki is enabled.",
                                    "default": True,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "has_pages": {
                                    "type": "boolean"
                                  },
                                  "has_downloads": {
                                    "description": "Whether downloads are enabled.",
                                    "default": True,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "archived": {
                                    "description": "Whether the repository is archived.",
                                    "default": False,
                                    "type": "boolean"
                                  },
                                  "disabled": {
                                    "type": "boolean",
                                    "description": "Returns whether or not this repository disabled."
                                  },
                                  "visibility": {
                                    "description": "The repository visibility: public, private, or internal.",
                                    "default": "public",
                                    "type": "string"
                                  },
                                  "pushed_at": {
                                    "type": [
                                      "string",
                                      "null"
                                    ],
                                    "format": "date-time",
                                    "examples": [
                                      "2011-01-26T19:06:43Z"
                                    ]
                                  },
                                  "created_at": {
                                    "type": [
                                      "string",
                                      "null"
                                    ],
                                    "format": "date-time",
                                    "examples": [
                                      "2011-01-26T19:01:12Z"
                                    ]
                                  },
                                  "updated_at": {
                                    "type": [
                                      "string",
                                      "null"
                                    ],
                                    "format": "date-time",
                                    "examples": [
                                      "2011-01-26T19:14:43Z"
                                    ]
                                  },
                                  "allow_rebase_merge": {
                                    "description": "Whether to allow rebase merges for pull requests.",
                                    "default": True
                                      ,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "template_repository": {
                                    "type": [
                                      "object",
                                      "null"
                                    ],
                                    "properties": {
                                      "id": {
                                        "type": "integer"
                                      },
                                      "node_id": {
                                        "type": "string"
                                      },
                                      "name": {
                                        "type": "string"
                                      },
                                      "full_name": {
                                        "type": "string"
                                      },
                                      "owner": {
                                        "type": "object",
                                        "properties": {
                                          "login": {
                                            "type": "string"
                                          },
                                          "id": {
                                            "type": "integer"
                                          },
                                          "node_id": {
                                            "type": "string"
                                          },
                                          "avatar_url": {
                                            "type": "string"
                                          },
                                          "gravatar_id": {
                                            "type": "string"
                                          },
                                          "url": {
                                            "type": "string"
                                          },
                                          "html_url": {
                                            "type": "string"
                                          },
                                          "followers_url": {
                                            "type": "string"
                                          },
                                          "following_url": {
                                            "type": "string"
                                          },
                                          "gists_url": {
                                            "type": "string"
                                          },
                                          "starred_url": {
                                            "type": "string"
                                          },
                                          "subscriptions_url": {
                                            "type": "string"
                                          },
                                          "organizations_url": {
                                            "type": "string"
                                          },
                                          "repos_url": {
                                            "type": "string"
                                          },
                                          "events_url": {
                                            "type": "string"
                                          },
                                          "received_events_url": {
                                            "type": "string"
                                          },
                                          "type": {
                                            "type": "string"
                                          },
                                          "site_admin": {
                                            "type": "boolean"
                                          }
                                        }
                                      },
                                      "private": {
                                        "type": "boolean"
                                      },
                                      "html_url": {
                                        "type": "string"
                                      },
                                      "description": {
                                        "type": "string"
                                      },
                                      "fork": {
                                        "type": "boolean"
                                      },
                                      "url": {
                                        "type": "string"
                                      },
                                      "archive_url": {
                                        "type": "string"
                                      },
                                      "assignees_url": {
                                        "type": "string"
                                      },
                                      "blobs_url": {
                                        "type": "string"
                                      },
                                      "branches_url": {
                                        "type": "string"
                                      },
                                      "collaborators_url": {
                                        "type": "string"
                                      },
                                      "comments_url": {
                                        "type": "string"
                                      },
                                      "commits_url": {
                                        "type": "string"
                                      },
                                      "compare_url": {
                                        "type": "string"
                                      },
                                      "contents_url": {
                                        "type": "string"
                                      },
                                      "contributors_url": {
                                        "type": "string"
                                      },
                                      "deployments_url": {
                                        "type": "string"
                                      },
                                      "downloads_url": {
                                        "type": "string"
                                      },
                                      "events_url": {
                                        "type": "string"
                                      },
                                      "forks_url": {
                                        "type": "string"
                                      },
                                      "git_commits_url": {
                                        "type": "string"
                                      },
                                      "git_refs_url": {
                                        "type": "string"
                                      },
                                      "git_tags_url": {
                                        "type": "string"
                                      },
                                      "git_url": {
                                        "type": "string"
                                      },
                                      "issue_comment_url": {
                                        "type": "string"
                                      },
                                      "issue_events_url": {
                                        "type": "string"
                                      },
                                      "issues_url": {
                                        "type": "string"
                                      },
                                      "keys_url": {
                                        "type": "string"
                                      },
                                      "labels_url": {
                                        "type": "string"
                                      },
                                      "languages_url": {
                                        "type": "string"
                                      },
                                      "merges_url": {
                                        "type": "string"
                                      },
                                      "milestones_url": {
                                        "type": "string"
                                      },
                                      "notifications_url": {
                                        "type": "string"
                                      },
                                      "pulls_url": {
                                        "type": "string"
                                      },
                                      "releases_url": {
                                        "type": "string"
                                      },
                                      "ssh_url": {
                                        "type": "string"
                                      },
                                      "stargazers_url": {
                                        "type": "string"
                                      },
                                      "statuses_url": {
                                        "type": "string"
                                      },
                                      "subscribers_url": {
                                        "type": "string"
                                      },
                                      "subscription_url": {
                                        "type": "string"
                                      },
                                      "tags_url": {
                                        "type": "string"
                                      },
                                      "teams_url": {
                                        "type": "string"
                                      },
                                      "trees_url": {
                                        "type": "string"
                                      },
                                      "clone_url": {
                                        "type": "string"
                                      },
                                      "mirror_url": {
                                        "type": "string"
                                      },
                                      "hooks_url": {
                                        "type": "string"
                                      },
                                      "svn_url": {
                                        "type": "string"
                                      },
                                      "homepage": {
                                        "type": "string"
                                      },
                                      "language": {
                                        "type": "string"
                                      },
                                      "forks_count": {
                                        "type": "integer"
                                      },
                                      "stargazers_count": {
                                        "type": "integer"
                                      },
                                      "watchers_count": {
                                        "type": "integer"
                                      },
                                      "size": {
                                        "type": "integer"
                                      },
                                      "default_branch": {
                                        "type": "string"
                                      },
                                      "open_issues_count": {
                                        "type": "integer"
                                      },
                                      "is_template": {
                                        "type": "boolean"
                                      },
                                      "topics": {
                                        "type": "array",
                                        "items": {
                                          "type": "string"
                                        }
                                      },
                                      "has_issues": {
                                        "type": "boolean"
                                      },
                                      "has_projects": {
                                        "type": "boolean"
                                      },
                                      "has_wiki": {
                                        "type": "boolean"
                                      },
                                      "has_pages": {
                                        "type": "boolean"
                                      },
                                      "has_downloads": {
                                        "type": "boolean"
                                      },
                                      "archived": {
                                        "type": "boolean"
                                      },
                                      "disabled": {
                                        "type": "boolean"
                                      },
                                      "visibility": {
                                        "type": "string"
                                      },
                                      "pushed_at": {
                                        "type": "string"
                                      },
                                      "created_at": {
                                        "type": "string"
                                      },
                                      "updated_at": {
                                        "type": "string"
                                      },
                                      "permissions": {
                                        "type": "object",
                                        "properties": {
                                          "admin": {
                                            "type": "boolean"
                                          },
                                          "maintain": {
                                            "type": "boolean"
                                          },
                                          "push": {
                                            "type": "boolean"
                                          },
                                          "triage": {
                                            "type": "boolean"
                                          },
                                          "pull": {
                                            "type": "boolean"
                                          }
                                        }
                                      },
                                      "allow_rebase_merge": {
                                        "type": "boolean"
                                      },
                                      "temp_clone_token": {
                                        "type": "string"
                                      },
                                      "allow_squash_merge": {
                                        "type": "boolean"
                                      },
                                      "allow_auto_merge": {
                                        "type": "boolean"
                                      },
                                      "delete_branch_on_merge": {
                                        "type": "boolean"
                                      },
                                      "allow_update_branch": {
                                        "type": "boolean"
                                      },
                                      "allow_merge_commit": {
                                        "type": "boolean"
                                      },
                                      "subscribers_count": {
                                        "type": "integer"
                                      },
                                      "network_count": {
                                        "type": "integer"
                                      }
                                    }
                                  },
                                  "temp_clone_token": {
                                    "type": "string"
                                  },
                                  "allow_squash_merge": {
                                    "description": "Whether to allow squash merges for pull requests.",
                                    "default": True,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "allow_auto_merge": {
                                    "description": "Whether to allow Auto-merge to be used on pull requests.",
                                    "default": False,
                                    "type": "boolean",
                                    "examples": [
                                      False
                                    ]
                                  },
                                  "delete_branch_on_merge": {
                                    "description": "Whether to delete head branches when pull requests are merged",
                                    "default": False,
                                    "type": "boolean",
                                    "examples": [
                                      False
                                    ]
                                  },
                                  "allow_merge_commit": {
                                    "description": "Whether to allow merge commits for pull requests.",
                                    "default": True,
                                    "type": "boolean",
                                    "examples": [
                                      True
                                    ]
                                  },
                                  "allow_forking": {
                                    "description": "Whether to allow forking this repo",
                                    "type": "boolean"
                                  },
                                  "subscribers_count": {
                                    "type": "integer"
                                  },
                                  "network_count": {
                                    "type": "integer"
                                  },
                                  "open_issues": {
                                    "type": "integer"
                                  },
                                  "watchers": {
                                    "type": "integer"
                                  },
                                  "master_branch": {
                                    "type": "string"
                                  },
                                  "starred_at": {
                                    "type": "string",
                                    "examples": [
                                      "\"2020-07-09T00:17:42Z\""
                                    ]
                                  }
                                },
                                "required": [
                                  "archive_url",
                                  "assignees_url",
                                  "blobs_url",
                                  "branches_url",
                                  "collaborators_url",
                                  "comments_url",
                                  "commits_url",
                                  "compare_url",
                                  "contents_url",
                                  "contributors_url",
                                  "deployments_url",
                                  "description",
                                  "downloads_url",
                                  "events_url",
                                  "fork",
                                  "forks_url",
                                  "full_name",
                                  "git_commits_url",
                                  "git_refs_url",
                                  "git_tags_url",
                                  "hooks_url",
                                  "html_url",
                                  "id",
                                  "node_id",
                                  "issue_comment_url",
                                  "issue_events_url",
                                  "issues_url",
                                  "keys_url",
                                  "labels_url",
                                  "languages_url",
                                  "merges_url",
                                  "milestones_url",
                                  "name",
                                  "notifications_url",
                                  "owner",
                                  "private",
                                  "pulls_url",
                                  "releases_url",
                                  "stargazers_url",
                                  "statuses_url",
                                  "subscribers_url",
                                  "subscription_url",
                                  "tags_url",
                                  "teams_url",
                                  "trees_url",
                                  "url",
                                  "clone_url",
                                  "default_branch",
                                  "forks",
                                  "forks_count",
                                  "git_url",
                                  "has_downloads",
                                  "has_issues",
                                  "has_projects",
                                  "has_wiki",
                                  "has_pages",
                                  "homepage",
                                  "language",
                                  "archived",
                                  "disabled",
                                  "mirror_url",
                                  "open_issues",
                                  "open_issues_count",
                                  "license",
                                  "pushed_at",
                                  "size",
                                  "ssh_url",
                                  "stargazers_count",
                                  "svn_url",
                                  "watchers",
                                  "watchers_count",
                                  "created_at",
                                  "updated_at"
                                ]
                              }
                            ]
                          },
                          "temp_clone_token": {
                            "type": "string"
                          },
                          "delete_branch_on_merge": {
                            "type": "boolean"
                          },
                          "subscribers_count": {
                            "type": "integer"
                          },
                          "network_count": {
                            "type": "integer"
                          },
                          "code_of_conduct": {
                            "title": "Code Of Conduct",
                            "description": "Code Of Conduct",
                            "type": "object",
                            "properties": {
                              "key": {
                                "type": "string",
                                "examples": [
                                  "contributor_covenant"
                                ]
                              },
                              "name": {
                                "type": "string",
                                "examples": [
                                  "Contributor Covenant"
                                ]
                              },
                              "url": {
                                "type": "string",
                                "format": "uri",
                                "examples": [
                                  "https://api.github.com/codes_of_conduct/contributor_covenant"
                                ]
                              },
                              "body": {
                                "type": "string",
                                "examples": [
                                  "# Contributor Covenant Code of Conduct\n\n## Our Pledge\n\nIn the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.\n\n## Our Standards\n\nExamples of behavior that contributes to creating a positive environment include:\n\n* Using welcoming and inclusive language\n* Being respectful of differing viewpoints and experiences\n* Gracefully accepting constructive criticism\n* Focusing on what is best for the community\n* Showing empathy towards other community members\n\nExamples of unacceptable behavior by participants include:\n\n* The use of sexualized language or imagery and unwelcome sexual attention or advances\n* Trolling, insulting/derogatory comments, and personal or political attacks\n* Public or private harassment\n* Publishing others' private information, such as a physical or electronic address, without explicit permission\n* Other conduct which could reasonably be considered inappropriate in a professional setting\n\n## Our Responsibilities\n\nProject maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response\n                  to any instances of unacceptable behavior.\n\nProject maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.\n\n## Scope\n\nThis Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address,\n                  posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.\n\n## Enforcement\n\nInstances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [EMAIL]. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.\n\nProject maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.\n\n## Attribution\n\nThis Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]\n\n[homepage]: http://contributor-covenant.org\n[version]: http://contributor-covenant.org/version/1/4/\n"
                                ]
                              },
                              "html_url": {
                                "type": [
                                  "string",
                                  "null"
                                ],
                                "format": "uri"
                              }
                            },
                            "required": [
                              "url",
                              "html_url",
                              "key",
                              "name"
                            ]
                          },
                          "license": {
                            "type": [
                              "object",
                              "null"
                            ],
                            "properties": {
                              "key": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "spdx_id": {
                                "type": "string"
                              },
                              "url": {
                                "type": "string"
                              },
                              "node_id": {
                                "type": "string"
                              }
                            }
                          },
                          "forks": {
                            "type": "integer",
                            "examples": [
                              0
                            ]
                          },
                          "open_issues": {
                            "type": "integer",
                            "examples": [
                              0
                            ]
                          },
                          "watchers": {
                            "type": "integer",
                            "examples": [
                              0
                            ]
                          },
                          "allow_forking": {
                            "type": "boolean"
                          }
                        },
                        "required": [
                          "archive_url",
                          "assignees_url",
                          "blobs_url",
                          "branches_url",
                          "collaborators_url",
                          "comments_url",
                          "commits_url",
                          "compare_url",
                          "contents_url",
                          "contributors_url",
                          "deployments_url",
                          "description",
                          "downloads_url",
                          "events_url",
                          "fork",
                          "forks_url",
                          "full_name",
                          "git_commits_url",
                          "git_refs_url",
                          "git_tags_url",
                          "hooks_url",
                          "html_url",
                          "id",
                          "node_id",
                          "issue_comment_url",
                          "issue_events_url",
                          "issues_url",
                          "keys_url",
                          "labels_url",
                          "languages_url",
                          "merges_url",
                          "milestones_url",
                          "name",
                          "notifications_url",
                          "owner",
                          "private",
                          "pulls_url",
                          "releases_url",
                          "stargazers_url",
                          "statuses_url",
                          "subscribers_url",
                          "subscription_url",
                          "tags_url",
                          "teams_url",
                          "trees_url",
                          "url"
                        ]
                      }
                    }
