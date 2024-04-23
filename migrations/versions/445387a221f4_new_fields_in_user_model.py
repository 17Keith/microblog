"""new fields in user model

Revision ID: 445387a221f4
Revises: 7c435efab259
Create Date: 2024-04-23 19:00:18.939660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '445387a221f4'
down_revision = '7c435efab259'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
