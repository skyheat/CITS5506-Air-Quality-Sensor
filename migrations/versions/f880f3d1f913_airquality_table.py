"""airquality table

Revision ID: f880f3d1f913
Revises: 
Create Date: 2022-09-21 13:12:57.969732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f880f3d1f913'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('air_quality',
    sa.Column('timestamp', sa.String(length=64), nullable=False),
    sa.Column('temp', sa.Integer(), nullable=True),
    sa.Column('humidity', sa.Integer(), nullable=True),
    sa.Column('particles', sa.Integer(), nullable=True),
    sa.Column('eco2', sa.Integer(), nullable=True),
    sa.Column('tvoc', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('timestamp')
    )
    op.create_index(op.f('ix_air_quality_timestamp'), 'air_quality', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_air_quality_timestamp'), table_name='air_quality')
    op.drop_table('air_quality')
    # ### end Alembic commands ###

def upgrade_settings():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature_lower_bound', sa.Integer(), nullable=False),
    sa.Column('temperature_upper_bound', sa.Integer(), nullable=False),
    sa.Column('humidity_lower_bound', sa.Integer(), nullable=False),
    sa.Column('humidity_upper_bound', sa.Integer(), nullable=False),
    sa.Column('particles_lower_bound', sa.Integer(), nullable=False),
    sa.Column('particles_upper_bound', sa.Integer(), nullable=False),
    sa.Column('co2_lower_bound', sa.Integer(), nullable=False),
    sa.Column('co2_upper_bound', sa.Integer(), nullable=False),
    sa.Column('tvoc_lower_bound', sa.Integer(), nullable=False),
    sa.Column('tvoc_upper_bound', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_settings_id'), 'settings', ['id'], unique=True)
    # ### end Alembic commands ###
 
