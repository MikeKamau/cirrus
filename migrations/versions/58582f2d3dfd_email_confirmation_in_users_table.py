"""Email confirmation in users table

Revision ID: 58582f2d3dfd
Revises: 1fcefbbe05b9
Create Date: 2021-09-16 12:42:42.274516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "58582f2d3dfd"
down_revision = "1fcefbbe05b9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("registered_on", sa.DateTime(), nullable=False))
    op.add_column("user", sa.Column("confirmed", sa.Boolean(), nullable=False))
    op.add_column("user", sa.Column("confirmed_on", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "confirmed_on")
    op.drop_column("user", "confirmed")
    op.drop_column("user", "registered_on")
    # ### end Alembic commands ###
