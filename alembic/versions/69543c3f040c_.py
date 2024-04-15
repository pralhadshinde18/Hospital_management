"""empty message

Revision ID: 69543c3f040c
Revises: 
Create Date: 2024-04-14 13:08:14.753751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69543c3f040c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hospital',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('hospital_name', sa.String(length=100), nullable=False),
    sa.Column('area', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('email_address', sa.String(length=100), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('contact_number', sa.Integer(), nullable=True),
    sa.Column('whatsapp_number', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('contact_number', sa.Integer(), nullable=True),
    sa.Column('whatsapp_number', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('reference_by', sa.String(length=100), nullable=True),
    sa.Column('test_conducted_by', sa.String(length=100), nullable=True),
    sa.Column('test_hospital', sa.String(length=50), nullable=True),
    sa.Column('referred_doctor', sa.String(length=50), nullable=True),
    sa.Column('referred_hospital', sa.String(length=100), nullable=True),
    sa.Column('clinical_category', sa.String(length=100), nullable=True),
    sa.Column('clinical_sub_category', sa.String(length=20), nullable=True),
    sa.Column('test', sa.String(length=50), nullable=True),
    sa.Column('format', sa.String(length=50), nullable=True),
    sa.Column('exam_procedure', sa.String(length=50), nullable=True),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reporting_doctor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('hospital_name', sa.String(length=100), nullable=True),
    sa.Column('contact_number', sa.Integer(), nullable=True),
    sa.Column('whatsapp_number', sa.Integer(), nullable=True),
    sa.Column('email_address', sa.String(length=100), nullable=True),
    sa.Column('education', sa.String(length=100), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('speciality', sa.String(length=100), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('technician',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('hospital_name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('contact_number', sa.Integer(), nullable=True),
    sa.Column('whatsapp_number', sa.Integer(), nullable=True),
    sa.Column('email_address', sa.String(length=100), nullable=True),
    sa.Column('education', sa.String(length=100), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('patient_name', sa.String(length=100), nullable=True),
    sa.Column('examine_date', sa.Date(), nullable=True),
    sa.Column('report_status', sa.String(length=50), nullable=True),
    sa.Column('referred_doctor', sa.String(length=100), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_hospital_link',
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], )
    )
    op.create_table('document',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.String(), nullable=True),
    sa.Column('is_downloaded', sa.Boolean(), nullable=True),
    sa.Column('patient_file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_file_id'], ['patient_file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document')
    op.drop_table('patient_hospital_link')
    op.drop_table('patient_file')
    op.drop_table('technician')
    op.drop_table('reporting_doctor')
    op.drop_table('patient')
    op.drop_table('hospital')
    # ### end Alembic commands ###
