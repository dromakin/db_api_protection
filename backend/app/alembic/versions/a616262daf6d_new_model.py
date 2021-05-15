"""New model

Revision ID: a616262daf6d
Revises: d4867f3a4c0a
Create Date: 2021-05-13 17:58:07.071826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a616262daf6d'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statistic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('target', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('tid', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('cookie', sa.String(), nullable=True),
    sa.Column('hashid', sa.String(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('webGL', sa.String(), nullable=True),
    sa.Column('canvas', sa.String(), nullable=True),
    sa.Column('deviceId', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_statistic_cookie'), 'statistic', ['cookie'], unique=False)
    op.create_index(op.f('ix_statistic_id'), 'statistic', ['id'], unique=False)
    op.create_index(op.f('ix_statistic_ip'), 'statistic', ['ip'], unique=False)
    op.create_index(op.f('ix_statistic_target'), 'statistic', ['target'], unique=False)
    op.create_index(op.f('ix_statistic_tid'), 'statistic', ['tid'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_statistic_tid'), table_name='statistic')
    op.drop_index(op.f('ix_statistic_target'), table_name='statistic')
    op.drop_index(op.f('ix_statistic_ip'), table_name='statistic')
    op.drop_index(op.f('ix_statistic_id'), table_name='statistic')
    op.drop_index(op.f('ix_statistic_cookie'), table_name='statistic')
    op.drop_table('statistic')
    # ### end Alembic commands ###
