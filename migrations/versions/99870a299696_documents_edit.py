"""documents_edit

Revision ID: 99870a299696
Revises: d302bfcf4ebd
Create Date: 2021-12-23 11:55:23.381742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99870a299696'
down_revision = 'd302bfcf4ebd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('post', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('documents')
    # ### end Alembic commands ###