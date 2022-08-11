"""empty message

Revision ID: fac199d8e12a
Revises: 968f6bc006c2
Create Date: 2022-08-11 06:44:25.080535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fac199d8e12a'
down_revision = '968f6bc006c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_urls_shorten_url_created_by', table_name='urls')
    op.create_unique_constraint(None, 'urls', ['shorten_url_created_by'])
    # ### end Alembic commands ###
    pass

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'urls', type_='unique')
    op.create_index('ix_urls_shorten_url_created_by', 'urls', ['shorten_url_created_by'], unique=False)
    ### end Alembic commands ###
    pass
