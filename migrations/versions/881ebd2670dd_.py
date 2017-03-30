"""empty message

Revision ID: 881ebd2670dd
Revises: 5b0c653a64b3
Create Date: 2017-03-30 13:07:46.478628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '881ebd2670dd'
down_revision = '5b0c653a64b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brewery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('style', sa.String(length=255), nullable=True),
    sa.Column('abv', sa.Float(), nullable=True),
    sa.Column('colour', sa.String(length=255), nullable=True),
    sa.Column('brewery_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brewery_id'], ['brewery.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'tap', sa.Column('beer_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_tap_beer', 'tap', 'beer', ['beer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_tap_beer', 'tap', type_='foreignkey')
    op.drop_column(u'tap', 'beer_id')
    op.drop_table('beer')
    op.drop_table('brewery')
    # ### end Alembic commands ###
