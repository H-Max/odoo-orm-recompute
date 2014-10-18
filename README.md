Odoo ORM Recompute
==================

This module add two methods to OpenERP / Odoo ORM in order to recompute the values of function fields.

## Compatibility

This module has been tested and is functionnal with OpenERP 7.0 (with `bzr revno` of `./server` folder : 5292)

If you successfully has it working with Odoo 8+, please let me know.

## Purpose

If your function fields are correctly written (with the `store` / `lambda` method), you should not have to install this module because their values will be recomputed when needed.

However, you could one day have to recompute the complex values of one or more stored function fields (particularly if you change the function used to compute the value).

## Usage

If you want to recompute all the function fields of an object :

```python
	self.compute_all(cr, user, ids, context)
```
If you want to recompute a specific list of fields :

```python
	self.compute(cr, user, ids, ['field1','field2'], context)
```