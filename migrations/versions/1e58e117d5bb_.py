"""empty message

Revision ID: 1e58e117d5bb
Revises: 
Create Date: 2023-05-12 12:22:41.982711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e58e117d5bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('aphp_num', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('aphp_num'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('status'),
    sa.UniqueConstraint('username')
    )
    op.create_table('grant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('project_title', sa.String(length=120), nullable=True),
    sa.Column('application', sa.String(length=20), nullable=True),
    sa.Column('organism', sa.String(length=20), nullable=True),
    sa.Column('principal_investigator', sa.String(length=20), nullable=True),
    sa.Column('promotor', sa.String(length=20), nullable=True),
    sa.Column('funding_type', sa.String(length=20), nullable=True),
    sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('urgency_of_request', sa.String(length=20), nullable=True),
    sa.Column('if_urgency', sa.Text(), nullable=True),
    sa.Column('project_context', sa.Text(), nullable=True),
    sa.Column('project_context_private', sa.Text(), nullable=True),
    sa.Column('project_summary', sa.Text(), nullable=True),
    sa.Column('bioF_needs', sa.Text(), nullable=True),
    sa.Column('data_available', sa.Boolean(), nullable=True),
    sa.Column('access_data', sa.String(length=120), nullable=True),
    sa.Column('data_owner', sa.String(length=20), nullable=True),
    sa.Column('regulatory_requirements', sa.Boolean(), nullable=True),
    sa.Column('if_regulatory_requirements', sa.String(length=20), nullable=True),
    sa.Column('data_type', sa.String(length=20), nullable=True),
    sa.Column('data_size', sa.Integer(), nullable=True),
    sa.Column('add_info', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_accepted', sa.Boolean(), nullable=True),
    sa.Column('project_token', sa.String(length=120), nullable=False),
    sa.Column('project_title', sa.String(length=120), nullable=True),
    sa.Column('application', sa.String(length=20), nullable=True),
    sa.Column('organism', sa.String(length=20), nullable=True),
    sa.Column('principal_investigator', sa.String(length=20), nullable=True),
    sa.Column('promotor', sa.String(length=20), nullable=True),
    sa.Column('urgency_of_request', sa.String(length=20), nullable=True),
    sa.Column('if_urgency', sa.Text(), nullable=True),
    sa.Column('project_context', sa.Text(), nullable=True),
    sa.Column('project_context_private', sa.Text(), nullable=True),
    sa.Column('project_summary', sa.Text(), nullable=True),
    sa.Column('bioF_needs', sa.Text(), nullable=True),
    sa.Column('data_available', sa.Boolean(), nullable=True),
    sa.Column('access_data', sa.String(length=120), nullable=True),
    sa.Column('data_owner', sa.String(length=20), nullable=True),
    sa.Column('regulatory_requirements', sa.Boolean(), nullable=True),
    sa.Column('if_regulatory_requirements', sa.String(length=20), nullable=True),
    sa.Column('data_type', sa.String(length=20), nullable=True),
    sa.Column('data_size', sa.Integer(), nullable=True),
    sa.Column('add_info', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_token')
    )
    op.create_table('project_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.String(length=70), nullable=False),
    sa.Column('project_request', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('motif', sa.String(length=1000), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_request')
    op.drop_table('project')
    op.drop_table('post')
    op.drop_table('grant')
    op.drop_table('user')
    # ### end Alembic commands ###