from pathlib import Path

from opal_common.scopes.scopes import ScopeConfig


class CeleryPullEngine:
    def fetch_source(self, base_dir: Path, scope: ScopeConfig):
        from opal_server import worker
        worker.fetch_source.delay(str(base_dir), scope.json())

