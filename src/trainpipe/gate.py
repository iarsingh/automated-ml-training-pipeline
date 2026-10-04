class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if int(body.get("rows") or 0) < 10: failed.append("too_few_rows")\n    if not body.get("target"): failed.append("missing_target")
    return {"passed": not failed, "failed": failed, "applied": False}
