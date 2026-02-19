import logging
from typing import Dict, List
from prometheus_client import generate_latest

class MetricCollector:
    def __init__(self):
        pass
    
    def collect_metrics(self) -> bytes:
        return generate_latest()

class MonitoringDashboard:
    def __init__(self):
        self.metrics = {}
    
    def update_metric(self, name: str, value: float) -> None:
        self.metrics[name] = value
    
    def get_dashboard_data(self) -> Dict:
        return self.metrics