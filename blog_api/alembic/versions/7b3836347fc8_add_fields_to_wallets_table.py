"""add fields to wallets table

Revision ID: 7b3836347fc8
Revises: 
Create Date: 2018-11-08 10:32:37.673314

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import IPAddressType

# revision identifiers, used by Alembic.
revision = '7b3836347fc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('wallets', sa.Column('label', sa.String))
  op.add_column('wallets', sa.Column('score', sa.Integer))
  op.add_column('wallets', sa.Column('last_balance', sa.Float))
  op.add_column('wallets', sa.Column('last_balance_update', sa.DateTime))
  op.add_column('wallets', sa.Column('last_ip_address', IPAddressType))
  op.add_column('wallets', sa.Column('active', sa.Boolean))
  op.add_column('wallets', sa.Column('portfolio_id', sa.Integer))
  op.create_unique_constraint('uq_hash', 'wallets', ['hash'])
  op.create_foreign_key(constraint_name="wallets_portfolio_fkey", source_table="wallets", referent_table="portfolios", local_cols=["portfolio_id"], remote_cols=["id"])


def downgrade():
  op.drop_column('wallets', 'label')
  op.drop_column('wallets', 'score')
  op.drop_column('wallets', 'last_balance')
  op.drop_column('wallets', 'last_balance_update')
  op.drop_column('wallets', 'last_ip_address')
  op.drop_column('wallets', 'active')
  op.drop_constraint('uq_hash', 'wallets', ['hash'])
  op.drop_constraint(constraint_name="wallets_portfolio_fkey", table_name="wallets", type_="foreignkey")
  op.drop_column('wallets', 'portfolio_id')
