# Copyright 2018 Google Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import datetime
# from googleapiclient import discovery
# from google.cloud import tasks_v2
# from google.protobuf import timestamp_pb2
# from oauth2client.client import GoogleCredentials


class TaskQueue(object):

  def add(self, task_name, params, delay):
    pass

  def delete(self, task_names):
    pass


# class CloudTasks(TaskQueue):
#
#   def __init__(self):
#     self.client = tasks_v2.CloudTasksClient()
#     project = 'crmint-johnstafford'
#     location = 'europe-west1'
#     queue = 'crmint-queue'
#     self.queue_path = self.client.queue_path(project, location, queue)
#
#   def add(self, name, params, delay):
#     schedule_datetime = datetime.datetime.utcnow() + datetime.timedelta(seconds=delay)
#     schedule_timestamp = timestamp_pb2.Timestamp()
#     schedule_timestamp.FromDateTime(schedule_datetime)
#
#     task = {
#       'name': name,
#       'schedule_time': schedule_timestamp,
#       'app_engine_http_request': {  # Specify the type of request.
#         'http_method': 'POST',
#         'relative_uri': '/task',
#         'body': params.encode()
#       }
#     }
#     response = self.client.create_task(self.queue_path, task)
#     return response
#
#   def delete(self, task_names):
#     credentials = GoogleCredentials.get_application_default()
#     service = discovery.build('cloudtasks', 'v2', credentials=credentials)
#     for task_name in task_names:
#       name = '{queue_path}/tasks/{task_name}'.format(
#         parent=self.queue_path, task_name=task_name)
#       request = service.projects().locations().queues().tasks().delete(name=name)
#       request.execute()



