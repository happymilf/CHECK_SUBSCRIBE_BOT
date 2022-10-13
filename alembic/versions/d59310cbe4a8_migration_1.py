"""migration_1

Revision ID: d59310cbe4a8
Revises: 
Create Date: 2022-10-13 19:40:04.148598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd59310cbe4a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bottexts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('field_name', sa.String(length=60), nullable=True),
    sa.Column('field_text', sa.String(length=2000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('field_name')
    )
    op.create_index(op.f('ix_bottexts_id'), 'bottexts', ['id'], unique=False)
    op.create_table('promocodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=100), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('counter', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_index(op.f('ix_promocodes_id'), 'promocodes', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('promocode', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_promocodes_id'), table_name='promocodes')
    op.drop_table('promocodes')
    op.drop_index(op.f('ix_bottexts_id'), table_name='bottexts')
    op.drop_table('bottexts')
    # ### end Alembic commands ###
