"""empty message

Revision ID: 5143ed1b36df
Revises: 0d071218f2c0
Create Date: 2022-03-29 15:15:50.259454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5143ed1b36df'
down_revision = '0d071218f2c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
