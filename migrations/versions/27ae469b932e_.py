"""empty message

Revision ID: 27ae469b932e
Revises: 7fab239ad6bb
Create Date: 2023-05-05 11:23:49.478762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27ae469b932e'
down_revision = '7fab239ad6bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###