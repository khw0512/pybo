"""empty message

Revision ID: 5521c5f0ec61
Revises: 5143ed1b36df
Create Date: 2022-03-29 23:39:55.458763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5521c5f0ec61'
down_revision = '5143ed1b36df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
