# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.utils.translation import ugettext_lazy as _

from auth_backend.resources.base import Action
from auth_backend.backends.bkiam import BkIAMBackend
from auth_backend.resources.django import DjangoModelResource
from auth_backend.resources.inspect import FixedCreatorFieldInspect

from gcloud.commons.template.models import CommonTemplate

common_template_resource = DjangoModelResource(
    rtype='common-template',
    name=_(u"公共流程"),
    scope_type='system',
    scope_id='bk_sops',
    scope_name=_(u"标准运维"),
    actions=[
        Action(id='create', name=_(u"新建"), is_instance_related=False),
        Action(id='view', name=_(u"查看"), is_instance_related=True),
        Action(id='edit', name=_(u"编辑"), is_instance_related=True),
        Action(id='delete', name=_(u"删除"), is_instance_related=True),
        Action(id='create_task', name=_(u"新建任务"), is_instance_related=True)
    ],
    operations=[
        {
            'operate_id': 'create',
            'actions_id': ['create']
        },
        {
            'operate_id': 'view',
            'actions_id': ['view']
        },
        {
            'operate_id': 'edit',
            'actions_id': ['view', 'edit']
        },
        {
            'operate_id': 'delete',
            'actions_id': ['view', 'delete']
        },
        {
            'operate_id': 'create_task',
            'actions_id': ['view', 'create_task']
        }
    ],
    resource_cls=CommonTemplate,
    tomb_field='is_deleted',
    backend=BkIAMBackend(),
    inspect=FixedCreatorFieldInspect(creator_type='user',
                                     creator_id_f='creator_name',
                                     resource_id_f='id',
                                     resource_name_f='name',
                                     parent_f='project'))
