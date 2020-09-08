#    Copyright 2020 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""sctp support

Revision ID: 8b47b2546312
Revises: e6ee84f0abf3
Create Date: 2020-06-26 09:26:45.397873

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '8b47b2546312'
down_revision = 'e6ee84f0abf3'


def upgrade():
    for table in ['protocol', 'health_monitor_type']:
        insert_table = sql.table(
            table,
            sql.column(u'name', sa.String),
            sql.column(u'description', sa.String)
        )

        op.bulk_insert(
            insert_table,
            [
                {'name': 'SCTP'}
            ]
        )
