"""empty message

Revision ID: 00d6a2cd9dc0
Revises: 
Create Date: 2020-02-22 22:32:39.836469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00d6a2cd9dc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    print('HIIII')
    print(engine_name)
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('probio_bloodreferrals',
    sa.Column('crid', sa.Integer(), nullable=False),
    sa.Column('pnr', sa.String(), nullable=False),
    sa.Column('rid', sa.String(), nullable=False),
    sa.Column('datum', sa.Date(), nullable=False),
    sa.Column('tid', sa.String(), nullable=False),
    sa.Column('sign', sa.Integer(), nullable=True),
    sa.Column('countyletter', sa.String(), nullable=False),
    sa.Column('new', sa.String(), nullable=False),
    sa.Column('progression', sa.String(), nullable=False),
    sa.Column('follow_up', sa.String(), nullable=False),
    sa.Column('cf_dna1', sa.String(), nullable=False),
    sa.Column('cf_dna2', sa.String(), nullable=False),
    sa.Column('cf_dna3', sa.String(), nullable=False),
    sa.Column('kommentar', sa.String(), nullable=False),
    sa.Column('filnamn', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('crid')
    )
    op.create_table('psff_bloodreferrals',
    sa.Column('crid', sa.Integer(), nullable=False),
    sa.Column('rid', sa.String(), nullable=False),
    sa.Column('datum', sa.Date(), nullable=False),
    sa.Column('tid', sa.String(), nullable=False),
    sa.Column('sign', sa.Integer(), nullable=True),
    sa.Column('blood1', sa.String(), nullable=False),
    sa.Column('blood2', sa.String(), nullable=False),
    sa.Column('blood3', sa.String(), nullable=False),
    sa.Column('blood4', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('filnamn', sa.String(), nullable=False),
    sa.Column('cdk', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('crid')
    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('psff_bloodreferrals')
    op.drop_table('probio_bloodreferrals')
    # ### end Alembic commands ###


def upgrade_curation():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table_igv_germline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('PROJECT_ID', sa.String(), nullable=False),
    sa.Column('SDID', sa.String(), nullable=False),
    sa.Column('CAPTURE_ID', sa.String(), nullable=False),
    sa.Column('CHROM', sa.String(), nullable=True),
    sa.Column('START', sa.String(), nullable=True),
    sa.Column('END', sa.String(), nullable=True),
    sa.Column('REF', sa.String(), nullable=True),
    sa.Column('ALT', sa.String(), nullable=True),
    sa.Column('CALL', sa.String(), nullable=True),
    sa.Column('TAG', sa.String(), nullable=True),
    sa.Column('NOTES', sa.String(), nullable=True),
    sa.Column('GENE', sa.String(), nullable=True),
    sa.Column('IMPACT', sa.String(), nullable=True),
    sa.Column('CONSEQUENCE', sa.String(), nullable=True),
    sa.Column('HGVSp', sa.String(), nullable=True),
    sa.Column('N_DP', sa.String(), nullable=True),
    sa.Column('N_ALT', sa.String(), nullable=True),
    sa.Column('N_VAF', sa.String(), nullable=True),
    sa.Column('CLIN_SIG', sa.String(), nullable=True),
    sa.Column('gnomAD', sa.String(), nullable=True),
    sa.Column('BRCAEx', sa.String(), nullable=True),
    sa.Column('OncoKB', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('table_igv_somatic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('PROJECT_ID', sa.String(), nullable=False),
    sa.Column('SDID', sa.String(), nullable=False),
    sa.Column('CAPTURE_ID', sa.String(), nullable=False),
    sa.Column('CHROM', sa.String(), nullable=True),
    sa.Column('START', sa.String(), nullable=True),
    sa.Column('END', sa.String(), nullable=True),
    sa.Column('REF', sa.String(), nullable=True),
    sa.Column('ALT', sa.String(), nullable=True),
    sa.Column('CALL', sa.String(), nullable=True),
    sa.Column('TAG', sa.String(), nullable=True),
    sa.Column('NOTES', sa.String(), nullable=True),
    sa.Column('GENE', sa.String(), nullable=True),
    sa.Column('IMPACT', sa.String(), nullable=True),
    sa.Column('CONSEQUENCE', sa.String(), nullable=True),
    sa.Column('HGVSp', sa.String(), nullable=True),
    sa.Column('T_DP', sa.String(), nullable=True),
    sa.Column('T_ALT', sa.String(), nullable=True),
    sa.Column('T_VAF', sa.String(), nullable=True),
    sa.Column('N_DP', sa.String(), nullable=True),
    sa.Column('N_ALT', sa.String(), nullable=True),
    sa.Column('N_VAF', sa.String(), nullable=True),
    sa.Column('CLIN_SIG', sa.String(), nullable=True),
    sa.Column('gnomAD', sa.String(), nullable=True),
    sa.Column('BRCAEx', sa.String(), nullable=True),
    sa.Column('OncoKB', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('table_svs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('PROJECT_ID', sa.String(), nullable=False),
    sa.Column('SDID', sa.String(), nullable=False),
    sa.Column('CAPTURE_ID', sa.String(), nullable=False),
    sa.Column('CHROM_A', sa.String(), nullable=True),
    sa.Column('START_A', sa.String(), nullable=True),
    sa.Column('END_A', sa.String(), nullable=True),
    sa.Column('CHROM_B', sa.String(), nullable=True),
    sa.Column('START_B', sa.String(), nullable=True),
    sa.Column('END_B', sa.String(), nullable=True),
    sa.Column('SVTYPE', sa.String(), nullable=True),
    sa.Column('SV_LENGTH', sa.String(), nullable=True),
    sa.Column('SUPPORT_READS', sa.String(), nullable=True),
    sa.Column('TOOL', sa.String(), nullable=True),
    sa.Column('SAMPLE', sa.String(), nullable=True),
    sa.Column('GENE_A', sa.String(), nullable=True),
    sa.Column('IN_DESIGN_A', sa.String(), nullable=True),
    sa.Column('GENE_B', sa.String(), nullable=True),
    sa.Column('IN_DESIGN_B', sa.String(), nullable=True),
    sa.Column('GENE_A-GENE_B-sorted', sa.String(), nullable=True),
    sa.Column('CALL', sa.String(), nullable=True),
    sa.Column('TYPE', sa.String(), nullable=True),
    sa.Column('SECONDHIT', sa.String(), nullable=True),
    sa.Column('COMMENT', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_curation():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('table_svs')
    op.drop_table('table_igv_somatic')
    op.drop_table('table_igv_germline')
    # ### end Alembic commands ###

