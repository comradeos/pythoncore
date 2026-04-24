import logging
import os

import requests

from odoo import _, fields, models

_LOGGER = logging.getLogger(__name__)


class DeviceLog(models.Model):
    _name = "device.log"
    _description = "Device Log"
    _order = "created_at desc, id desc"

    name = fields.Char(required=True)
    device_id = fields.Char(required=True)
    voltage = fields.Float(readonly=True)
    current = fields.Float(readonly=True)
    created_at = fields.Datetime(default=fields.Datetime.now, readonly=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("loaded", "Loaded"),
            ("error", "Error"),
        ],
        default="draft",
        readonly=True,
        copy=False,
    )
    last_error = fields.Text(readonly=True, copy=False)

    def _get_device_api_base_url(self):
        return os.getenv("DEVICE_API_URL", "http://device-api:8080").rstrip("/")

    def action_fetch(self):
        notification = False

        for rec in self:
            endpoint = f"{self._get_device_api_base_url()}/device/{rec.device_id}"
            try:
                response = requests.get(endpoint, timeout=5)
                response.raise_for_status()
                data = response.json()

                rec.write(
                    {
                        "voltage": data.get("voltage"),
                        "current": data.get("current"),
                        "state": "loaded",
                        "last_error": False,
                    }
                )
            except (requests.RequestException, ValueError) as err:
                _LOGGER.exception("Failed to load device data for %s", rec.device_id)
                rec.write(
                    {
                        "state": "error",
                        "last_error": str(err),
                    }
                )

                notification = {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "title": _("Device API Error"),
                        "message": _(
                            "Unable to load data for device '%(device)s' from %(url)s. "
                            "Details: %(details)s"
                        )
                        % {
                            "device": rec.device_id,
                            "url": endpoint,
                            "details": str(err),
                        },
                        "type": "danger",
                        "sticky": True,
                    },
                }

        return notification
