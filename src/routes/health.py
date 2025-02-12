from flask import Blueprint, jsonify

from src.t import CheckModel, HealthResponseModel
from src.utils.check import check_memory, check_postgres_db, check_redis

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("/", methods=["GET"])
def get_health():
    checks: list[CheckModel] = []
    healthy: bool = True

    checks.append(check_memory())
    checks.append(check_redis())
    checks.append(check_postgres_db())

    for check in checks:
        if not check.healthy:
            healthy = False

    m = HealthResponseModel(
        healthy=healthy,
        checks=checks,
    )

    r = jsonify(m.model_dump(exclude_none=True))

    # Disable caching
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"

    if not healthy:
        r.status_code = 503

    return r
