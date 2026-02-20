# -*- coding: utf-8 -*-
{
    "name": "SID - Sale Order Line Views (OV)",
    "version": "15.0.1.0.0",
    "category": "Sales",
    "summary": "Migración de vistas OV (tree/form/search) de sale.order.line desde Studio/export.",
    "author": "SID",
    "license": "LGPL-3",
    "depends": [
        "sale",
        "sale_stock",
        "stock",
        "sid_sale_line_custom_fields",
        "sid_purchase_delay_sync",
    ],
    "data": [
        "views/sale_order_line_form_readonly_ov.xml",
        "views/sale_order_line_search_ov.xml",
        "views/sale_order_line_tree_ov.xml",
    ],
    "installable": True,
    "application": False,
}
