"""empty message

Revision ID: 4b9c935caff6
Revises: 3f2584e6033b
Create Date: 2023-11-15 12:02:50.228304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b9c935caff6'
down_revision: Union[str, None] = '3f2584e6033b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    # ### end Alembic commands ###
