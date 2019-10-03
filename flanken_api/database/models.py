from flanken_api.database import db as pssql


class ProbioBloodReferral(pssql.Model):
    __tablename__ = "probio_bloodreferrals"
    crid = pssql.Column(pssql.Integer, primary_key=True, nullable=False)
    pnr  = pssql.Column(pssql.String, nullable=False)
    rid  = pssql.Column(pssql.String, nullable=False)
    datum = pssql.Column(pssql.Date, nullable=False)
    tid  = pssql.Column(pssql.String, nullable=False)
    sign = pssql.Column(pssql.Integer)
    countyletter  = pssql.Column(pssql.String, nullable=False)
    new = pssql.Column(pssql.String, nullable=False)
    progression = pssql.Column(pssql.String, nullable=False)
    follow_up    = pssql.Column(pssql.String, nullable=False)
    cf_dna1 = pssql.Column(pssql.String, nullable=False)
    cf_dna2 = pssql.Column(pssql.String, nullable=False)
    cf_dna3 = pssql.Column(pssql.String, nullable=False)
    kommentar = pssql.Column(pssql.String, nullable=False)
    filnamn = pssql.Column(pssql.String, nullable=False)
    def __repr__(self): 
        return "<ProbioReferral (crid='%s', pnr='%s', rid='%s', date='%s', filename='%s')>" % (self.crid,self.pnr,self.rid,self.datum,self.filnamn)


class PSFFBloodReferral(pssql.Model):
    __tablename__ = "psff_bloodreferrals"
    crid = pssql.Column(pssql.Integer, primary_key=True, nullable=False)
    rid  = pssql.Column(pssql.String, nullable=False)
    datum = pssql.Column(pssql.Date, nullable=False)
    tid  = pssql.Column(pssql.String, nullable=False)
    sign = pssql.Column(pssql.Integer)
    blood1 = pssql.Column(pssql.String, nullable=False)
    blood2 = pssql.Column(pssql.String, nullable=False)
    blood3 = pssql.Column(pssql.String, nullable=False)
    blood4 = pssql.Column(pssql.String, nullable=False)
    comment = pssql.Column(pssql.String, nullable=False)
    filnamn = pssql.Column(pssql.String, nullable=False)
    cdk = pssql.Column(pssql.String, nullable=False)
    def __repr__(self):
        return "<PSFFReferral (cdk='%s', rid='%s', date='%s', filename='%s')>" % (self.cdk,self.rid,self.datum,self.filnamn)
