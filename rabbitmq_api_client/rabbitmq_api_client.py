#!/usr/bin/env python

import requests

class rabbit_conn:
    """"

    """
    def __init__(self, url, username, password):
        """

        Args:
            url:
            username: rabbitmq user
            password: password for accessing the rabbitmq
        """
        self.url=url
        self.user=username
        self.pwd= password

    def NewClient(self, path):
        """

        Args:
            path: http link

        Returns:

        """
        conn=requests.get(path, auth=(self.user, self.pwd))
        return conn

    def ListQueues(self):
        """

        Returns: list of queues declared on that rabbitmq

        """
        queues_list_url= self.url+ "/api/queues"
        res=self.NewClient(queues_list_url)
        queues=self.parse_queues(res.json(), 'name')
        return queues

    def ListQueuesIn(self, vhost):
        """

        Returns:

        """
        queues_list_url=self.url+"/api/queues/" + str(vhost)
        res=self.NewClient(queues_list_url)
        queues=self.parse_queues(res.json(), 'name')
        return queues

    def GetQueue(self,  qname, vhost='%2F'):
        """

        Args:
            qname:

        Returns:

        """
        queue_url=self.url + "/api/queues/" + str(vhost) + +"/" + qname
        res=self.NewClient(queue_url)
        return res.json()

    def parse_queues(self, res, key):
        """

        Args:
            res: response of the Http request
            key: dict value to be extracted

        Returns:

        """
        q_list=[]
        for q_name in res:
            q_list.append(q_name[key])
        return q_list






