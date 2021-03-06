"""Changing column names

Revision ID: ffdd0cf544c4
Revises: 5bfb2527602d
Create Date: 2017-11-14 03:10:47.037106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffdd0cf544c4'
down_revision = '5bfb2527602d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AnotherTestTable', sa.Column('Letters', sa.String(), nullable=True))
    op.add_column('AnotherTestTable', sa.Column('Numbers', sa.Float(), nullable=True))
    op.drop_column('AnotherTestTable', 'Words')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AnotherTestTable', sa.Column('Words', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('AnotherTestTable', 'Numbers')
    op.drop_column('AnotherTestTable', 'Letters')
    # ### end Alembic commands ###
