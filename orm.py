# -*- encoding: utf-8 -*-
###############################################################################
# Add a compute and compute_all method to the ORM
# In order to recompute the values of function fields in OpenERP / Odoo objects
#
# Methods check user right on objets before computing the values
#
###############################################################################

from openerp.osv.orm import BaseModel
from openerp.osv import fields


def compute(self, cr, user, ids, vals, context=None):
    if vals is None:
        vals = []
    # Check that user has access right on the objet (do not check field rights, since it's function fields only)

    self.check_access_rights(cr, user, 'write')
    self._store_set_values(cr, user, ids, vals, context)

    return True


def compute_all(self, cr, user, ids, context=None):
    self.check_access_rights(cr, user, 'write')

    fields_to_compute = []

    for f in self._columns:
        if isinstance(self._columns[f], fields.function):
            fields_to_compute.append(f)

    if fields_to_compute:
        self.compute(cr, user, ids, fields_to_compute, context)

    return True

BaseModel.compute = compute
BaseModel.compute_all = compute_all
