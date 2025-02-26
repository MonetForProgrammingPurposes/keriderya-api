"""add menu table

Revision ID: ee6d6394730a
Revises: fe81a300b82f
Create Date: 2024-11-16 18:09:21.911393

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ee6d6394730a'
down_revision = 'fe81a300b82f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('menu_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('menu_uuid', mysql.CHAR(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['menu_category.menu_id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.restaurant_id'], ),
    sa.PrimaryKeyConstraint('menu_id'),
    sa.UniqueConstraint('menu_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu')
    # ### end Alembic commands ###
