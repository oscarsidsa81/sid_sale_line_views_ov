# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    """Vincula el XML ID estable a un grupo Operarios existente si ya existe en la BD."""
    env = api.Environment(cr, SUPERUSER_ID, {})

    xmlid = env["ir.model.data"].search([
        ("module", "=", "sid_sale_line_views_ov"),
        ("name", "=", "group_operarios"),
        ("model", "=", "res.groups"),
    ], limit=1)
    if not xmlid:
        return

    current_group = env["res.groups"].browse(xmlid.res_id)
    category_inventory = env.ref("base.module_category_inventory", raise_if_not_found=False)

    domain = [("name", "=", "Operarios")]
    if category_inventory:
        domain.append(("category_id", "=", category_inventory.id))

    existing_group = env["res.groups"].search(domain, order="id asc", limit=1)

    if existing_group and existing_group.id != current_group.id:
        xmlid.res_id = existing_group.id
        if current_group.exists():
            current_group.unlink()
