from odoo import http
from odoo.http import request


class DeviceAPI(http.Controller):
    @http.route(
        "/api/device_logs",
        auth="public",
        type="http",
        methods=["GET"],
        csrf=False,
    )
    def get_logs(self, **kwargs):
        logs = request.env["device.log"].sudo().search([], order="created_at desc, id desc")
        payload = []

        for log in logs:
            payload.append(
                {
                    "id": log.id,
                    "name": log.name,
                    "device_id": log.device_id,
                    "voltage": log.voltage,
                    "current": log.current,
                    "state": log.state,
                    "created_at": log.created_at.isoformat() if log.created_at else None,
                }
            )

        return request.make_json_response(payload)
