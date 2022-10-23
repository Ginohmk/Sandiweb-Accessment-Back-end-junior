"""Add Product Table

Revision ID: 690ed1dd46e8
Revises: 
Create Date: 2022-10-23 17:01:34.683288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690ed1dd46e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('price', sa.Integer(), nullable=False))
    op.add_column('product', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'product', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'category_id')
    op.drop_column('product', 'price')
    # ### end Alembic commands ###
