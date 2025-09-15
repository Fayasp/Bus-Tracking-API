class ResponseInfo(object):
    def __init__(self, user=None, **args):
        self.response = {
            "message": args.get("message", ""),
            "data": args.get("data", {}),
            "errors": args.get("errors", {}),
        }
