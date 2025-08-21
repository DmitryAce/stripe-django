from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

def get_unfold_config() -> dict:
    return {
        "SITE_TITLE": "E-Commerce Admin",
        "SITE_HEADER": "E-Commerce Admin",
        "SITE_ICON": lambda request: static("logo.png"),
        "THEME": "dark",
        "SIDEBAR": {
            "navigation": [
                {
                    "title": _("🛍️ Товары"),
                    "icon": "inventory_2",
                    "collapsible": True,
                    "items": [
                        {
                            "title": _("📦 Все товары"),
                            "link": reverse_lazy("admin:items_item_changelist"),
                        },
                        {
                            "title": _("➕ Добавить товар"),
                            "link": reverse_lazy("admin:items_item_add"),
                        },
                    ],
                },
                {
                    "title": _("📋 Заказы"),
                    "icon": "receipt",
                    "collapsible": True,
                    "items": [
                        {
                            "title": _("📄 Все заказы"),
                            "link": reverse_lazy("admin:items_order_changelist"),
                        },
                        {
                            "title": _("🛒 Создать заказ"),
                            "link": reverse_lazy("admin:items_order_add"),
                        },
                    ],
                },
                {
                    "title": _("🎯 Скидки и налоги"),
                    "icon": "percent",
                    "collapsible": True,
                    "items": [
                        {
                            "title": _("💰 Скидки"),
                            "link": reverse_lazy("admin:items_discount_changelist"),
                        },
                        {
                            "title": _("📊 Налоги"),
                            "link": reverse_lazy("admin:items_tax_changelist"),
                        },
                    ],
                },
                {
                    "title": _("💳 Платежи"),
                    "icon": "payments",
                    "collapsible": True,
                    "items": [
                        {
                            "title": _("⚙️ Настройки Stripe"),
                            "link": reverse_lazy("admin:index"),
                        },
                    ],
                },
            ],
        }
    }