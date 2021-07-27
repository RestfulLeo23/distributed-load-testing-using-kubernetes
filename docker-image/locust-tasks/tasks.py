#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from locust_plugins.users import HttpUserWithResources
from locust import HttpUser , TaskSet, task


class MetricsTaskSet(HttpUserWithResources):
    # these values can be overridden
    # bundle_resource_stats=False
    # default_resource_filter=".*[^(js)]$"
    @task
    def include_resources_default(self):
        self.client.get("/")

class MetricsLocust(HttpUser):
    task_set = MetricsTaskSet

