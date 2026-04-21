# -*- coding: utf-8 -*-
{
    "name": "sid_sale_line_views_ov",
    "version": "15.0.1.1.0",
    "category": "Sales",
    "summary": "Refactor de vistas OV de sale.order.line con herencias más limpias y agrupadas.",
    "author": "oscarsidsa81",
    "license": "LGPL-3",
    "depends": [
        "sale",
        "sale_stock",
        "stock",
    ],
    "data": [
        "views/sale_order_line_form_readonly_ov.xml",
        "views/sale_order_line_search_ov.xml",
        "views/sale_order_line_tree_ov.xml",
    ],
    "installable": True,
    "application": False,
}
