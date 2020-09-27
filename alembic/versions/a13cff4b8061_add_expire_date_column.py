"""Add expire date column

Revision ID: a13cff4b8061
Revises: 39f877d94c71
Create Date: 2020-09-27 19:39:34.465502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a13cff4b8061'
down_revision = '39f877d94c71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('expire', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'expire')
    # ### end Alembic commands ###
