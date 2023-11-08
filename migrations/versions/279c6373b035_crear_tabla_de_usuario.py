"""crear tabla de usuario

Revision ID: 279c6373b035
Revises: f2408b08dfdb
Create Date: 2023-08-08 22:54:40.228723

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '279c6373b035'
down_revision = 'f2408b08dfdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=11), nullable=False))
        batch_op.create_unique_constraint(None, ['correo_electronico'])
        batch_op.drop_column('contraseña')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contraseña', mysql.VARCHAR(length=11), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###