
def m(request):
    if request.method not in ('GET', 'HEAD'):
        try:
            data = request.body
        except Exception:
            try:
                data = request.raw_post_data
            except Exception:
                # assume we had a partial read.
                try:
                    data = request.POST or '<unavailable>'
                except Exception:
                    data = '<unavailable>'
                else:
                    if isinstance(data, dict):
                        data = dict(
                            (k, v[0] if len(v) == 1 else v)
                            for k, v in data.items())
    return data
